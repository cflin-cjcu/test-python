s=input()
print(s[:s.find('h')]+s[s.rfind('h'):s.find('h'):-1]+s[s.rfind('h'):])
