import mlflow

from Utils import *

if __name__ == "__main__":
    mlflow.create_experiment(
        name = "testing_mlflow1",
        artifact_location= "testing_mlflow1_artefacts",
        tags={"env": "dev", "version": "1.0.0"} 
    )

tags = {
    "version" : "1.0.0",
    "env" : "test",
    "Author" : "Ashutosh Shukla"
}

First_ML_Experiement = create_experiments("First_ML_Experiemnt", "first_test_flow.txt",tags)
print(First_ML_Experiement)

print("New Experiment has been created with ID: %s"%First_ML_Experiement)
print("Experiment name is: {}".format(mlflow.get_experiment(First_ML_Experiement).name))
print("New Experiment has been created with ID: {}".format(mlflow.get_experiment_by_name(mlflow.get_experiment_(First_ML_Experiement).name)))

experiment = get_mlflow_experiment(experiment_id=First_ML_Experiement)
with mlflow.start_run(run_name ="First_Run", experiment_id=experiment.experiment_id) as run:
    # Your machine learning code goes here
        mlflow.log_param("learning_rate",0.01)
        # print run info    
        print("run_id: {}".format(run.info.run_id))
        print("experiment_id: {}".format(run.info.experiment_id))
        print("status: {}".format(run.info.status))
        print("start_time: {}".format(run.info.start_time))
        print("end_time: {}".format(run.info.end_time))
        print("lifecycle_stage: {}".format(run.info.lifecycle_stage))