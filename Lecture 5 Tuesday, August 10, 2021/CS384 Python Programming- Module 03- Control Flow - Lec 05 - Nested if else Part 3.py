import os
os.system("cls")  # For Windows
# os.system("clear")  # For Linux & MAC

#####################
amount = 20000  # int(input("Enter amount: "))
if amount < 1000:
    discount = amount*0.05
    print("Discount", discount)
elif amount < 5000:
    discount = amount*0.10
    print("Discount", discount)
elif amount < 10000:
    discount = amount*0.15
    print("Discount", discount)
else:
    discount = amount*0.20
    print("Discount", discount)

print("Net payable:", amount-discount)

#####################

num = int(input("enter number"))

if num % 2 == 0:
    if num % 3 == 0:
        print("Divisible by 3 and 2")
    else:
        print("divisible by 2 not divisible by 3")
else:
    if num % 3 == 0:
        print("divisible by 3 not divisible by 2")
    else:
        print("not Divisible by 2 not divisible by 3")
