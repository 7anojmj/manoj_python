import os
os.system("cls")  # For Windows
# os.system("clear")  # For Linux & MAC

# Single Statement Suites
# Similar to the if statement syntax, if your while clause consists only of a single statement,
# it may be placed on the same line as the while header.
# Here is the syntax and example of a one-line while clause-
# #!/usr/bin/python3
flag = 1
# while (flag):
#     print('Given flag is really true!')
# print("Good bye!")

# The Infinite Loop
# A loop becomes infinite loop if a condition never becomes FALSE. You must be cautious
# when using while loops because of the possibility that this condition never resolves to a
# FALSE value. This results in a loop that never ends. Such a loop is called an infinite loop.
# An infinite loop might be useful in client/server programming where the server needs to
# run continuously so that client programs can communicate with it as and when required.
# #!/usr/bin/python3
var = 1
while var == 1:
    # This constructs an infinite loop
    num = int(input("Enter a number:"))
    print("You entered: ", num)
print("Good bye!")
