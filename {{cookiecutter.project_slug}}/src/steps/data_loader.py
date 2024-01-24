import os
import random
from datetime import datetime, timedelta

import pandas as pd
from zenml import step
from zenml.client import Client

PATH = "data/raw"
FILENAME = "data.parquet"
PROJECT_SLUG = "{{cookiecutter.project_slug}}"


@step
def load_data_local() -> pd.DataFrame:
    """
    replace the following dummy logic as needed
    """

    filepath = os.path.join(PATH, FILENAME)

    # pretend the data was already there...
    os.makedirs(PATH, exist_ok=True)
    data = get_dummy_data(20)
    df = pd.DataFrame(data)
    df.to_parquet(filepath)

    # now read the data
    df = pd.read_parquet(filepath)

    return df


@step
def load_data_s3() -> pd.DataFrame:
    """
    replace the following dummy logic as needed
    """
    client = Client()
    store = client.active_stack.artifact_store
    root_path = store.path

    # assuming the data exists at the s3 path
    artifact_path = os.path.join(root_path, PROJECT_SLUG, PATH, FILENAME)

    with store.open(artifact_path, "rb") as f:
        df = pd.read_parquet(f)

    return df


def get_dummy_data(num_records=100) -> dict:
    # Sample clinical data fields
    patients = [f"Patient_{i}" for i in range(num_records)]
    ages = [random.randint(18, 80) for _ in range(num_records)]
    blood_types = ["A", "B", "AB", "O"]
    random.shuffle(blood_types)
    genders = ["Male", "Female"]
    dates_of_visit = [
        str(datetime(2022, 1, 1) + timedelta(days=random.randint(1, 365)))
        for _ in range(num_records)
    ]

    # Creating a dictionary from the sample data
    data_dict = {
        "PatientID": patients,
        "Age": ages,
        "BloodType": [random.choice(blood_types) for _ in range(num_records)],
        "Gender": [random.choice(genders) for _ in range(num_records)],
        "DateOfVisit": dates_of_visit,
    }

    return data_dict
