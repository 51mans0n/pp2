def generator():
    yield from [x for x in range(0, value) if x % 12 == 0]
value = int(input())
for i in generator():
    print(i)