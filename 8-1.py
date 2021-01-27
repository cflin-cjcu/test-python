row, col = [ int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(row)]
mul = int(input())
for i in range(row):
    for j in range(col):
        a[i][j] *= mul
for row in a:
    print(*row)