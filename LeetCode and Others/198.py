k = 3
nums = [1,2,3,4,5,6,7]
print(nums[7-k:]+nums[:7-k])
for i in range(k):
    nums.insert(0,nums.pop(-1))
print(nums)