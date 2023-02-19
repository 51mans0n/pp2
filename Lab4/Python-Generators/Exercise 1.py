def generator():
    yield from [x ** 2 for x in range(value) if x ** 2 < value]
value = int(input())
for i in generator():
    print(i)