from azureml.core import Workspace,Experiment

ws=Workspace.from_config()

#Create Experiment
experiment = Experiment(ws, name="Loan-SDK-Experiment-1")

#Run the experiment and Log
new_run= experiment.start_logging()


#Stop or complete the experiment
new_run.complete()
