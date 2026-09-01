nums = [-1,-33,-4,-67,-89,-90,-23]
largest = nums[0]
for n in range(len(nums)):
    if nums[n]> largest:
        largest = nums[n]
print(largest)