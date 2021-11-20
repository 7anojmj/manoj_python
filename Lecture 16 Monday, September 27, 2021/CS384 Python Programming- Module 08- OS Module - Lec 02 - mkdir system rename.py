
import os
os.system('cls')
# os.system('clear')

print(os.getcwd())

# os.chdir(r"d:\Songs")
# print(os.getcwd())

# print("#"*25)

# os.mkdir("Instrumental_2")


# path = r"D:\Songs\Party"
# os.mkdir(path)
# print("*"*25)

# path = r'D:\Songs\lights\camera\action'
# os.makedirs(path)
print("#"*25)
print(os.getcwd())
with open("test.txt", 'w') as file:
    pass
# os.remove("test.txt")
os.system("dir")  # ls

os.rename("test.txt", "cs384.txt")
os.system("dir")
path = r'D:\Songs\lights\camera\action'
os.rmdir(path)

os.startfile(r'C:\Users\cs102\Dropbox\CS384 2021\Firefox.txt')

currentFiles = os.system("dir")
print(currentFiles)
