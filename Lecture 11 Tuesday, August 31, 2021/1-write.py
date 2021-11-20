# A simple example - Python write file
###
file_handle = open("sample_log.txt", "w")

file_handle.write("Hello Everyone!\n")
file_handle.write("\tIt is     my first attempt to write to a file in Python.")
file_handle.write("I'll first open the file and then write.")
file_handle.write("Finally, I'll close it.")

file_handle.close()
