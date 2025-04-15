import functools

@functools.cache
def fibo(x):
    if x <= 1:
        return x
    if x > 1:
        return fibo(x-1)+fibo(x-2)
    
print(fibo(100))
    