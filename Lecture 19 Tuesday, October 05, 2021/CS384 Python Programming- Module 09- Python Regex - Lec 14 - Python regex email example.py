
import re
import os
os.system('cls')
# os.system('clear')

# Python regex email example
# In the following example, we create
# a regex pattern for checking email addresses.


emails = ("luke@gmail.com", "andy@yahoocom",
          "34234sdfa#2345", "f344@gmail.comIITPAtna", '1801me02@iitp.ac.in')

pattern = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,18}$')

for email in emails:

    if re.match(pattern, email):
        print(f'{email} matches')
    else:
        print(f'{email} does not match')
