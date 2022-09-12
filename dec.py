# def func1():
# #     print("Subscribe now!")
# #
# # func2=func1() #Here I save func1 in func2
# # func2
#
#
# #We can return fuction through a function
# # def funcret(num):
# #     if num==0:
# #         return print
# #     if num==1:
# #         return sum
# # a=funcret(0)
# # print(1)
#
# #WE can pass a function as an argument as well
# def executor(func):
#     func("this")
#
# executor(print)
#
# #Decorators: we use decorators when we use one function to the other places
# def dec1(func1):
#     def nowexec():
#         print("Excecuting now!")
#         func1()
#         print("Excecuted")
#     return nowexec
# @dec1 #short method
# def who_is_harry():
#     print("Harry is a good boy")
# who_is_harry()
#
# # who_is_harry=dec1(who_is_harry) #Long method
# # who_is_harry()


#____________________________________________________________________________________________________________________________________
# 25-Aug-2022
#What are Decoartors in Python?

# def func1():
#     print("Subscribe  Now!")
# func2=func1()
# func2

#Here we create a program that will return two Functions
# def funcret(x):
#     if x==0:
#         return print # This will Return <built-in function print>
#     if x==1:
#         return sum # This will Return <built-in function sum>
# z=funcret(1)
# print(z)

# Note that:
# WE CAN RETURN A FUNCTION THROUGH Functions

# WE CAN ALSO GIVE A FUNCTION AS AN ARGUMENT
# def func(func2):
#     func2("this")
# func(print) # WE CAN ALSO GIVE A FUNCTION AS AN ARGUMENT


#See this Below
#here WE create a function which takes function as a argument
def dec1(func1):
    def noeexe():
        print("Excecuting Now!")
        func1()
        print("Executed")
    return noeexe()


@dec1
#Here I create an other function
def who_is_me():
    print("My name is tasbeeha")


# #Now I pass my function who_is_me to dec1() Function which takes one argument as a function
# who_is_me=dec1(who_is_me()) #pass who_is_me() to dec1()
# who_is_me()
print(dec1())
who_is_me