#odd_char_extract
s=input()
a=""
for i in range(0,len(s)):
  if i%2==0:
    a+=s[i]
print(a)