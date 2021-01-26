s=input()
a=s.find('p')
if a==-1:
    print(-2)
else:    
    print(s.find('p',a+1))