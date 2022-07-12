from statistics import median
from icecream import ic
import math

# NOT WORKING YET
# KOMPLIZIERT

def median_of_medians(A, left, right):
    if right - left <= 5:
        ic("sorting")
        B = A[left: right]
        B.sort()
        ic(B)
        if len(B) % 2:
            m = math.floor(len(B) / 2)
        else:
            m = int(len(B) / 2)
        ic(m)
        return B[m]

    medians_tbd = []
    i = 0
    ic(A)
    while i+5 < len(A):
        medians_tbd.append(i)
        i = i + 5
    medians_tbd.append(i)
        
    medians = []
    for m in medians_tbd:
        new_m = median_of_medians(A, m, m+5)
        ic(new_m)
        medians.append(new_m)

    return median_of_medians(medians, 0, len(medians))

list = [100,3,9,11,1,12,5]
list2 = [10,1,67,20,56,8,43,90,54,34,0]

ic(
    median_of_medians(list2, 0, len(list2))

)