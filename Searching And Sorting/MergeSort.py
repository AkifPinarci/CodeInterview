arr = [2324,3245,4567,457,3234,4,1234,23415,4645,67546,7,543,32456,342,3245,6,423567]

def mergeSort(arr):
    if len(arr) > 1:
        left = arr[:len(arr) // 2]
        right = arr[len(arr) // 2:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        t = 0
        while( l < len(left) and r < len(right)):
            if left[l] < right[r]:
                arr[t] = left[l]
                l += 1
            else:
                arr[t] = right[r]
                r += 1
            t += 1
        while( l < len(left)):
            arr[t] = left[l]
            t+=1
            l+=1
        while(r < len(right)):
            arr[t] = right[r]
            t+=1
            r+=1

mergeSort(arr)
print(arr)