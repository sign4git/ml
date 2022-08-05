from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import cross_val_score
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from azureml.core import Workspace, Datastore, Dataset, Experiment, Run

import pandas as pd

ws = Workspace.from_config()
raw_df = pd.read_csv('./Data/loan_prediction_updated.csv')

df = raw_df.copy()
df_describe = df.describe()
df_info = df.info()
df.drop(columns=['Loan_ID'], inplace=True)

print(df.isnull().sum())
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

non_numerical_columns = df.select_dtypes(include='object')
numerical_columns = df.select_dtypes(exclude='object')

for column in non_numerical_columns.columns:
    print("Column:: ", column, " Unique Values:: ",
          non_numerical_columns[column].unique())

##Treating Ordinal Features
dependents_dictionary = {"0": 0, "1": 1, "2": 2, "3+": 3}
property_area = {"Rural": 0, "Semiurban": 1, "Urban": 2}
loan_status = {"N": 0, "Y": 1}

df["Dependents"] = df["Dependents"].map(dependents_dictionary)
non_numerical_columns.drop(columns=["Dependents"], inplace=True)

df["Property_Area"] = df["Property_Area"].map(property_area)
non_numerical_columns.drop(columns=["Property_Area"], inplace=True)

df["Loan_Status"] = df["Loan_Status"].map(loan_status)
non_numerical_columns.drop(columns=["Loan_Status"], inplace=True)


#Organize features and Labels
X = df.drop(columns=['Loan_Status'])
y = df['Loan_Status']


#Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.30,
                                                    random_state=42,
                                                    stratify=y)
print(X_train.columns)

#Encode Categorical Features
for column in non_numerical_columns.columns:
    if column in X_train.columns:
        encode = LabelEncoder()
        X_train[column] = encode.fit_transform(X_train[column])
        X_test[column] = encode.transform(X_test[column])

#Scale the numerical features
for column in X_train.columns:
    scale = StandardScaler()
    X_train_scaled = scale.fit_transform(X_train)
    X_test_scaled = scale.transform(X_test)

#Calculate crossvalidation score for the chosen model
xgb = XGBClassifier(n_estimators=25)
train_accuracy_score = cross_val_score(
    xgb, X_train_scaled, y_train, cv=5, scoring='accuracy')

#Train the model
xgbmodel = xgb.fit(X_train_scaled, y_train)

#Predict using the trained model
y_pred = xgbmodel.predict(X_test_scaled)

#Calculate the metrics
test_accuracy_score = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

#Organize predict probability
prob_list = []
predict_probability = xgbmodel.predict_proba(X_test_scaled)
for i in predict_probability:
    prob_list.append(i[1])


#Add Actuals, Predictions and Predict Probability
X_test["Actual"] = y_test
X_test["prediction"] = y_pred
X_test["predict_proba"] = prob_list

#Form confusion matric object
cm_dictionary = {
    "schema_type": "confusion_matrix",
    "schema_version": "1.0.0",
    "data": {
        "class_labels": ["0", "1"],
        "matrix": cm.tolist()
    }
}

#Get the run context from the job
run = Run.get_context()

#Log the metrics
run.log("Cross Validation Accuracy Train", train_accuracy_score)
run.log("Test_Accuracy", test_accuracy_score)
run.log_confusion_matrix(name="Confusion Matrix for Loan", value=cm_dictionary)

#Write output file
X_test.to_csv("./outputs/loan_trunc.csv", index=False)

#complete the run
run.complete()
