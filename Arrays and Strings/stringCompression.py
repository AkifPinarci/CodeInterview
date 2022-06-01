name = "aabcccccccccaaaacaa"
result = ""
track = 1
count = 1
length = 0
while track < len(name):
    if(name[track] == name[track-1]):
        count += 1
    else:
        length += len(str(count))+1
        count = 1
    track += 1
length += len(str(count))+1


count = 1
track = 1
if(length > len(name)):
    print(name)
else:
    while track < len(name):
        if(name[track] == name[track-1]):
            count += 1
        else:
            print("here")
            result += name[track-1]
            result += str(count)
            count = 1
        track += 1
    result += name[track-1]+str(count)
    print(result)
