import numpy as np
np.set_printoptions(suppress=True)

def dyn(n):
    C = []
    C = np.zeros(n+1)
    C[0] = 3

    for i in range(1, n+1):
        sum = 0
        for k in range(1,i+1):
            sum = sum + C[k-1] + C[i-k]
        C[i] = ((i + 1/i)) * sum

    return C

x = dyn(10)
print(x)