from scipy.optimize import minimize
import numpy as np


def rosen(para):
    x1, x2, x3 = para
    return 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2 + 100 * (
            x3 - x2 ** 2) ** 2 + (1 - x2) ** 2


def rosen_der(para):
    der = np.zeros_like(para)
    x1, x2, x3 = para
    der[0] = -400 * x1 * (x2 - x1 ** 2) - 2 * (1 - x1)
    der[1] = 200 * (x2 - x1 ** 2) - 400 * x2 * (x3 - x2 ** 2) - 2 * (1 - x2)
    der[2] = 200 * (x3 - x2 ** 2)
    return der


# number of experiments
n = 100

currMin = 10 ** 10
solution = None

# Run optimization algo using different starting points
for i in range(n):
    a = np.random.uniform(-100, 100, size=(3, 1))
    res = minimize(rosen, x0=a, method='BFGS', jac=rosen_der)
    if rosen(res.x) < currMin and res.success:
        currMin = rosen(res.x)
        solution = res.x

print(solution)
