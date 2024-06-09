#neon no
num=int(input("Enter the no: "))
sum=0
square=num*num

while(square!=0):
  digit=square%10
  sum+=digit
  square//=10

if(num==sum):
  print(num," is a neon no:")
else:
  print(num," is not a neon no:")
