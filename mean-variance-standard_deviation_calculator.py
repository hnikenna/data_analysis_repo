import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    c = np.array(list)
    y = c.reshape((3, 3))

    calculations = {'mean': [np.mean(y, axis=0).tolist(), np.mean(y, axis=1).tolist(), np.mean(y)],
                    'variance': [np.var(y, axis=0).tolist(), np.var(y, axis=1).tolist(), np.var(y)],
                    'standard deviation': [np.std(y, axis=0).tolist(), np.std(y, axis=1).tolist(), np.std(y)],
                    'max': [np.max(y, axis=0).tolist(), np.max(y, axis=1).tolist(), np.max(y)],
                    'min': [np.min(y, axis=0).tolist(), np.min(y, axis=1).tolist(), np.min(y)],
                    'sum': [np.sum(y, axis=0).tolist(), np.sum(y, axis=1).tolist(), np.sum(y)]
                    }
    return calculations


print(calculate([0,1,2,3,4,5,6,7,8]))
