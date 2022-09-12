#Recursions in Python: Function in a Function/ Nested Function

def print2(str1):
    # print("This is me" + str1)
    print2(str1)
    return "This is me" + str1


v=print2(" Irtizayy!")
print(v)


