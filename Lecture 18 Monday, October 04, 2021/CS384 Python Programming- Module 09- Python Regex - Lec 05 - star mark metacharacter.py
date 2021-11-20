
import re
import os
os.system('cls')
# os.system('clear')

# star mark meta character
# The star     mark (*) meta character is a
# quantifier that matches the previous element zero or more time.
# Question mark meta character
# The question mark (?) meta character is a
# quantifier that matches the previous element zero or
# one time.

words = ('ssssssssssssssssssssssssssssssssssssssssssssssseven', 'even', '7even', 'prevent', 'revenge', 'maven',
         'eleven', 'amen', 'event')

pattern = re.compile(r'.*even')  # 0 to infinity


for word in words:

    if re.match(pattern, word):
        print(f'The {word} matches')
    else:
        print(f'The {word} does NOT match')

    if re.search(pattern, word):
        print(f'The {word} searches')
    else:
        print(f'The {word} does NOT search')

    print('*' * 25)


# # '*' replaces the no. of occurrence of a character.
# Greedy
# p = re.compile('ab*')
# print(p.findall("ababbaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbba"))
