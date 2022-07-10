import numpy as np
from icecream import ic
# G[0] = 0
# G[n] = x[n]
# G[1] = 8
# 
# G[k] = max(G[k-1] | n/k * x[k])

# IST DAS RICHTIG?
# IDK!
n = 4
x = [0,2,3,8,9]
def zuschnitt():
    G = []
    G = np.zeros(n+1)
    G[0] = 0 # Basisfall
    for i in range(1, n+1):
        times = int(n/i)
        rest = n % i
        G[i] = max(G[i-1], times*x[i] + x[rest] ) # Rekursionsformel
    return G
ic(
    zuschnitt()
)    