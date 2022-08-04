from azureml.core import Workspace,Datastore,Dataset,Experiment,Run,ScriptRunConfig,Environment
from azureml.core.environment import CondaDependencies 
ws= Workspace.create(name='MLWorkspace',
                      resource_group='MachineLearningRG',
                      create_resource_group=True,
                      location='eastus2',
                      subscription_id='3291212d-f305-40a5-a60c-2bf6825d4013')

ws.write_config()

my_data_store=Datastore.register_azure_blob_container(workspace=ws, 
                                                      datastore_name='business_datastore', 
                                                      container_name='businessblobcontainer',
                                                      account_name='businessstorageaccount',
                                                      account_key='7yH9Bb0EbKX0vjMj6flMqPMWNS/NkiWvWkJJyoAWVPOyokEW+7HTXAmZOD6namYBuWFfIIalA02u+AStvpiHgA==')
my_datastore=Datastore.get(workspace=ws, datastore_name='business_datastore')
my_datastore.upload_files(files=['./Data/loan_prediction_updated.csv'],
                           overwrite=True,
                           target_path='./Loan Data/')

# data_path=(my_datastore,'loan_prediction_updated.csv')
# my_dataset=Dataset.Tabular.from_delimited_files(path=data_path)
# my_dataset.register(workspace=ws, name="Loan Prediction File")

experiment= Experiment(workspace=ws, name='Loan-SDK')

my_environment=Environment(name="SDK_Environment")
my_dependencies=CondaDependencies.create(conda_packages=['pandas'])
my_environment.python.conda_dependencies= my_dependencies
my_environment.register(ws)

script_config=ScriptRunConfig(source_directory='.',
                              script='script_to_run.py',
                              environment=my_environment)
run = experiment.submit(config=script_config)

run.wait_for_completion()