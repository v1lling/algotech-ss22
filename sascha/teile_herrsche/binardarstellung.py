from icecream import ic

def bin(zahl):
    if zahl == 0:
        return
    else:
        r = zahl % 2
        bin(int(zahl/2))
        print(r)

def bin2(zahl):
    if zahl == 1:
        return print(1)
    else:
        bin2(int(zahl/2))
    m = zahl % 2
    print(m)

bin(128)
print("--")
bin2(256)