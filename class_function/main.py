import numpy as np

def lnorm(x,y, h =2):
    val = 0.0
    if x.shape == y.shape:
        for i in range(x.shape[0]):
            val = val + np.power(np.abs(x[i] - y[i]), h)

    return np.power(val, 1/h)

x = np.array([1,2,3,1])
y = np.array([3,5,5,5])

print(lnorm(x,y,20))