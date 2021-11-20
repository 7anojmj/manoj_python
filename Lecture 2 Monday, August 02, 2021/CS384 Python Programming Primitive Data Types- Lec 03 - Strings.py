word = 'Joker'
sentence = "India is my country !."
paragraph = '''This is a paragraph. It is
made up of multiple lines and sentences.
This is CS384 Ptyhon Class'''


paragraph2 = """This is a paragraph. It is
made up of multiple lines and sentences.
This is CS384 Ptyhon Class"""


print(word)

print(sentence)

print(paragraph)

str = 'Hello-World!'
# HelloAWorld!
# 0123456789
print(str)  # Prints complete string
print(str[0])
# Prints first character of the string
print(str[2:5])  # 2:4  #2:(5-1)
# # Prints characters starting from 3rd to 5th
print(str[2:])
# # HelloAWorld!
# # 0123456789
print(str[:4])

# # Prints string starting from 3rd character
# print('#' * 30)
# # Prints string two times
# print(str + " " + "India" + "is my country")  # Prints concatenated string
# # Input on string
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
print("Your full name is ", first_name + " " + last_name)
