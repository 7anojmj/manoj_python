
import re
import os
os.system('cls')
# os.system('clear')

# Named character classes
# There are some predefined character classes.
# The \s matches a whitespace character [\t\n\t\f\v],
# the \d a digit [0-9], and the \w a word character [a-zA-Z0-9_].

text = 'India won the T_20 World Cup in 2007. Sachin has 100 centuries !. 9999999999999933333333333'

pattern = re.compile(r'\d+')  # + = 1 or more

found = re.findall(pattern, text)

if found:
    print(found)
    print(f'There are {len(found)} numbers')

pattern = re.compile(r'\w')

found = re.findall(pattern, text)

if found:
    print(found)
    print(f'There are {len(found)} words')
