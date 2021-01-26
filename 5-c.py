s=input()
d=''
for i in range(len(s)):
    if i%3!=0:
        d += s[i]
print(d)        