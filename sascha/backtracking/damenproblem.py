

from re import X

def threat(pos, i, j):
    return (pos[i] == pos[j] or abs(pos[i]-pos[j]) == abs(i-j))

def damenproblem(n):
    pos = []
    x = 0
    pos.append(0)
    while len(pos) < n:
        valid = False
        j = len(pos)
        print(pos)
        while valid == False and x < n:
            
            valid = True
            pos.append(x)
            print("append " + str(x))
            for i in range(j):
                print(i)
                if threat(pos, j, i):
                    valid = False
            if not valid:
                print("not valid" + str(pos))
                x = pos.pop() + 1
        if x == n and j == 0:
            print("oh shit")
            break
        if valid == True:
            x = 0
        else:
            x = pos.pop() + 1
    return pos


print(damenproblem(3))