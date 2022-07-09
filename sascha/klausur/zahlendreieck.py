from icecream import ic
import numpy as np

a = [[10,0,0,0,0,0,0],
    [82,81,0,0,0,0,0],
    [4,6,10,0,0,0,0],
    [2,14,35,7,0,0,0],
    [41,3,52,26,15,0,0],
    [32,90,11,87,56,23,0],
    [54,65,89,32,71,9,31]]
s = np.zeros((7,7))

for i,zeile in enumerate(a):
    ic(zeile)
 #   s[i] = np.zeros(7)
    if i == 0: 
        s[i] = zeile
        continue
    for j,spalte in enumerate(zeile):
        if j == 0:
            s[i,j] = s[i-1][j] + a[i][j]
        else:
            if s[i-1][j] > s[i-1][j-1]:
                s[i,j] = s[i-1][j] + a[i][j]
            else:
                s[i,j] = s[i-1][j-1] + a[i][j]

ic(s)
print("Max Pfad: " + str(max(s[6])))