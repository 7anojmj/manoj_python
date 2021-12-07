import os
os.system("cls")
# CSV -- Comma Separated Values
with open('country.csv', 'r') as f:
    results = []
    for line in f:
        print("Line Read is: ", line)
        words = line.split(',')
        print(words, type(words))
        # results.append((words[0], words[1:]))
    print(results)
