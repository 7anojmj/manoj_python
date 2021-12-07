import re

import os
os.system('cls')
# os.system('clear')


# The fullmatch function looks an exact match.


words = ('seven', 'even', '1even', 'prevent', "evens",
         'revenge', 'maven', 'eleven', 'amen', 'event')

pattern = re.compile(r'even')

for word in words:
    if re.match(pattern, word):
        print(f'The {word} matches')

    if re.search(pattern, word):
        print(f'The {word} search')

    if re.fullmatch(pattern, word):
        print(f'The {word} Full matches')

    print("*"*25)
