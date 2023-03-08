import os

path = r"C:\Users\Andrey\Desktop\MyProjects\python\Lab6\Directories-and-files\test.txt"

temp = open(path, "r")
counter = 0
for i in temp:
    if(i != "\n"):
        counter += 1
print("The amount of lines in this file: ", counter)