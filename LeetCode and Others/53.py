def maximumSubarray(arr):
    maxSum = arr[0]
    prev = maxSum
    for i in range(1, len(arr)):
        res = max(arr[i] + prev, arr[i])
        maxSum = max(res, maxSum)
        prev = res
        
    return maxSum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maximumSubarray(nums))