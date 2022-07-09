from icecream import ic

def mergesort(data_to_sort):
    if len(data_to_sort) > 1:
        mid = len(data_to_sort) // 2
        leftarray = data_to_sort[:mid]
        rightarray = data_to_sort[mid:]

        mergesort(leftarray)
        mergesort(rightarray)

        i, j, k = 0, 0, 0

        while i < len(leftarray) and j < len(rightarray):
            if leftarray[i] < rightarray[j]:
                data_to_sort[k] = leftarray[i]
                i += 1
            else:
                data_to_sort[k] = rightarray[j]
                j += 1
            k += 1

        while i < len(leftarray):
            data_to_sort[k] = leftarray[i]
            i += 1
            k += 1

        while j < len(rightarray):
            data_to_sort[k] = rightarray[j]
            j += 1
            k += 1 

list = [1, 5, 3, 8, 2] # paare: 5-3 | 5-2, 3-2, 8-2
ic(
    mergesort(list),
    list
)