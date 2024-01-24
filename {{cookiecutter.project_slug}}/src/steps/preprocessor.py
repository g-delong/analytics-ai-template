import pandas as pd
from zenml import step


@step
def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    replace the following dummy logic as needed
    """

    df["DateOfVisit"] = pd.to_datetime(df["DateOfVisit"])

    return df
