import numpy as np
from icecream import ic

def dyn(N):
    C = []
    C = np.zeros(N+1)
    C[0] = 1
    for i in range(0, N):
        sum = 0
        for k in range(0, i+1):
            sum = sum + (C[k] * C[i-k])
        C[i+1] =sum
    return C

def dyn_new(N):
    C = []
    C = np.zeros(N+1)
    C[0] = 1
    for i in range(1, N+1):
        sum = 0
        for k in range(0, i+1):
            sum = sum + (C[k] * C[i-1-k])
        C[i] =sum
    return C

print(dyn(10))
print(dyn_new(10))


def catalan(N):
    C = []
    C = np.zeros(N+1)
    C[0] = 1

    for i in range(0,N): 
        for k in range(0,i+1):
            C[i+1] = C[i+1] + (C[k] * C[i-k])
    return C

print(catalan(10))