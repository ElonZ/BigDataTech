from scipy.optimize import minimize
import numpy as np


def rosen(x):
    return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2 + 100 * (
            x[2] - x[1] ** 2) ** 2 + (1 - x[1]) ** 2


# number of experiments
n = 100

currMin = 10 ** 10
solution = None

# Run optimization algo using different starting points
for i in range(n):
    a = np.random.uniform(-100, 100, size=(3, 1))
    res = minimize(rosen, x0=a, method='BFGS')

    if rosen(res.x) < currMin:
        currMin = rosen(res.x)
        solution = res.x

print(solution)
