import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def normalize(x):
    return (x - np.min(x))/ (np.max(x) - np.min(x))

def lnorm(x,y, h =2):
    val = 0.0
    if x.shape == y.shape:
        for i in range(x.shape[0]):
            val = val + np.power(np.abs(x[i] - y[i]), h)

    return np.power(val, 1/h)
#     return np.power(np.power(np.abs(x-y),h).sum(), 1/h) # one-liner

x = np.array([1,2])
y = np.array([3,5])

print(lnorm(x,y,20))
print(normalize(x))

sns.histplot(x)
plt.show()
sns.histplot(normalize(x))
plt.show()