from zenml import pipeline
from zenml.client import Client

from src.steps.data_loader import load_data_local, load_data_s3
from src.steps.data_outputter import output_data_local, output_data_s3
from src.steps.preprocessor import preprocess
from src.steps.processor import process


@pipeline
def {{cookiecutter.project_python_slug}}_pipeline():
    client = Client()
    flavor = client.active_stack_model.components["artifact_store"][0].flavor
    if flavor == "local":
        data = load_data_local()
    else:
        data = load_data_s3()
    prep_data = preprocess(df=data)
    proc_data = process(df=prep_data)
    if flavor == "local":
        output_data_local(proc_data)
    else:
        output_data_s3(proc_data)
