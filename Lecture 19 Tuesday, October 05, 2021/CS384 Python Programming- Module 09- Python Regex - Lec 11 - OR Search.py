
import re
import os
os.system('cls')
# os.system('clear')

# The alternation operator | creates a regular expression with several choices.


words = ("Eiffel Tower", "Leaning Tower of Pisa", "Taj Mahal",
         "Sydney Opera House", "Pyramid of Giza", "Statue of Liberty")

pattern = re.compile(r'Eiffel|Taj|Pyramid|House|Pisa')

for word in words:

    if re.search(pattern, word):
        print(f'{word}  matches :)')
    else:
        print(f'{word} Does NOT match')
