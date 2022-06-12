arr = [2324,3245,4567,4567,3234,4,1234,23415,4645,67546,7,543,32456,342,3245,6,423567]

for i in range(len(arr)):
    minIndex = 0
    minValue = arr[len(arr) - 1]
    for j in range(i, len(arr)):
        if arr[j] <= minValue:
            minIndex = j
            minValue = arr[j]
    arr[i], arr[minIndex] = arr[minIndex], arr[i]

print(arr)