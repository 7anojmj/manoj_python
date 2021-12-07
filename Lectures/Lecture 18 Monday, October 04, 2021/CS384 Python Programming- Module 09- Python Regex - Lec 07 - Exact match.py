
import re
import os
os.system('cls')
# os.system('clear')

# Exact match
# An exact match can be performed with the
# fullmatch function or by placing the term between the anchors: ^ and $.


words = ('book', 'bookworm', 'Bible',
         'bookish', 'cookbook', 'bookstore', 'pocketbook')

pattern = re.compile(r'^book$')

for word in words:

    if re.search(pattern, word):
        print(f'The {word} matches')
    else:
        print(f'The {word} does not match')
