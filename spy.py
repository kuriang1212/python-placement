#spy no
num=int(input("Enter the no:"))
sum=0
prod=1
while(num!=0):
  digit=num%10
  sum+=digit
  prod*=digit
  num//=10
if (prod==sum):
  print("spy no:")
else:
  print("not spy no:")