
import re
import os
os.system('cls')
# os.system('clear')


sentence = '''
Delhi is the 
capital of 
India
'''
# Delhi is the capital of India

print(sentence)

pattern = re.compile("\n")

sentence = pattern.sub(" ", sentence)

print(sentence)
# exit()
# Regular Expression pattern 'ub' matches the string at "Subject" and "Uber".
# As the CASE has been ignored, using Flag, 'ub' should match twice with the string
# Upon matching, 'ub' is replaced by '~*' in "Subject", and in "Uber", 'Ub' is replaced.
print('Subject has Uber booked already')
print(re.sub('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))

# Consider the Case Senstivity, 'Ub' in "Uber", will not be reaplced.
print(re.sub('ub', '~*', 'Subject has Uber booked already'))

# As count has been given value 1, the maximum times replacement occurs is 1
print(re.sub('ub', '~*', 'Subject has Uber booked already',
             count=1, flags=re.IGNORECASE))

# 'r' before the patter denotes RE, \s is for start and end of a String.
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam Band', flags=re.IGNORECASE))
