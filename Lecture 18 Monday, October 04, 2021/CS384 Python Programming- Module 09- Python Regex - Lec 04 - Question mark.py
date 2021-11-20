
import re
import os
os.system('cls')
# os.system('clear')

# Question mark meta character
# The question mark (?) meta character is a
# quantifier that matches the previous element zero or one time.


words = ('seven', 'even', '1even', 'prevent', 'revenge',
         'maven',  'eleven', 'amen', 'event')

pattern = re.compile(r'.?even')
# pattern1 = re.compile(r'even')
# pattern2 = re.compile(r'.even')


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
