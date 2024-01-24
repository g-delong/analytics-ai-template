import numpy as np
import pandas as pd
from zenml import step


@step
def process(df: pd.DataFrame) -> pd.DataFrame:
    """
    replace the following dummy logic as needed
    """

    df["RiskScore"] = np.random.rand(len(df))

    print(df.head())
    return df
