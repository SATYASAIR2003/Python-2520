# file=open("file.txt","r")
# print(file)

# Reading the data in file
# we use "r" module

with open("file.txt","r") as new_file:
    print(new_file.readlines())

with open("file.txt","r") as new_file:
    for char in new_file.read():
        print(char)

with open("file.txt","r") as new_file:
    for word in new_file.read().split():
        print(word)

# Writing in a file
# we "w" module
with open("write.txt","w") as write:
    print(write)
    write.writelines(["Hi Manoj\n","How are you"])

file_name="sai"
import os
# os.rmdir(file_name)
# print("file deleted")

import shutil
shutil.rmtree(file_name)
print("file deleted")