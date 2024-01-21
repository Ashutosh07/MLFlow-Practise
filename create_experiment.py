import mlflow

if __name__ == "__main__":
    mlflow.create_experiment(
        name = "testng_mlflow1",
        artifact_location= "testing_mlflow1_artefacts",
        tags={"env": "dev", "version": "1.0.0"} 
    )

