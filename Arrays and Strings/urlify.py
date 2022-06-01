name = "  Mr John Smith    "
trueLen = 13
replace = "%20"
count = 0
result = ""
while count < len(name):
    if(name[count] != " "):
        name = name[count:]
        break
    count += 1
count = 0
print(name)
for i in name:
    if i != " ":
        result += i
    else:
        result += replace
    count += 1
    if(count == trueLen):
        break

print(result)