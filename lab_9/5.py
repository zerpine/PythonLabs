import time
import numpy as np
from scipy.stats import multivariate_normal


def logarifm(X, m, C):
    kovar_det = np.linalg.det(C)  
    invar_kovar_det = np.linalg.inv(C)  

    X_centered = X - m

    exponent = -0.5 * np.sum(X_centered @ invar_kovar_det * X_centered, axis=1)
    normalization = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(kovar_det)

    log = exponent + normalization
    return log


N = 10
D = 7
X = np.random.randn(N, D)
m = np.random.randn(D)
C = np.random.randn(D, D)
C = np.dot(C, C.T) 

start_time = time.time()
result_custom = logarifm(X, m, C)
custom_duration = time.time() - start_time

start_time = time.time()
result_scipy = multivariate_normal(m, C).logpdf(X)
scipy_duration = time.time() - start_time

print(f"\nMy result: \n{result_custom}\n")
print(f"Scipy result:\n{result_scipy}\n")

print(f"\nMy time: {custom_duration} seconds\n")
print(f"Scipy time: {scipy_duration} seconds\n")