import mlflow
import dagshub

# Set the tracking URI to DagsHub
mlflow.set_tracking_uri("https://dagshub.com/SirIsaac96/mlops-project.mlflow")

dagshub.init(repo_owner='SirIsaac96', repo_name='mlops-project', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)