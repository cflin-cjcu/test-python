n=int(input())
a=1
# print(1,end=' ')
b=1
# print(1,end=' ')
i=3
while i <= n:
    a,b=b,a+b
    i += 1
print(b, end=' ')