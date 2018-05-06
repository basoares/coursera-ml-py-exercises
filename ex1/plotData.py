'''

Stanford Machine Learning (Coursera) - Python

plotData plots the data points into a new figure 
   plotData(data) plots the data points and gives the figure axes labels of
   population and profit.

Parameters
----------
    X: array
        X-axis values

    y: array
        Y-axis values

Released under the MIT License <http://opensource.org/licenses/mit-license.php>

'''
__version__ = '0.1'
__all__ = ['plotData']

import matplotlib.pyplot as plt

def plotData(X, y):
# ====================== YOUR CODE HERE ======================
# Instructions: Plot the training data into a figure using the 
#               "figure" and "plot" commands. Set the axes labels using
#               the "xlabel" and "ylabel" commands. Assume the 
#               population and revenue data have been passed in
#               as the x and y arguments of this function.
#
# Hint: You can use the 'rx' option with plot to have the markers
#       appear as red crosses. Furthermore, you can make the
#       markers larger by using plot(..., 'rx', 'MarkerSize', 10);

    plt.figure(figsize=(10,6))
    plt.grid(True)
    plt.show()

# ============================================================
