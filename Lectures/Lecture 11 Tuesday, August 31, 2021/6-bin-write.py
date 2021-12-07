f = open("binfile.bin", "wb")
num = [5, 10, 15, 20, 25]
arr = bytearray(num)
# https://www.programiz.com/python-programming/methods/built-in/bytearray
print(arr)
f.write(arr)
f.close()
