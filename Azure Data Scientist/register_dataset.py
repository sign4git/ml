from azureml.core import Workspace,Datastore,Dataset

#get workspace
ws=Workspace.from_config()

#get datastore
my_data_store=Datastore.get(workspace=ws, datastore_name="business_datastore") 


file_path= (my_data_store,'loan_prediction_updated.csv')
my_dataset=Dataset.Tabular.from_delimited_files(path=file_path)
my_dataset=my_dataset.register(workspace=ws, 
                            name="Loan Prediction Updated Datset")