strs = ["eat","tea","tan","ate","nat","bat"]
hash_list = dict()

for i in strs:
    sortedChars = "".join(sorted(i))
    if sortedChars not in hash_list:
        hash_list[sortedChars] = [i]
    else:
        hash_list[sortedChars].append(i)
result = []
for i in hash_list:
    result.append(hash_list[i])
print(result)
