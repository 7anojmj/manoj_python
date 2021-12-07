import os
os.system("cls")
f = open("foo.txt", "r")
print(f.read())
# Return the 5 first characters of the file:

# f = open("foo.txt", "r")
# print(f.read(5))  # number of characters

# Read one line of the file:

# f = open("foo.txt", "r")
# print(f.readline())
# exit()

# Read two lines of the file:

# f = open("foo.txt", "r")
# print(f.readline().strip())
# print(f.readline().strip())
# exit()
# Read two lines of the file:

# f = open("foo.txt", "r")
# print(f.readlines(5))  # Returns as a list
# # all_lines = f.readlines()
# # print(type(all_lines))
# # for x in all_lines:
# #     print("Line Read is ", x)
# exit()

# f = open("foo.txt", "r")
# for x in f:
#     print(x.strip())
# exit()

# Close the file when you are finish with it:

f = open("foo.txt", "r")
print(f.readline())
f.close()


with open("foo.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
