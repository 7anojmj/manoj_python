
years = [['January', 'February', 'March'], ['April', 'May', 'June'], [
    'July', 'August', 'September'], ['October', 'November', 'December']]

for x in years:
    print(x)
    # for sublist in x:
    #     print(sublist)

nested_tuple = (('blue', 'green'), ('red', 'black'), ('blue', 'white'))
for inner in nested_tuple:
    for value in inner:
        print(value)


D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

for id, info in D.items():
    print(id, "#", info)
    print("\nEmployee ID:", id)
    for key in info:
        print(key + ':', info[key])
