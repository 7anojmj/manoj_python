import glob
import os
os.system('cls')
# os.system('clear')


print(glob.glob(r"D:\programs\mix\*.py"))
# exit()
x = glob.glob(r"D:\programs\mix\*.py")

for i in x:
    print(i)
