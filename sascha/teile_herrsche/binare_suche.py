from icecream import ic

list = [1, 4, 6, 45, 432, 5344, 54345]

def bin_search(li, re, x):
    m = int((li + re) / 2)
    if list[m] == x:
        return m
    elif list[m] < x:
        return bin_search(m, re, x) 
    else:
        return bin_search(li, m, x)

index = bin_search(0, len(list), 5344)
ic(index)

index = bin_search(0, len(list), 4)
ic(index)

index = bin_search(0, len(list), 6)
ic(index)