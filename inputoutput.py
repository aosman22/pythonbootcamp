with open('myfile.txt', 'r') as my_new_file: 
     print(my_new_file.read()) 

# open() function makes sure the file is opened safely without affecting other programs.
# A variable called my_new_file is assigned to the contents of the text file. 

# READING, WRITING, APPENDING MODES
# mode='r' is read only.
# mode='w' is write only (will overwrite files or create new!).
# mode='a' is append only (will add on to file).
# mode='r+' is reading and writing.
# mode='w+' is reading and writing (Overwrites existing files or creates a new file.)

with open('myfile.txt', 'a') as my_new_file: 
    my_new_file.write('A NEW IS ADDED TO THE FILE.')
    my_new_file.close()

with open('myfile2.txt', 'w+') as my_new_file: 
    my_new_file.write('A NEW IS ADDED TO THE FILE.')
    my_new_file.close()