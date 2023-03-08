import os

path = r"C:\Users\Andrey\Desktop\MyProjects\python\Lab6"

path1 = os.access(path, os.F_OK)
if(path1 == True):
    print("Your file exist")
else:
    print("Your file doesn't exist") 

path2 = os.access(path, os.R_OK)
if(path2 == True):
    print("I can read your file")
else:
    print("I can't read your file")

path3 = os.access(path, os.W_OK)
if(path3 == True):
    print("I can work with your file")
else:
    print("I can't work with your file")

path4 = os.access(path, os.X_OK)
if(path4 == True):
    print("I can execute your file")
else:
    print("I can't execute your file")
                                      