name = "mehmetakifpinarci"
name2 = "akifpinarcimehmet"

if len(name) != len(name2):
    print("Not permutation!")
if len(set(name)) != len(set(name2)):
    print("Not permutation!")
h_list = dict()

for i in name:
    if i in h_list:
        h_list[i] += 1
    else:
        h_list[i] = 1 

for i in name2:
    if i in h_list:
        h_list[i] -= 1
    else:
        print("Not in the list")
        break

for i in h_list:
    if h_list[i] != 0:
        print("Not permutation")
        break
    else:
        print("It is a permutation")