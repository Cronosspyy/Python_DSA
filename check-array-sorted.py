#nums = [3,5,6,8,9,10,20]  #true
nums1 = [1,2,4,3,5,6,7,89,0]  #false

n = len(nums1)
for i in range(0,n-1):
    if nums1[i]>nums1[i+1]:
        print("False")
print("true")

