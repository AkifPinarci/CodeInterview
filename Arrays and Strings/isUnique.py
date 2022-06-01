name = "mehnarci"
h_list = dict()

for i in name:
    if i in h_list:
        h_list[i] += 1
    else:
        h_list[i] = 1

for i in h_list:
    if h_list[i] > 1:
        print("Duplicate!")
