import re

message = input()
result = re.findall(r"a.+b$", message)
print(result)