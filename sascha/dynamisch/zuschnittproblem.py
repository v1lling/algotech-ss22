from icecream import ic

n = 4 # Baumstammlänge
x = [0,2,3,8,9] # Erlöse Länge 0, 1, 2, 3, 4
G = [0,0,0,0,0] # maximale Erlös 

def G(i):
    if i == 0: return 0

    times = int(n/i) # Wie oft passt Länge i in n?
    rest = n % i # Gibt es einen Rest?

    erloes = times * x[i] + x[rest] # Erloes

    return max(G(i-1), erloes) # Rekursion

ic(G(n))


