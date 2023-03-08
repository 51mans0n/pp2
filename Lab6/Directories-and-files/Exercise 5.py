import os

path = r"C:\Users\Andrey\Desktop\MyProjects\python\Lab6\Directories-and-files\test.txt"

Mylist = ["Hello there!", "I'm Maxim.", "KBTU FIT 1st course!"]
temp = open(path, "w")
print("I'll write this list to your file:")
print(Mylist, "\n")

for i in Mylist:
    temp.write(str(i) + " ")
temp.close()

print("The result:")
temp = open(path, "r")
print(temp.read())