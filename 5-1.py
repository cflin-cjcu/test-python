# You are given a string.
s= input()
# In the first line, print the third character of this string.
print(s[2])
# In the second line, print the second to last character of this string.
print(s[-2])
# In the third line, print the first five characters of this string.
print(s[:5])
# In the fourth line, print all but the last two characters of this string.
print(s[:-2])
# In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).
print(s[::2])
# In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).
print(s[1::2])
# In the seventh line, print all the characters of the string in reverse order.
print(s[::-1])
# In the eighth line, print every second character of the string in reverse order, starting from the last one.
print(s[::-2])
# In the ninth line, print the length of the given string.
print(len(s))
