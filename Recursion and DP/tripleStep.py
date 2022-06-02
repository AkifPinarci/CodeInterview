def steps(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return steps(n - 1) + steps(n - 2) + steps(n - 3)

def step(n):
    arr = [-1] * (n + 1)
    return memo(n, arr)

def memo(n, arr):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif arr[n] > -1:
        return arr[n]
    else:
        arr[n] = memo(n - 1, arr) + memo(n - 2, arr) + memo(n - 3, arr)
        return arr[n]
print(steps(84))