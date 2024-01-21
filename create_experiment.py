import mlflow

from Utils import * as ut

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

First_ML_Experiemnt = ut.create_experiments("First_ML_Experiemnt", ,tags)