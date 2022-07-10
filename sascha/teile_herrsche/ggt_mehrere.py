from icecream import ic

# gleich wie ggt
# nur immer restliche liste anhängen (alle außer x, y)
# wenn es nur noch 2 zahlen sind und r==0 -->
#   letzter Rest das Ergebnis

def ggt(list):
    x = list[0]
    y = list[1]
    r = x % y
    if r == 0 and len(list) == 2:
        return y
    if r == 0:
        return ggt([y] + list[2:])            
    else:
        return ggt([y] + [r] + list[2:])

ic(
    ggt([247, 589]),
    ggt([2, 8, 16, 20]),
    ggt([123,456,789]),
    ggt([984, 1002, 382])
)