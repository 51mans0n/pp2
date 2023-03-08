import os

path = r"C:\Users\Andrey\Desktop\MyProjects\python\Lab6"

for i in range(65, 90):
    name = os.path.join(path, chr(i) + ".txt")
    temp = open(name, "a")
for i in os.listdir(path):
    print(i)