array = [-10, -5, -1, 1, 2, 3, 5, 7, 9, 12, 13]

def search(start, end, array):
    if start > end:
        return -1
    mid = (end + start) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return search(start, mid-1, array)
    else:
        return search(mid+1, end, array)

print(search(0, len(array), array))