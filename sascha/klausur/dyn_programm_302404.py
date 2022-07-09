import numpy as np
from icecream import ic
def rec(n):
    D = []
    D = np.zeros(n+1)

    # basisfall
    D[0] = 4

    for k in range(1, n+1):
        ic(k)
        sum = 0

        for i in range(1,k+1):
            sum = sum + (1 + D[i-1] + D[k-i])
            ic(sum)

        D[k] =  1/k * sum
        ic(D[k])
    
    return D
        
print(rec(5))
