def generator():
    yield from [x for x in range(value) if x % 2 == 0 and x < value]
value = int(input())
for i in generator():
    print(i, "", sep=",", end="")