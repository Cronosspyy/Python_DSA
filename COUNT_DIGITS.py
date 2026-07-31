n= 8687898
nums = n 
count = 0
while (nums>0):
    count+=1
    nums = nums//10

print("totals digits are :",count)



# or 


from math import * 
def count_digits(num):
    return int(log10(num)+1)

print(count_digits(n))