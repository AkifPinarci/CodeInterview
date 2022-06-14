arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
def binarySearch(arr, begin, end , val):
    mid = begin + (end - begin) // 2
    if arr[mid] == val:
        return mid
    if begin > end:
        return -1
    
    if arr[mid] < arr[begin]:
        if val <= arr[end] and arr[mid] < val:
            return binarySearch(arr, mid + 1, end, val)
        else:
            return binarySearch(arr, begin, mid - 1, val)
    else:
        if val >= arr[begin] and val < arr[mid]:
            return binarySearch(arr, begin, mid - 1, val)
        else:
            return binarySearch(arr, mid + 1, end, val)
index = binarySearch(arr,0, len(arr) - 1, 25)
print(index)