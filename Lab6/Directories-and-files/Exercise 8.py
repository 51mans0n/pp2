import os

path = r"C:\Users\Andrey\Desktop\MyProjects\python\Lab6\Directories-and-files\file_for_delete.txt"

if(os.access(path, os.F_OK)):
    print("Your path is exists, let's delete this file")
    os.remove(path)
    print("File was deleted")
else:
    print("Your path is incorrect")