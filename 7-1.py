a=[int(i) for i in input().split()]
#7-1
# print(*a[::2])
#7-2
# for i in a:
#     if i%2==0:
#         print(i,end=' ')
#7-3
for i in range(1,len(a)):
    if a[i-1] < a[i]:
        print(a[i],end=' ')        