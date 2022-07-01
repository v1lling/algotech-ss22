from icecream import ic
import math

# ist das rekursiv?? ne

def f(x):
    ic(x)
    return math.e ** x ** 2

def trapez(a, b, n):
    h = (b-a)/n
    sum = (f(a)+f(b))/2.
    for i in range(1,n):
        sum = sum + f(a + h*i)
    return sum*h
    
ic(
    trapez(0, 1, 4)
)