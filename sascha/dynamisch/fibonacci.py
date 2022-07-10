import numpy as np
def fib(n):
    zahlen = []
    zahlen = np.zeros(n+1)
    zahlen[0] = 0
    zahlen[1] = 1
    for i in range(2, n+1):
        zahlen[i] = zahlen[i-1] + zahlen[i-2]
    return zahlen

print(fib(1))
print(fib(14))
