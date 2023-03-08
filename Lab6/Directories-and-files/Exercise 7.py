import os

path1 = r"C:\Users\Andrey\Desktop\MyProjects\python\Lab6\Directories-and-files\test.txt"
path2 = r"C:\Users\Andrey\Desktop\MyProjects\python\Lab6\Directories-and-files\second_test.txt"

temp1 = open(path1, "r")
temp2 = open(path2, "w")

for i in temp1:
    temp2.write(str(i))
temp1.close()
temp2.close()

temp2 = open(path2, "r")
for i in temp2:
    print(i)