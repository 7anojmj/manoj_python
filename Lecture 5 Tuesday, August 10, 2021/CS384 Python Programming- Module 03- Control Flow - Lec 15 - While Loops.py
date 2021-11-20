import os
os.system("cls")  # For Windows
# os.system("clear")  # For Linux & MAC


count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1
print("Good bye!")

var = 10
# Second Example
while var > 0:
    print('Current variable value :', var)
    var = var - 1
    if var == 5:
        break
print("Good bye!")

while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('Current variable value :', var)
print("Good bye!")


# Using else Statement with Loops
# Python supports having an else statement associated with a loop statement.
#  If the else statement is used with a for loop, the else statement is executed when
# the loop has exhausted iterating the list.
#  If the else statement is used with a while loop, the else statement is executed
# when the condition becomes false.
# The following example illustrates the combination of an else statement with a while
# statement that prints a number as long as it is less than 5, otherwise the else statement
# gets executed.
#!/usr/bin/python3
count = 0
while count < 5:
    print(count, " is less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")
