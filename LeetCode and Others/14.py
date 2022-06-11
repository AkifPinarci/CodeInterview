
def helper(check, arrStr):
    for i in range(len(check)):
        if check[i] != arrStr[i]:
            return check[:i]
    return check
            
strs = ["flower","flow","flight"]

lenMin = len(strs[0])
minStr = helper(str(min(len(strs[0]), len(strs[1]))), str(max(len(strs[0]), len(strs[1]))))
for i in strs:
    if len(i) < lenMin:
        lenMin = len(i)
        minStr = i
for i in strs:
    minStr = helper(minStr, i)
    if len(minStr) == 0:
        print("0")
    
print(minStr)
            