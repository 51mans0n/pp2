import re

message = input()
result = re.findall(r"ab{0,}", message)
print(result)