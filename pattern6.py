#patter6.py
n=int(input())
for i in range(0,n):
  for j in range(0,n):
    if (j<=i):
      print(i+1,end=" ")
  print()