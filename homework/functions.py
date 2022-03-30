
# Jesus Minjares 
# Master of Science in Computer Engineering

import numpy as np
from scipy import stats

def mean(data):
    """Returns the mean of the numpy"""
    return np.mean(data)

def median(data):
    """Returns the median of the numpy"""
    return np.median(data)

def mode_using_scipy(data):
    """Return a list of [value, count]"""
    return stats.mode(data, axis = 0)

def mode(data):
    """Return the mode of the numpy, with all max occurences"""
    vals, counts = np.unique(data, return_counts=True)
    mode_value = np.argwhere(counts == np.max(counts))

    return vals[mode_value]

def midrange(data):
    """Returns the midrange value of the numpy array"""
    return (np.max(data) + np.min(data)) / 2

def five_number_summmary(data):
    five_num = {
                'min':np.min(data),
                'q1': np.percentile(data,[25]),
                'median': np.median(data),
                'q3': np.percentile(data,[75]),
                'max': np.max(data),
                }
    return five_num
    
# Euclidean
def euclidean(x,y):
    val = 0.0
    if x.shape == y.shape:
        for i in range(x.shape[0]):
            val = val + np.power(np.abs(x[i] - y[i]),2)

    return np.power(val, 1/2)

# Manhattan
def manhattan(x,y):
    val = 0.0
    if x.shape == y.shape:
        for i in range(x.shape[0]):
            val = val + np.abs(x[i] - y[i])

    return val

# Minkowski
def minkowski(x,y,h):
    val = 0.0
    if x.shape == y.shape:
        for i in range(x.shape[0]):
            val = val + np.power(np.abs(x[i] - y[i]), h)

    return np.power(val, 1/h)

#  supremum distance
def supremum_distance(x,y):
    return np.abs(np.max(x) - np.max(y))


def lnorm(x,y, h =2):
    """
    euclidean-> h = 2
    manhattan-> h = 1
    minkowski-> h = any number
    """
    val = 0.0
    if x.shape == y.shape:
        for i in range(x.shape[0]):
            val = val + np.power(np.abs(x[i] - y[i]), h)

    return np.power(val, 1/h)