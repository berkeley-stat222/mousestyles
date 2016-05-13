import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_performance(result):
    """
    Plots the performance of classification model.It
    is a side-by-side barplot. For each strain, it plots
    the precision, recall and F-1 measure.
    Parameters
    ----------
    result: dataframe, columns of precision, recall and
            F-1 measure.
    Returns
    -------
    None
    """
    N = 16
    ind = np.arange(N)  # the x locations for the groups
    width = 0.2
    fig = plt.figure()
    ax = fig.add_subplot(111)
    precision = result.iloc[:, 0]
    rects1 = ax.bar(ind, precision, width, color='Coral')
    recall = result.iloc[:, 1]
    rects2 = ax.bar(ind+width, recall, width, color='LightSeaGreen')
    f1 = result.iloc[:, 2]
    rects3 = ax.bar(ind+width*2, f1, width, color='DodgerBlue')
    ax.set_ylabel('Accuracy')
    ax.set_xlabel('Strains')
    ax.set_xticks(ind+width)
    ax.set_xticklabels(range(16))
    ax.legend((rects1[0], rects2[0], rects3[0]), ('precision', 'recall', 'F1'))
    plt.show()
    return()
