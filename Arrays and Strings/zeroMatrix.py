rows = list()
columns = list()
array = [[0, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
def pa(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end=' ')
        print()
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == 0:
            rows.append(i)
            columns.append(j)

for i in rows:
    for j in range(len(array[i])):
        array[i][j] = 0

for i in columns:
    for j in range(len(array)):
        array[j][i] = 0

pa(array)