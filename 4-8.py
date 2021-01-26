n=int(input())
sum =0
for i in range(1,n+1):
    prod = 1
    for j in range(1,i+1):
        prod *= j
    sum += prod    
print(sum)    