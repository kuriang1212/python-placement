#happy no:
def isHappy(n):
  sum=0
  while(n!=0):
    digit=n%10
    sum+=digit*digit
    n//=10
  return sum
n=int(input())
temp=n
while(temp!=1 and temp!=4):
  temp=isHappy(temp)

if(temp==1):
  print("true")
elif(temp==4 and temp==0):
  print("false")