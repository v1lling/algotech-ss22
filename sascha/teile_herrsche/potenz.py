from icecream import ic 

def pow(y, n):
    if (y == 0): return 1
    if (n == 1): return y

    y2 = pow(y, int(n/2))
    result = y2 * y2
    if n % 2:
        result = result * y
    return result

def pow2(y, n):
    if n == 1: return y
    if n % 2:
        return pow2(y, int(n/2)) * pow2(y, int(n/2)) * y
    else:
        return pow2(y, int(n/2)) * pow2(y, int(n/2))
# r = invpot(2, 3)
r = pow(24, 12)
r2 = pow2(24, 12)
print(r)
print(r2)