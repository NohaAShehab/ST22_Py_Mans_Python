# info = {"name":"test", "email":"test@gmail.com"}
#
#
# # info.clear()  # empty dictionary
#
# # del info
#
# # del info["name"]
# info.clear("name")
# modules

"""
any python file is considered to be a module
"""
# "1- get part of the module"
# from validationModule import checkInt
#
# # is_int = checkInt('iti')
# # is_int = checkInt(77.7)
#
# "2- import the module"
# import validationModule
# # name=validationModule.askforalpha("please enter name : ")
# # print(name)
#
# from validationModule import pi
#
# print(pi)
# pi = 5
#
# print(pi)
# from validationModule import pi
# print(pi)

#exception


# file handling


### import part of the module

# from iti.greeting import sayHello
#
# sayHello("Ahmed")

# ########### import the module

# import iti.greeting
# iti.greeting.sayHello("Ahmed")


# ########## alias the module
# import iti.greeting as greet
#
# greet.sayHello("Ahmed")

# import tensforflow as tf

#######################################################
# import helper
#
#
# helper.test()

# from helper import  test
#
# test()

# from helper.InputsModule import askforInt
#
# n = askforInt("please enter day ")

# from helper import askforInt
import helper

age = helper.askforInt("please enter age : ")








