a=[int(i) for i in input().split()]
count = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            count +=1
print(count)            