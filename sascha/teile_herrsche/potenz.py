from icecream import ic 

def pow(y, n):
    if (y == 0): return 1
    if (n == 1): return y

    y2 = pow(y, int(n/2))
    result = y2 * y2
    if n % 2:
        result = result * y
    return result

# r = invpot(2, 3)
r = pow(24, 12)

print(r)