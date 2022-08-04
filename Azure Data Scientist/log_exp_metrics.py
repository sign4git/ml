from azureml.core import Workspace,Experiment,Dataset

ws=Workspace.from_config()
print(ws.datasets.keys())
my_dataset=Dataset.get_by_name(workspace=ws,
                               name='Loan Prediction Updated Datset')

#Create or get experiment
experiment= Experiment(workspace=ws,
                       name='Loan-SDK-Experiment-1')

#start run

new_run=experiment.start_logging()

#convert dataset to dataframe
df = my_dataset.to_pandas_dataframe()
df_length= len(df)
null_df = df.isnull().sum()

## Logging metrics
new_run.log("DataFrame Length", df_length)
for column in null_df.index:
    print(null_df[column])
    new_run.log(column,null_df[column])
    
##end run   
new_run.complete()
    


