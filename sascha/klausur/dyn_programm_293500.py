from icecream import ic
import numpy as np

def dyn(n):
    D = np.zeros(n)
    D[0] = 4

    for i in range(0,n):
        ic(i)
        D[i] = 0
        for i in range(1,n):
            D[i] += 1/n * (D[i] + 1 + D[i-1] + D[n-i])
    return D

ic(
    dyn(1),
    dyn(3),
    dyn(5),
    dyn(16)
)
