import re

message = input()
result = re.findall(r"ab{2,3}", message)
print(result)