
array = [1, 2, 3, 4, 5]
def sub(arr):
    result = [[]]
    for i in arr:
        for sub in result:
            result = result + [list(sub) + [i]]
    return result
print(sub(array))