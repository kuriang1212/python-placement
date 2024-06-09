#armstrong no:
num=int(input("enter a no: "))
leng=len(str(num))
sum=0
temp=num
while(temp!=0):
  digit=temp%10
  sum+=digit**leng
  temp//=10
if sum==num:
  print(num," is a asrmstrong no: ")
else:
  print(num,"its not an armstrong no:")