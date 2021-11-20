import os
os.system("cls")  # For Windows
# os.system("clear")  # For Linux & MAC

flag = 0
numbers = [11, 33, 55, 39, 55, 75, 37, 21, 23, 41, 13]
for num in numbers:
    print(num)
    break


for num in numbers:
    print(num)
    if num % 2 == 0:
        print('the list contains an even number')
        flag = 1  # Updating flag indicating presence of even number
        break

if flag == 1:
    print("The list had an even number")
else:
    print("The list did not have had an even number")

numbers = [11, 30, 55, 39, 55, 75, 37, 21, 23, 41, 13]
for num in numbers:
    print(num)
    if num % 2 == 0:
        print('the list contains an even number')
        break
    else:
        print('the list does NOT contain even number')
