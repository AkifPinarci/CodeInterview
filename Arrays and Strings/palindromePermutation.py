name  = "Tact ddffpoo3323opCoa"
name = name.lower()
h_list = dict()
for i in name:
    if i != " ":
        if i in h_list:
            h_list[i] += 1
        else:
            h_list[i] = 1
result = 0
for i in h_list:
    if h_list[i] % 2 == 1:
        result += 1
    elif h_list[i] % 2 == 0:
        pass
    else:
        result += 2
if result == 0 or result == 1:
    print(True)
else:
    print(False)