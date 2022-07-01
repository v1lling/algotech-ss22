from icecream import ic
def partition(a):
    b = []
    c = []
    for zahl in a:
        if abs(zahl + sum(b) - sum(c)) < abs(zahl + sum(c) - sum(b)):
            b.append(zahl)
        else:
            c.append(zahl)
    ic(b)
    ic(sum(b))
    ic(c)
    ic(sum(c))

def same(array):

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

        x = max(array)
        array.remove(max(array))
        if (sum1+x <= mid):
            list1.append(x)
            sum1 += x
        else:
            list2.append(x)
            sum2 += x

    return list1, list2

def same2(array):

    total = 0

    for x in array:
        total += x

    if (total%2 == 1):
        return 

    sum1= 0
    sum2 = 0
    list1=[]
    list2 = []
    m = total/2

    for p in array:
        if (sum1+p <= m):
            list1.append(p)
            sum1 += p
        else:
            list2.append(p)
            sum2 += p 

    return list1, list2



w = [3,2,2,3,2]
p = [3,2,2,3,2]

print(same(w))
print(same2(p))

partition(p)