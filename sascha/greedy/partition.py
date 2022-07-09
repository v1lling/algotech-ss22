from icecream import ic
def partition(a):
    b = []
    c = []
    for zahl in a:
        if abs(zahl + sum(b) - sum(c)) < abs(zahl + sum(c) - sum(b)):
            b.append(zahl)
        else:
            c.append(zahl)
    return b,c

def partition2(a):
    b = []
    c = []
    for zahl in a:
        if abs(zahl + sum(b) < sum(c)):
            b.append(zahl)
        else:
            c.append(zahl)
    return b,c

def partition3(array):
    sum1= 0
    sum2 = 0
    list1=[]
    list2 = []
    total = 0
    for x in array:
        total+= x

    if (total%2 == 1):
        return "is not working"

    mid = total/2

    while(len(array) > 0):
        x = array[0]
        array.remove(x)
        if (sum1+x <= mid):
            list1.append(x)
            sum1 += x
        else:
            list2.append(x)
            sum2 += x

    return list1, list2


w = [1,1,1,4,5]
p = w.copy()
q = w.copy()
print(w)
print(partition(w))
print(partition2(p))
print(partition3(q))
print()
w = [2,3,2,1,2]
p = [2,3,2,1,2]
q = [2,3,2,1,2]
print(w)
print(partition(w))
print(partition2(p))
print(partition3(q))