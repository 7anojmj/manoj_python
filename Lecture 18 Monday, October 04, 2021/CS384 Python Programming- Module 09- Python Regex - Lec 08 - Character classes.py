
import re
import os
os.system('cls')
# os.system('clear')

# Character classes
# A character class defines a set of characters,
# any one of which can occur in an input string for a match to succeed.


words = ('a gray bird', 'grey hair', 'great look')

pattern = re.compile(r'gr[ea]y')

for word in words:

    if re.search(pattern, word):
        print(f'{word} matches')
    else:
        print(f'The {word} does not match')


# compile() creates regular expression character class [a-e],
# which is equivalent to [abcde].
# class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'.
p = re.compile('[a-e]')

# findall() searches for the Regular Expression and return a list upon finding
print(p.findall("Aye, said Mr. Gibenson Stark"))
