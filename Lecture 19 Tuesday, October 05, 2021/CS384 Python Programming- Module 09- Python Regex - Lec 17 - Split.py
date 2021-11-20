
import re
import os
os.system('cls')
# os.system('clear')


print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM'))
On |th Jan |, at |:| AM
# 'Boy' and 'boy' will be treated same when flags = re.IGNORECASE
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))
