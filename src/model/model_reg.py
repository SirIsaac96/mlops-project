import json
from mlflow.tracking import MlflowClient
import mlflow
import dagshub

# Initialize DagsHub for experiment tracking
dagshub.init(repo_owner='SirIsaac96', repo_name='mlops-project', mlflow=True)

# Set the experiment name in MLflow
mlflow.set_experiment("Final_Model")

# Set the tracking URI for MLflow to log the experiment in DagsHub
mlflow.set_tracking_uri("https://dagshub.com/SirIsaac96/mlops-project.mlflow")

# Load the run ID and model name from the saved JSON file
reports_path = "reports/run_info.json"
with open(reports_path, 'r') as file:
    run_info = json.load(file)

run_id = run_info['run_id'] # Fetch run id from the JSON file
model_name = run_info['model_name']  # Fetch model name from the JSON file

# Create an MLflow client
client = MlflowClient()

# Create the model URI
model_uri = f"runs:/{run_id}/Best_Model"

# Register the model
reg = mlflow.register_model(model_uri, model_name)

# Get the model version
model_version = reg.version  # Get the registered model version

print(f"Model {model_name} registered as version {model_version}.")