from azureml.core import Workspace,Datastore,Dataset

ws= Workspace.from_config()
my_datastore=Datastore.get(workspace=ws, datastore_name="business_datastore")

print([ws.datasets.keys()])
my_dataset=Dataset.get_by_name(ws, name="Loan Prediction Updated Datset")

#convert dataset to dataframe
df = my_dataset.to_pandas_dataframe()
print(type(df))

#UPLOAD CLIPPED DATASET
clipped_df=df[["Gender","Married","Loan_Status"]]
print(clipped_df.columns)

#upload dataframe and register to datasets
Dataset.Tabular.register_pandas_dataframe(dataframe=clipped_df, target=my_datastore, name="Loan Clipped Dataframe")
