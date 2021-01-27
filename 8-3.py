n=int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j]= (n+i-j)%n
for row in a:
    print(*row)