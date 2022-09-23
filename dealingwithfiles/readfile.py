"""

    simple text files ----> json

    ---> files
        ---> read
        ---> write  ---> write to the file starting from the beginning of the file ((remove old content))
        ---> append ---> append to the file starting from the end of the file ((keep old content))


    ===> open file and decide the mode (r, w, a)
            open("filename", mode) ---> r , w , a

    ===> do the operation
        --> read   --> read file content
        --> write  ---> add content the file

    ===> close file
        close
"""

# """ Read file  into one string  """
#
# try:
#     fileobj = open("names.txt", 'r')
# except Exception as e:
#     print(e)
# else:
#     print(fileobj)  # object---> TextIOWrapper
#     data  = fileobj.read() # read the file content into a string
#     print(data)
#
#     fileobj.close()



#
# """ Read file  line by line """
#
# try:
#     fileobj = open("names.txt", 'r')
# except Exception as e:
#     print(e)
# else:
#     print(fileobj)  # object---> TextIOWrapper
#     data  = fileobj.readline() # read the file content into a string
#     print(data)
#
#     fileobj.close()


""" Read file  into lines  """

try:
    fileobj = open("names.txt", 'r')
except Exception as e:
    print(e)
else:
    print(fileobj)  # object---> TextIOWrapper
    data  = fileobj.readlines() # read the file content into a list
    print(data)

    fileobj.close()