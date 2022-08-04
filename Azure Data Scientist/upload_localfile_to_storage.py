from azureml.core import Workspace,Datastore

ws=Workspace.from_config()
my_data_store=Datastore.get(workspace=ws,datastore_name="business_datastore")

#upload files to storage account
files= ["./.azureml/config.json"]
my_data_store.upload_files(files=files,
                           target_path="./Python/",
                           overwrite=True)

#upload folder to storage account
my_data_store.upload(src_dir="./.azureml/",
                     target_path="./MYCONFIG/",
                     overwrite=True)