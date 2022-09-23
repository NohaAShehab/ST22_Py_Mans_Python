
"""

    append =--> 'a' open the file for appending 000, starting from the end of the file

    if the file not exists ----> will try to create it
"""

try:
    fileobj = open("my.txt", 'a')
except Exception as e:
    print(e)
else:
    print(fileobj)  # object---> TextIOWrapper
    fileobj.writelines(["2\n", "test\n"])
    fileobj.write("My name is noha \n")
    fileobj.close()