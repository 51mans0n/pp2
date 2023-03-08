import os

path = r"C:\Users\Andrey\Desktop\MyProjects\python\Lab6\Builtin-function-of-python\Exercise 1.py"

if os.access(path, os.F_OK):
    print("Your path exists")
    directory , filename = os.path.split(path)
    print("The directory of the file: ", directory)
    print("The name of the file: ", filename)
else:
    print("Your path doesn't exist")