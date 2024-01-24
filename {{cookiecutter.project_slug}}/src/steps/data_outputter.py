import os
import tempfile

import pandas as pd
from zenml import step
from zenml.client import Client
from zenml.io import fileio

PROJECT_SLUG = "{{cookiecutter.project_slug}}"
PATH = "data/processed"
FILENAME = "data.parquet"


@step
def output_data_local(df: pd.DataFrame) -> None:
    """
    replace the following dummy logic as needed
    """
    filepath = os.path.join(PATH, FILENAME)
    os.makedirs(PATH, exist_ok=True)

    df.to_parquet(filepath)


@step
def output_data_s3(df: pd.DataFrame) -> None:
    """
    replace the following dummy logic as needed
    """
    client = Client()
    root_path = client.active_stack.artifact_store.path
    artifact_path = os.path.join(root_path, PROJECT_SLUG, PATH)
    artifact_uri = os.path.join(artifact_path, FILENAME)
    fileio.makedirs(artifact_path)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".parquet", delete=True) as f:
        df.to_parquet(f.name)
        # Copy it into artifact store
        fileio.copy(f.name, artifact_uri, overwrite=True)
