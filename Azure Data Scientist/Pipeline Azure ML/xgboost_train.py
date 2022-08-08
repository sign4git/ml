from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import cross_val_score
from xgboost import XGBClassifier
from azureml.core import Workspace, Datastore, Dataset, Experiment, Run
run=Run.get_context()

import argparse
my_arg=argparse.ArgumentParser()
my_arg.add_argument("--datafolder",type=str)
args=my_arg.parse_args()

import os
import pandas as pd

path = os.path.join(args.datafolder, 'defaults_prep.csv')
df = pd.read_csv(path)

#Organize features and Labels
X = df.drop(columns=['Loan_Status'])
y = df['Loan_Status']


#Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.30,
                                                    random_state=42,
                                                    stratify=y)
print(X_train.columns)
non_numerical_columns = df.select_dtypes(include='object')
numerical_columns = df.select_dtypes(exclude='object')
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


#Log the metrics
run.log("Cross Validation Accuracy Train", train_accuracy_score)
run.log("Test_Accuracy", test_accuracy_score)
run.log_confusion_matrix(name="Confusion Matrix for Loan", value=cm_dictionary)

#Write output file
X_test.to_csv("./outputs/loan_trunc.csv", index=False)

#complete the run
run.complete()
