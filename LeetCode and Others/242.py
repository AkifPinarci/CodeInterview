def validAnagram(s, t):
    if len(s) != len(t):
        return False
    if s == t:
        return False
    hash_list = dict()
    for i in range(len(s)):
        if s[i] not in hash_list:
            hash_list[s[i]] = 1
        else:
            hash_list[s[i]] += 1

        if t[i] not in hash_list:
            hash_list[t[i]] = -1
        else:
            hash_list[t[i]] -= 1
    print(hash_list)
    for i in hash_list:
        if hash_list[i] != 0:
            return False
    return True

validAnagram("anagram","nagaram")