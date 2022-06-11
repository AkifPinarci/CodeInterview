def checkVertical(arr):
    for i in range(len(arr)):
        check = set()
        for j in range(len(arr[i])):
            if arr[j][i] in check:
                return False
            if arr[j][i] != ".":
                check.add(arr[j][i])
    return True

def checkHorizontal(arr):
    for i in range(len(arr)):
        check = set()
        for j in range(len(arr[i])):
            if arr[i][j] in check:
                return False
            if arr[i][j] != ".":
                check.add(arr[i][j])
    return True 

def check9(arr, i, j):
    check = set()
    for row in range(3):
        for col in range(3):  
            if arr[i+row][j+col] in check:
                return False
            if arr[i+row][j+col] != ".":
                check.add(arr[i+row][j+col])
    return True

def checkBox(arr):
    for i in range(0,len(arr),3):
        for j in range(0, len(arr), 3):
            if not check9(arr, i, j):
                return False
    return True
                
      
board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]


print(checkBox(board))
print(checkHorizontal(board))
print(checkVertical(board))

print(False and True and False)