
import os
os.system("cls")
# os.system("clear") #For mac/ubuntu
#


def biodata(**info):
    "This prints a variable passed arguments"
    print("Output is: ")
    # print(info)
    print(type(info))
    print(info["age"])
    print(info["name"])
    print(info["hobby"])


# Now you can call biodata function
biodata(name="Joker", age=44, hobby="Painting")
