#pali
def is_pali(num):
  str_num=str(num)
  rev_num=str_num[::-1]
  return str_num==rev_num
num=int(input())
if(is_pali(num)):
  print("true")
else:
  print("false")