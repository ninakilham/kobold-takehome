"""Utility functions for soil geochemistry interpolation."""
    
import pandas as pd
import matplotlib.pyplot as plt


def check_if_empty(df: pd.DataFrame, var: str) -> pd.DataFrame:
    """checks and removes any no data values in a series 

    Args:
        df (pd.DataFrame): DataFrame with variable
        var (str): column to check

    Returns:
        pd.DataFrame: new frame with no data values removed
    """
    values = df.copy().dropna(subset=[var])
    if len(values) < len(df):
        print(f'Dataframe column {var} contains {df[var].isna().sum()} no data values!')
        
    return values
    
def plot_overview(df: pd.DataFrame, var: str, label: str, ax):
    """Overview map of a column at x,y locations.

    Args:
        df (pd.DataFrame): x, y and z values
        var (str): column to plot
        label (str): variable label
        ax (_type_): plot axis
    """
    cmap = ax.scatter(df.x, df.y, s=50, c=df[var], cmap='plasma')
    ax.set_title(f'{label}')
    plt.colorbar(cmap, ax=ax)
    
def plot_hist(df: pd.DataFrame, var: str, label: str, ax):
    """Histogram of a variable.

    Args:
        df (pd.DataFrame): DataFrame with variable
        var (str): column to plot
        label (str): variable label
        ax (_type_): plot axis
    """
    df.plot.hist(column=[var], bins=50, ax=ax)
    ax.set_ylabel(f'{label}')