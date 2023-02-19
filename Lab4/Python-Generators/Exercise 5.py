def generator():
    yield from [value for value in range(value, -1, -1)]
value = int(input())
for i in generator():
    print(i)