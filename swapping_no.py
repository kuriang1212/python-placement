#swapping no 
def swap_num(a,b):
  print("Before swapping:")
  print("a=",a)
  print("b=",b)
  temp=a
  a=b
  b=temp
  print("after swapping")
  print("a=",a)
  print("b=",b)
  num1=int(input())
  num2=int(input())
  num1,num2=swap_num(num1,num2)