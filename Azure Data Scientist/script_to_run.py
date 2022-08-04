from azureml.core import Workspace,Datastore,Dataset,Run


ws=Workspace.from_config()

my_data_store=Datastore.get(workspace=ws, datastore_name='business_datastore')
my_data_set=Dataset.get_by_name(workspace=ws, name='Loan Prediction')
df= my_data_set.to_pandas_dataframe()

run = Run.get_context()

null_df=df.isnull().sum()

for col in null_df.index:
    run.log(col,null_df[col])


new_df = df[["Gender", "Married", "Education", "Loan_Status"]]
new_df.to_csv("./outputs/loan_trunc.csv", index=False)

run.complete()
