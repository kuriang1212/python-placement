#fib series
n=int(input())
fib1=0
fib2=1
print(fib1,fib2,end=" ")
for i in range(2,n):
  fib3=fib1+fib2
  print(fib3,end=" ")
  fib1=fib2
  fib2=fib3