"""

    string  ---> sequence of chars ====> set of chars

"""
#
# "1- to define a string"
# course = 'python'
# "2- empty string is falsy value"
# s= ""
# if s:
#     print("---- found")
# else:
#     print("not found ")
#
# "3- get no of chars in the strings "
# print(len(course))
#
# "4-  count no of occurance for a character "
# o = 'odoo'
# print(o.count("o"))
#
# "5-string chars can be accessed using index ---> start from 0 "
# print(course[2])
# "6- get the index of the char in the string "
# print(o.index("d"))
#
# "7- string concatenation"
# fname = 'noha'
# lname = 'shehab'
# fullname = fname + lname
#
# "8- interpolation"
# fname = 'noha '
# mid= "Abdelhady "
# lname = 'shehab '
# # fullname = fname + mid + mid  +lname
# fullname = fname + mid *2  +lname
# print(fullname)
#
# "9- replace"
# message = 'I love Python '
# print(message.replace("o", "@"))
#
#
# "10-  string format "
# # template = "My name is {0} I works at {1}"
# # print(template.format("noha", "iti"))
# # print(template.format("Amira", "Microsoft"))
# # print(template.format("Valeo", "Ali"))
#
# template = "My name is {username} I works at {workname} since {year}"
# print(template.format(workname="Valeo",username="Ali", year=2014))
#
# "11- f-format string"
# name = 'noha'
# track = 'open source'
# message = f"my name is {name} I graduated from {track}."
# print(message)
#
# "12-get input from the user "
# myname = input("-------- please enter your name ------ ")
# print(myname, type(myname))  # ## input always returns with string
#
# "13- check the type of the value in the string "
# "=--> number "
# if myname.isdigit():  ## isnumeric
#     print("---- value in the string is numeric ")
# " ===> Alpha "
# if myname.isalpha():
#     print("the string consists from characters only .... ")
#
# if myname.isspace():
#     print(" the input string consists from spaces only         ")
#
# if myname.islower():
#     print("string in lower cases")
#
# if myname.isupper():
#     print("string in upper cases")
#
# "14- capatilize the string "
# print(myname.capitalize())
# print(myname.upper())
# print(myname.lower())
#
# """ 15- strip string """
#
# # message = "                My name is Noha                           "
# # print(message,len(message))
# # # print(message.strip())  # remove spaces from both sides
# # print(message.lstrip())  # remove spaces from left sides
# # print(message.rstrip())  # remove spaces from left sides
#
#
# message = "                My name is @@ Noha            @"
# print(message,len(message))
# print(message.strip("@ "))  # remove spaces from both sides
# print(message.lstrip("@ "))  # remove spaces from both sides
# print(message.rstrip("@ "))  # remove spaces from both sides
#
#
#
# num = 10.8
# print(round(num))

a,b,c = 5,6,7
print(min(a,b,c))
print(max(a,b,c))

############################# type conversions
# num = 2022
#
# num = str(num)
#
#
# v = False
# v = str(v)
################################333

msg = "44"
msg = int(msg)

course =input("please enter value ")
if course.isdigit():
    course = int(course)




