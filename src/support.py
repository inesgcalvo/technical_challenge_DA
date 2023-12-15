import re
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Functions for DataFrames
    
def view_nan(df: pd.DataFrame) -> None:
    """
    Visualize the NaN values per column in the DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.

    Returns:
    None
    """
    fig = plt.figure(figsize = (10, 6), facecolor = 'none') 
    ax = fig.add_subplot(111, facecolor = 'none')
    sns.heatmap(df.isna(),           
                yticklabels = False,  
                cmap = 'magma',     
                cbar = False)
    ax.tick_params(colors = 'grey')
    ax.xaxis.label.set_color('grey')
    plt.show();