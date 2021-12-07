# Open the file "foo.txt" and append content to the file:

f = open("foo.txt", "a")
f.write("\n\n-----\nNow the file has more content!")
f.close()
