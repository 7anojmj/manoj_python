# A simple example - Python write file
###
file_handle = open("sample_log_2.txt", "w")

file_handle.writelines(["Hello Everyone!", "It is my first attempt to write to a file in Python.",
                       "I'll first open the file and then write.", "Finally, I'll close it."])
file_handle.close()
