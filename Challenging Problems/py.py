matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

# find the longest river
# chance = [(i-1, j), (i, j-1), (i, j + 1), (i + 1, j)]
# count = {}
# for i in range(len(matrix)):
#    for j in range(len(matrix[0])):
#        chance = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
#        if matrix[i][j] == 1:
#            count[i] = 1
#            for a, b in chance:
#                if matrix[a][b] == 1:
#                    count[i] += 1




