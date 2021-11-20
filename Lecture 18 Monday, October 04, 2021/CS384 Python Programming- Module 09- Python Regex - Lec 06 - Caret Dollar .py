
import re
import os
os.system('cls')
# os.system('clear')

# When using the ^ anchor the match must occur at the
# beginning of the string and when using the $ anchor
# the match must occur at the end of the string.


sentences = ('I am looking for Jane',
             'Jane was walking along the river.',
             'Kate and Jane are close friends.',
             'Jane')


pattern = re.compile(r'Jane')

for sentence in sentences:

    if re.search(pattern, sentence):
        print(sentence)

print('#' * 25)


pattern = re.compile(r'^Jane')

for sentence in sentences:

    if re.search(pattern, sentence):
        print(sentence)

print('#' * 25)

pattern = re.compile(r'Jane$')
for sentence in sentences:

    if re.search(pattern, sentence):
        print(sentence)


pattern = re.compile(r'^Jane$')
for sentence in sentences:

    if re.search(pattern, sentence):
        print(sentence)
