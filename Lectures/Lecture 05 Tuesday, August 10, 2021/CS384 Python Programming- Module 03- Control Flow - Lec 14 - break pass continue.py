import os
os.system("cls")  # For Windows
#os.system("clear")  # For Linux & MAC


for letter in 'Python':
    # First Example
    if letter == 'h':
        continue
    print('Current Letter :', letter)
var = 10

# break
print('*'*25)
for letter in 'Python':
    if letter == 'h':
        break
        print('This is pass block')
    print('Current Letter :', letter)
print("Good bye!")


# Pass

print('*'*25)
for letter in 'Python':
    if letter == 'h':
        pass
        print('This is pass block')
    print('Current Letter :', letter)
print("Good bye!")
