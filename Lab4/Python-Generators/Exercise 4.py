def generator():
    yield from [x ** 2 for x in range(value)]
value = int(input())
for i in generator():
    print(i)