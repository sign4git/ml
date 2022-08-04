#import workspace from azure ml SDK 
from azureml.core import Workspace

#Create a workspace
ws=Workspace.create(name='MLWorkspace',
                    subscription_id='3291212d-f305-40a5-a60c-2bf6825d4013',
                    resource_group='MachineLearningRG',
                    create_resource_group=True,
                    location='eastus2')
#saving a workspace
save_config=Workspace.write_config(ws)
