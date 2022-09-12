

def printharr(string):
    return f"Ye string Harry ko dedo Thakkurrrrr{string}"

def add(num1,num2):
    return num1+num2*8

print("And the name is:",__name__) #Whenever you ran a function with the same file the value of the __name__ will be:main
if __name__ == '__main__':

    print(printharr(" Harry"))

    a=add(4,9)
    print(a)
#If you wanna use the same functions in another file and you don't wanna copy paste so you will have be able to import these functions
#There is a big flex while you are importing function from different files this will excecute the whole content/functions in the same file which you obviously don't wanna execute
#For this pupose you have to make "main" function
# if __name__ == '__main__':