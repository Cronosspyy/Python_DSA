# brute force 
nums = [1,2,3,4,5,6,7]
k = 3
for _ in range(0,k):
    e = nums.pop()
    nums.insert(0,e)

print(nums)

#extreme brute force

nums = [1,2,3,4,5,6,7]
n = len(nums)
k = 7
rotation = k%n
for _ in range(0,rotation):
    e = nums.pop()
    nums.insert(0,e)

print(nums)

#better
nums = [1,2,3,4,5,6,7]
n = len(nums)
k = 3
nums[:] = nums[n-k:] + nums[:n-k]

#optimal 
