import re

message = input()
print(''.join(x.capitalize() or '_' for x in message.split('_')))