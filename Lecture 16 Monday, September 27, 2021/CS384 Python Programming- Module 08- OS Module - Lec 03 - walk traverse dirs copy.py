import os
os.system('cls')
# os.system('clear')


path = r'D:\programs'

for root, dirs, files in os.walk(path):
    print(root, dirs, files)
