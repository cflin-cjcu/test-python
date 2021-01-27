a=[int(i) for i in input().split()]
max(a)
# print( len(set(a)) )
b=[]
count=0
for i in a:
    if i not in b:
        b.append(i)
        count += 1
print(count)        
print(b)