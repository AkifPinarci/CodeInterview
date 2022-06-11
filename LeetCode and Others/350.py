
nums1 = [2,1]
nums2 = [1,1]
if len(nums1) > len(nums2):
    long = nums1
    short = nums2
else:
    long = nums2
    short = nums1
result = list()
track = 0
while long[track] != short[0]:
    track += 1
add = 0
print(track)
while long[track] == short[add]:
    result.append(long[track])
    track+=1
    add += 1
    if add >= len(short):
        break
print(result)