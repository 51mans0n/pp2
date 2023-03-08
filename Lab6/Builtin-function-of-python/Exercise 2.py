MyString = str(input())

count_lower = 0
count_upper = 0

for i in range(0, len(MyString)):
    if MyString[i].islower():
        count_lower += 1
    if MyString[i].isupper():
        count_upper += 1
        
print("Count of lower case letters:", count_lower)
print("Count of upper case letters:", count_upper)