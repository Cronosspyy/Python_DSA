nums = [5,3,4,5,6,7,89,1,2]
n = len(nums)
temp = nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1] = nums[i]
nums[0] = temp

print(nums)

# TC -> O(n) , SC -> O(1)
