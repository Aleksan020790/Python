mat = [[' '] * 7 for _ in range(7)]
for i in range(7):
    for j in range(7):
        if (i > j and i > 7 - 1 - j) or (i < j and i < 7 - 1 - j):
            mat[i][j] = '*'
for i in mat:   print(*i)
