import os

print("There are all your folders in this path: ")
for i in os.listdir(r"C:\Users\Andrey\Desktop\MyProjects\python"):
    if os.path.isdir(os.path.join(r"C:\Users\Andrey\Desktop\MyProjects\python", i)):
        print(i)
print("\nThere are all files in this path: ")
for i in os.listdir(r"C:\Users\Andrey\Desktop\MyProjects\python"):
    if os.path.isfile(os.path.join(r"C:\Users\Andrey\Desktop\MyProjects\python", i)):
        print(i)
print("\nThere are all files and folders: ")
for i in os.listdir(r"C:\Users\Andrey\Desktop\MyProjects\python"):
    print(i)