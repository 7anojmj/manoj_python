
import re
import os
os.system('cls')
# os.system('clear')

# The finditer function
# The finditer function returns an
# iterator yielding match objects over all non-overlapping matches for the pattern in a string.


text = 'I saw a fox in the wood. The fox had red fur.'
# I saw a fox in the wood. The fox had red fur.


pattern = re.compile(r'fox')

found = re.finditer(pattern, text)
print(found)
for item in found:

    s = item.start()
    e = item.end()
    print(f'Found {text[s:e]} at {s}:{e}')
