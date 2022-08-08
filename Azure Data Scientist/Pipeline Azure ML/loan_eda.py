print("@@@@@@@@@@@")
import argparse
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import cross_val_score
from xgboost import XGBClassifier
from azureml.core import Workspace, Datastore, Dataset, Experiment, Run

import pandas as pd
parser=argparse.ArgumentParser()
parser.add_argument("--datafolder",type=str)
args=parser.parse_args()
run=Run.get_context()
ws=Workspace.from_config(path='./Azure Data Scientist')
raw_df = run.input_datasets['raw_data'].to_pandas_dataframe()
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
#non_numerical_columns.drop(columns=["Loan_Status"], inplace=True)

import os
os.makedirs(args.datafolder, exist_ok=True)
path = os.path.join(args.datafolder, 'defaults_prep.csv')

df.to_csv(path, index=False)
run.log("EDA","This is EDA Logs")
print("dummy")
run.complete()