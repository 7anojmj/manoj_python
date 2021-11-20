import os
os.system("cls")
# os.system("clear")

numerator = 10
denominator = 0  # 0, '0'


try:
    print("An apple a day keeps the doctor away !")
    division = numerator/denominator  # error
    # Since above line is error, ignore all try lines
    print("Hi There")
    print(division)
except:  # Exception
    print("There was some error in try clause")


multiplication = numerator*denominator
print(multiplication)
print("Have A Good Day!")
