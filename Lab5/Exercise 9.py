import re

message = input()
result = re.findall("[A-Z][a-z]*", message)
print(' '.join(result))