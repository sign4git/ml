from azureml.core import Workspace,Datastore,Dataset

#GET WORKSPACE FROM CONFIG
ws=Workspace.from_config()

#GET LIST OF WORKSPACES
ws_list=Workspace.list(subscription_id='3291212d-f305-40a5-a60c-2bf6825d4013')
print(list(ws_list))

#get datastore
my_data_store=Datastore.get(workspace=ws, datastore_name="business_datastore") 
print(my_data_store)

#GET default DATASTORES
dstore_default=Datastore.get_default(workspace=ws)
print(dstore_default)

#GET LIST OF ALL DATASTORES
dstore_list=ws.datastores
print(list(dstore_list))

#GET ALL DATASETS
dset_list=ws.datasets.keys()
print(list(dset_list))

#GET A DATASET
my_dataset=Dataset.get_by_name(ws,name='Loan Prediction Updated Datset')
print(my_dataset)
