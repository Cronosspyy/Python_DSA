n = 1634
nums = n
result = 0 
k = len(str(nums))
while(nums>0):
    ld = nums % 10 
    result = result + ld**k
    nums = nums //10

print(result)