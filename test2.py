s = "Hello world!"

dict = {}
for i in s:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for x, y in dict.items():
    print(x, y)