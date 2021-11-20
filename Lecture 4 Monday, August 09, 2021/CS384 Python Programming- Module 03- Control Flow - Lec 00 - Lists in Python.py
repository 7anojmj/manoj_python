import os
os.system("cls")

my_list = ['k', 2, 3.55, "CS384", 5.1]
print(my_list)

print(my_list[0])
print(my_list[2])


print("The length of the list is: {}".format(len(my_list)))
my_list[2] = "IITP"
print("After modification")
print(my_list)
print(my_list[2])

list1 = ['physics', 'chemistry', 1997, 2000]


list3 = ["a", "b", "c", "d"]

print(list1)

print(list3)

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])


list = ['physics', 'chemistry', 1997, 2000]
print("Value available at index 2 : ", list[2])
list[2] = 2001
print("New value available at index 2 : ", list[2])

list1, list2 = ['C++', 'Java109', 'Python'], [456, 700, 200]
print("Max value element : ", max(list1))
print("Max value element : ", max(list2))

print("Min value element : ", min(list1))
print("Min value element : ", min(list2))
