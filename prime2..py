# Python program to display all the prime numbers within an interval and also the count

lower = int(input("Enter the lower intreval: "))
upper = int(input("Enter the upper intreval: "))

print("Prime numbers between", lower, "and", upper, "are:")
count=0
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           count+=1
print("count=",count)