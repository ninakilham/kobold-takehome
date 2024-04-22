"""Utility functions for soil geochemistry interpolation."""
    
import pandas as pd

def check_if_empty(df: pd.DataFrame, subset: list) -> pd.DataFrame:
    """checks for any no data values in a series

    Args:
        df (pd.DataFrame): _description_
        subset (list): _description_

    Returns:
        pd.DataFrame: _description_
    """