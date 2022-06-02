# First solution comes to the mind
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# Using help of an array
def fibb(n):
    arr = [0] * (n+1)
    return memo(n, arr)
def memo(n, arr):
    if (n == 0) or (n == 1):
        return n
    if arr[n] == 0:
        arr[n] = memo(n-1, arr) + memo(n-2, arr)
    return arr[n]
print(fibb(1))