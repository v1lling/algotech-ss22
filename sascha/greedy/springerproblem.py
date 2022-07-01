from icecream import ic
import numpy as np
def spring(n, m, x, y):
    c = np.zeros((m,n))
    c[y, x] = 1
    ok = True
    ic(c)
    while ok == True:
        gibt_neues_feld = True
        if gibt_neues_feld:
            springe_neues_feld
        else:
            ok = False
        ic(c)

    ic("Finished")
#   ---> n
# |  O O O O  
# |  O O O O
# |  O O O O 
# v  O O O O
# m

spring(5,6, 1,0)
