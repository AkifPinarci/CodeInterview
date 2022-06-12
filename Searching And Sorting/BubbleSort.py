arr = [2324,3245,4567,4567,3234,4,1234,23415,4645,67546,7,543,32456,342,3245,6,423567]

for i in range(1, len(arr)):
    for j in range(len(arr) - i):
        if arr[j] >= arr[j+1]:
            arr[j], arr[j+1] = arr[j + 1], arr[j]
print(arr)