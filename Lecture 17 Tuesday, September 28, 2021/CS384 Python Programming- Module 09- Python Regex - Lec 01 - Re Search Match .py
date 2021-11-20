import re  # Regular Expression
import os
os.system('cls')
# os.system('clear')


# match_fun.py
# The match function returns a match object
# if zero or more characters at the
# beginning of string match the regular expression pattern.
# The search function looks for the
# first location where the regular expression pattern produces a match.


words = ('seven', 'even', 'Even', '1even', 'prevent',
         'revenge', 'maven', 'eleven', 'amen', 'event')

pattern = re.compile(r'even')

for word in words:

    if re.match(pattern, word):  # Checks only Starting
        print(f'The {word} matches')
    else:
        print(f'The {word} does NOT match')

    if re.search(pattern, word):  # Check anywhere
        print(f'The {word} searches')
    else:
        print(f'The {word} does NOT search')

    print('*' * 25)
