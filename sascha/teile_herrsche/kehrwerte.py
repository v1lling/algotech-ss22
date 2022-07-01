from icecream import ic
import math

def pow(y, n):
   # if (y == 0): return 1 # may not be correct mathematically if y == 0 but 0 is not possible per definition
    if (n == 1): return y
    result = pow(y, int(n/2)) * pow(y, int(n/2))
    if n % 2:
        result = result * y
    return result

def my_invpot(y, n):
    return 1/pow(y, n)

def invpot(y, n):
   # if y == 0: return 1
    if n == 1: return 1/y
    r = invpot(y, int(n/2)) * invpot(y, int(n/2))
    if (n % 2):
        r = r * y
    return 1/r

def invpot2(y, n):
   # if y == 0: return 1
    if n == 1: return 1/y

    r = invpot2(y, int(n/2)) * invpot2(y, int(n/2))
    if n % 2:
        r = r * 1/y
    return r

y = 20
n = 5

#r = 1/pow(y, n)
#print(r)
#print('{:f}'.format(r))
#
#r = invpot(y, n)
#print(r)
#print('{:f}'.format(r))


r = invpot2(y, n)
print(r)
print('{:f}'.format(r))

#r = my_invpot(y, n)
#print(r)
#print('{:f}'.format(r))
#
r = 1/math.pow(y, n)
print(r)
print('{:f}'.format(r))