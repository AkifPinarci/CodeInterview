arr = [1,2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 21, 22, 23,122,234, 244, 300, 311, 322, 345, 5678, 89645, 90000, 945464, 4564563, 99999999]
def binarySearchIterative(arr, val):
    begin  = 0
    end = len(arr) - 1

    while(begin < end):
        mid = begin + (end - begin) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            end = mid - 1
        else:
            begin = mid + 1
        
    return -1


def binarySearchRecursive(arr,val):
    begin = 0
    end = len(arr) - 1
    def bsr(arr, begin, end, val):
        if len(arr) == 0 or begin > end:
            return -1
        mid = begin + (end - begin) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            return bsr(arr, begin, mid - 1, val)
        else:
            return bsr(arr, mid + 1, end, val)
    return bsr(arr, begin, end, val)

print(binarySearchIterative(arr, 345))
print(binarySearchRecursive(arr, 516))