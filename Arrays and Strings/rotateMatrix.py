array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
def pa(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end=' ')
        print()
pa(array)
left, right = 0, len(array)-1
while left < right:
    top, bottom = left, right
    for i in range(right-left):
        
        temp = array[top][left+i]
        array[top][left+i] = array[bottom-i][left]
        array[bottom-i][left] = array[bottom][right-i]
        array[bottom][right-i] = array[top+i][right]
        array[top+i][right] = temp

    left += 1
    right -= 1


pa(array)