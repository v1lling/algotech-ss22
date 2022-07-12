from icecream import ic
def sort(array=[12,4,5,6,7,3,1,15]):
    """Sort the array by using quicksort."""
    if len(array) == 0: return []
    if len(array) == 1: return array
    less = []
    equal = []
    greater = []

    pivot = array[0]
    for x in array:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        elif x > pivot:
            greater.append(x)

    return sort(less)+equal+sort(greater)

list = [1, 5, 3, 8, 2] # paare: 5-3 | 5-2, 3-2, 8-2
ic(
    list,
    sort(list),
)