
import re
import os
os.system('cls')
# os.system('clear')


mystring = "956 456 218 854"

print("\d Matches:", len(re.findall("\d", mystring)))
print("[0-9] Matches:", len(re.findall("[0-9]", mystring)))


# As you can see from the above output, d matches the integers present in the string.
# However if we replace it with D, it will match everything BUT an integer, the exact opposite of d.

mystring = "956 456 218 854A"

print(" \\D Matches:", len(re.findall("\D", mystring)))
print(" [^0-9] Matches:", len(re.findall("[^0-9]", mystring)))
print(" ^[0-9] Matches:", len(re.findall("^[0-9]", mystring)))
