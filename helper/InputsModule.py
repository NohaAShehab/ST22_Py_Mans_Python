

def askforInt(message):
    numm = input(message)
    if numm.isdigit():
        return numm

    print("============ invalid number ============")
    return askforInt(message)