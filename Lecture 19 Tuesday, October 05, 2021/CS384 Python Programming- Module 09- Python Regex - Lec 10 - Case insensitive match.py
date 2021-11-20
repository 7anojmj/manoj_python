
import re
import os
os.system('cls')
# os.system('clear')

# Case insensitive match
# By default, the matching of patterns is case sensitive. By passing the re.IGNORECASE to the compile function, we can make it case insensitive.


words = ('dog', 'Dog', 'DOG', 'Doggy')

# pattern = re.compile(r'dog')
pattern = re.compile(r'dog', re.I)

for word in words:
    if re.match(pattern, word):
        print(f'{word} matches')
    else:
        print(f'{word} Does NOT match')
