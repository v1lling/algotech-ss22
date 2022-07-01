from icecream import ic

def summe(list):
    if len(list) == 0: return 0
    if len(list) == 1: return list[0]
    m = int(len(list)/2)
    ic(list[:m])
    ic(list[m:])
    li = summe(list[:m])
    re = summe(list[m:])
    return li + re


list = [3,2,-4,-6,3,-10,1,-2,16,-14]
ic(
    summe(list)
)
