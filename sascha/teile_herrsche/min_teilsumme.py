import math
from icecream import ic
def min_teilsumme(arr, left, right):
    # Basisfall
    if left >= right: 
        return arr[left] 

    # Teile
    mid = int((left + right)/2)
    left_min = min_teilsumme(arr, left, mid)
    right_min = min_teilsumme(arr, mid+1, right)

    # Maximum bestimmen
    # Links
    left_sum = math.inf
    sum = 0
    i = mid
    while i >= left:
        sum = sum + arr[i]
        if sum < left_sum:
            left_sum = sum
        i = i-1

    # Rechts
    right_sum = math.inf
    j = mid+1
    sum = 0
    while j <= right:
        sum = sum + arr[j]
        if sum < right_sum:
            right_sum = sum
        j = j+1

    # Minumum Wert von
    #      Rechts oder Links oder über Mitte hinweg
    return min(right_min, left_min, right_sum + left_sum)

a = [12,1,13,-1]
b = [3,2,-4,-6,3,-10,1,-2,16,-14]
c = [-3,-12,-3,21,-21,2,-12,20,-14,3,-4,-4,-4,12,-32,32]
ic(
    min_teilsumme(a, 0, len(a) - 1),
    min_teilsumme(b, 0, len(b) - 1),
    min_teilsumme(c, 0, len(c) - 1),

)

# MasterTheorem
# a = 2
# b = 2
# alpha = log2(2) = 1
# f(n) = O(n)

# => Laufzeit T(n) = O(n log n)