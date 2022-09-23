# print("-------------- welcome to validation module --------------")

def checkInt(num):
    if isinstance(num, int) or isinstance(num, float):
        return True


pi = 3.14
#
# def askforalpha(message):
#     while True:
#         inputstring = input(message)
#         if inputstring.isalpha():
#             return inputstring



def askforalpha(message):

    inputstring = input(message)
    if inputstring.isalpha():
        return inputstring

    return askforalpha(message)