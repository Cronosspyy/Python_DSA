# brute force

n = 7
nums = n 
lst =[]
for i in range(1,nums+1):
    if nums%i == 0:
        lst.append(i)
print(lst)
lst.clear()

# optimized 

n = 105
nums = n 
for i in range(1,nums+1//2):
    if nums%i == 0:
        lst.append(i)
lst.append(nums)
print(lst)
