"""Utility functions for soil geochemistry interpolation."""
    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib_scalebar.scalebar import ScaleBar


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
    
def plot_variogram_model_grids(V, models=('spherical', 'exponential', 'gaussian',
                                           'matern', 'stable', 'cubic')):
    V.bin_func = 'scott'
    _, _a = plt.subplots(2,3, figsize=(12, 6), sharex=True, sharey=True)
    axes = _a.flatten()
    for i, model in enumerate(models):
        V.model = model
        V.plot(axes=axes[i], hist=False, show=False)
        axes[i].set_title('Model: %s; RMSE: %.2f' % (model, V.rmse))
        
    plt.tight_layout()
    
def plot_krigging_results(df: pd.DataFrame, var: str, field, s2):
    """Krigging results with error plotted over a gird.

    Args:
        df (pd.DataFrame): x, y, vals
        var (str): column to be interpolated
        field (arr): array of interpolated values
        s2 (arr): array of krigging errors

    Returns:
        plt: matplotlib figure handle
    """
    x = df.x.values
    y = df.y.values
    vals = df[var].values
    _, axes = plt.subplots(1,2, figsize=(10,5))

    # rescale the coordinates to fit the interpolation raster
    x_ = (x - x.min()) / (x.max() - x.min()) * 100
    y_ = (y - y.min()) / (y.max() - y.min()) * 100

    cmap1 = axes[0].matshow(field.T, origin='lower', cmap='plasma',
                            vmin=vals.min(), vmax=vals.max())
    axes[0].set_title(f'{var} Concentrations (ppm)')
    axes[0].plot(x_, y_, '+w')
    axes[0].set_xlim((0, 100))
    axes[0].set_ylim((0, 100))
    scalebar = ScaleBar(0.2, units="m") 
    axes[0].add_artist(scalebar)
    plt.colorbar(cmap1, ax=axes[0])

    cmap2 = axes[1].matshow(s2.T, origin='lower', cmap='YlGn_r')
    axes[1].set_title('Kriging Error')
    plt.colorbar(cmap2, ax=axes[1], format="%.1f")
    axes[1].plot(x_, y_, '+w')
    axes[1].set_xlim((0, 100))
    axes[1].set_ylim((0, 100))

    plt.tight_layout()
    
    return plt

def build_grid(df):
    x = df.x.values
    y = df.y.values
    xx, yy = np.mgrid[x.min():x.max():100j, y.min():y.max():100j]
    
    return xx, yy