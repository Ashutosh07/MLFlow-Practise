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

#print("New Experiment has been created with ID: %s"%(First_ML_Experiement.experiment_id))
#print("Experiment name is: {}".format(First_ML_Experiement.name))
#print("New Experiment has been created with ID: {}".format(First_ML_Experiement.experiment_id))