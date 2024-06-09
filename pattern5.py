#patter5.py
n=int(input())
for i in range(0,n):
  for j in range(0,n):
    if (i+j<=n-1):
      print("*",end=" ")
  print()

  '''another way #patter5.py
n=int(input())
for i in range(0,n):
  for j in range(0,n):
    if (i+j>=n):
      print(" ",end=" ")
    else:
      print("*",end=" ")
  print()'''