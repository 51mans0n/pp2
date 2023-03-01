import re

message = input()
result = re.findall(r"[a-z]+_[a-z]+", message)
print(result)