name = "waterbottle"
name2 = "erbottlewat"

for i in range(len(name)):
    if(name[i:len(name)]+name[0:i]) == name2:
        print(True)
