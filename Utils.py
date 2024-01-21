import mlflow

def create_experiments(Experiment_name : str, artifact_locations: str, tags_list: dict[str,any])-> str:
    try:
        experiment_details= mlflow.create_experiment(name= Experiment_name, artifact_location= artifact_locations, tags = tags_list)

    except:
        print(f"Experiment {Experiment_name} aldready exists")
        experiment_details = mlflow.get_experiment_by_name(Experiment_name)

    return experiment_details

print("Hello World")#This gets executed first when this library is imported as it is not under main function