import re

message = input()
result = re.findall("[A-Z][^A-Z]*", message)
print(result)