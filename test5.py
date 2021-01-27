n = 3
m = 4
a = [[0] * m for i in range(n)]
print(a)
a[0][0] = 5
for row in a:
    print(*row)