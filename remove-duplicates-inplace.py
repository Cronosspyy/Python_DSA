nums = [1,1,1,2,3,4,4,7,9,9,9,10]
dict = {}
#brute force
n = len(nums)
for i in range(0,n):
    dict[nums[i]] = 0 
j = 0 
for k in dict:
    nums[j] = k 
    j+=1
print(j)
print(nums)
# -> tc O[n]


#optimal case(two pointer)
n = len(nums)
if n==1:
    print(1)
i = 0
j = i+1
while j<n:
    if nums[j] != nums[i]:
        i+=1
        nums[i],nums[j] = nums[j],nums[i]
    j+=1
print(i+1)

# TC -> O(n) , SC -> O(1)




