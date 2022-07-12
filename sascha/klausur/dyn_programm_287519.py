import numpy

def dyn(n):

    B = []
    B = numpy.zeros(n+1)
    B[0] = 2

    for k in range(1,n+1):

        sum = 0
        for i in range(1, k+1):
            sum = sum + B[i-1] + B[k-i]
        B[k] = (k + (1/(k+1))) * sum 

    return B


print(dyn(5))