import re

message = input()
result = re.findall(r"[A-Z][a-z]", message)
print(result)