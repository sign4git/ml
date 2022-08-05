from azureml.core import Workspace, Experiment, ScriptRunConfig
from azureml.core.environment import Environment, CondaDependencies
ws = Workspace.from_config()

my_exp = Experiment(workspace=ws, name="loan_prediction_xgboost")
my_environment = Environment(name="loan_prediction_environment")
my_dependencies = CondaDependencies.create(conda_packages=['scikit-learn',
                                                           'xgboost', 'pandas'])
my_environment.python.conda_dependencies = my_dependencies
my_environment.register(ws)
script_config = ScriptRunConfig(source_directory='.',
                                script='loan_prediction_training_script.py',
                                environment=my_environment)

run = my_exp.submit(config=script_config)

run.wait_for_completion()
