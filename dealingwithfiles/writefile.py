"""

    open file mode ---> w ---> interpreter check if the file exists ---> remove its content
    and open the file starting from the begining of the file

    ---> if the file not exists ---> interpreter will try to create

"""


"""write to the file  """

# try:
#     fileobj = open("mycv.txt", 'w')
# except Exception as e:
#     print(e)
# else:
#     print(fileobj)  # object---> TextIOWrapper
#     fileobj.write("------###########################\n")
#     fileobj.write("Nice to meet you\n")
#     fileobj.write("Nice to meet you\n")
#     fileobj.close()



# try:
#     fileobj = open("mycv.txt", 'w')
# except Exception as e:
#     print(e)
# else:
#     print(fileobj)  # object---> TextIOWrapper
#     fileobj.writelines(["Ahmed\n", "Ali\n", "Mohamed\n"])
#     fileobj.close()