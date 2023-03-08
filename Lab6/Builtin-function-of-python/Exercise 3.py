MyString1 = str(input())
MyString2 = ""

list = list(MyString1)
reversed_list = reversed(list)

for i in reversed_list:
    MyString2 += i
if(MyString1 == MyString2):
    print("This string is palindrome")
else:
    print("This string isn't palindrome")