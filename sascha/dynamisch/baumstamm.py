import numpy as np
from icecream import ic
# G[0] = 0
# G[n] = x[n]
# G[1] = 8
# 
# G[k] = max(G[k-1] | n/k * x[k])

# am 0-1-Rucksack Problem orientiert!

n = 5
x = [0,2,3,8,9,0]
def zuschnitt():
    G = np.zeros((n+1, n+1))
    for i in range(0, n+1):
        G[i][0] = 0 # Basisfall
        ic(i)
        for k in range(0, n+1):
            if (i==0):
                G[i][k] = 0
            else:
                rest = i - k
                ic(rest)
                if rest < 0:
                    G[i][k] = G[i][k-1]
                else:
                    G[i][k] = max(G[i][k-1], x[k] + G[rest][k])
    return G
ic(
    zuschnitt()
)    

#       k 0 -> n
#  i 0  [0 0 0 0 0 0 0]
#  0 1  [0 2 2 2 2 2 2
#  | 2  [0 4 4 4 4 4 4
#  v 3  [0 6                max(6,3+2)            
#  n 4
#    5
#
#
