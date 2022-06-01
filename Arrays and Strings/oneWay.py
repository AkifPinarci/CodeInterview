name1 = "pale"
name2 = "bake"

replace = 0
count1 = 0
count2 = 0
insert = 0

if len(name1) == len(name2):
    for i in range(len(name1)):
        if name1[i] != name2[i]:
            replace += 1
elif (len(name1)+1 == len(name2) or len(name1) == len(name2)+1):
    if len(name1) >= len(name2):
        while count2 < len(name2):
            if name1[count1] != name2[count2]:
                insert += 1
                count1 += 1
            count1 += 1
            count2 += 1
    else:
        while count1 < len(name1):
            if name1[count1] != name2[count2]:
                insert += 1
                count2 += 1
            count1 += 1
            count2 += 1
else:
    print(False)
if(insert < 2 and replace < 2):
    print(True)
else:
    print(False)
