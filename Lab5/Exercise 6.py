import re

message = input()
result = re.sub("[., ]", ":", message)
print(result)