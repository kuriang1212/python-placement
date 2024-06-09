#factorial
num=int(input(""))
factorial=1
if num<0:
  print("-ve input")
elif num==0:
  print("The factorial of o is 1")
else:
  for i in range (1,num + 1):
    factorial*=i
  print("The factorial of",num,"is",factorial)