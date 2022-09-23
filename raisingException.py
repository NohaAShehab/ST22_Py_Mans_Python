from helper.InputsModule import askforInt
def divnums():
    num1 = askforInt("please enter num1: ")
    num2= askforInt("please enter num2 : ")
    if num2=='0':
        raise Exception("We cannot divide by zero ----- please restart the application")
    num1 = int(num1)
    num2 = int(num2)
    res  = num1/num2
    print(f"res = {res}")
    return res

d= divnums()
print("===================================")