from icecream import ic

# 
# x = zahl1
# y = zahl2
# Rechne Rest = zahl1 % zahl2
# rekursiv wieder aufruf:
#   zahl2 und Rest
# Solange bis Rest ==0, dann war letzter Rest das Ergebnis:

def ggt(x, y):
    r = x % y
    ic(r)
    if r == 0:
        return y
    else:
        return ggt(y, r)


ic(
    ggt(589, 247),
    ggt(43423, 86846)
)