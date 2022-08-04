from azureml.core import Workspace,Datastore
ws= Workspace.from_config()


#Register an Existing BLOB datastore
my_data_store=Datastore.register_azure_blob_container(workspace=ws,
                                                      datastore_name="business_datastore",
                                                      container_name="businessblobcontainer",
                                                      account_name="businessstorageaccount",
                                                      account_key="phuIWBH2hOthRT46RymOsWUuhwUmYS6YvxK75WBDY6OotY6DTqvXYWxh8BDGVcK+YtS/v4rylBw7+AStHO4m/Q==")