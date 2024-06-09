#strong no:
num=int(input("Enetr the number:"))
temp=num
sum=0;
while(num):
  i=1
  f=1
  r=num%10
  while(i<=r):
    f=f*i
    i=i+1
  sum+=f
  num=num//10
if(sum==temp):
  print("The no:  is a strong no:")
else:
  print("THe no: ia not a strong no:")