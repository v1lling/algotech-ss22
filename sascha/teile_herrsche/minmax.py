
from icecream import ic
def max(a):
    max = a[0]
    for zahl in a:
        if zahl > max:
            max = zahl
    return max

def maxrec(a, li, re):
    ic(a,li,re)
    #base case
    if li==re: return a[li]
    
    m = int((re+li)/2)
    ic(m)
    left = maxrec(a, li, m)
    right = maxrec(a, m+1, re)

    if left>right:
        return left
    else:
        return right


a = [123, 124, 125, 126, 125, 124, 3]
ic(max(a))
ic(maxrec(a, 0, len(a) -1 ))