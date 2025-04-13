# # File Basic opening and reading of file in python 
# # 1. READING OPERATIONS
# file=open("demo_file_for_FileHandling.txt","r")
# data=file.read() # if we give read(n) => starting ke 'n' character hi read karega
# data=file.readline() # Reads one line only from file
# print(data)
# print(type(data))
# file.close() # Closing a file is a good practice otherwise someone else might access your file data

# # file=open("demo_file_for_FileHandling.txt","rb") # For opening binary files in reading mode, 'b' is added. 't' for text mode is by default hence needn't mention "rt"
# # "r+" means reading and writing mode both 
# # "w+" means writing and reading mode both 

# # 2. WRITING OPERATIONS
# # fileWriteMode=open("demo_file_for_FileHandling.txt","w")
# # fileWriteMode.write("New line added now 1st attempt using 'w' mode") # This will overwrite the file, old data lost
# fileWriteMode=open("demo_file_for_FileHandling.txt","a")

# fileWriteMode.write("\nNew line added now 1st attempt using 'a' mode") # This will append at the file end
# fileWriteMode.close()
# ----------------------------------------------------------------------------------------------------------
# # WITH SYntax in file handling
with open("demo_file_for_FileHandling.txt","r") as f:
    data=f.read()
    print(data) # No need to close the file, it will be closed automatically when we are using WITH syntax

# ----------------------------------------------------------------------------------------------------------
# DeLETING a File

import os; # for deletion we will use os.remove(fileName)
# os.remove("demo_file_for_FileHandling.txt")