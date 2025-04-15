def inc(x):
    return x+1
def add(x,y):
    for i in range(y):
        x=inc(x)
    return x
def mult(x,y):
    intx = x
    temp = 0
    for i in range(y):
        temp = add(temp,intx )
    return temp
def exp(x,y):
    intx = x
    temp = 1
    for i in range(y):
        temp = mult(temp,intx )
    return temp

print(exp(2,4))
#GG!
