# # #lEARN ABOUT VARIABLE SCOPE
# # # def function1(n):
# # #     print(n,"Hey I have printed function1 argument n")
# # #
# # # function1("There is another argument in function1 which will be concatinate with the above given argument")
# #
# # l=20 #Global Variable/global scope here you can use this variable anywhere in your whole program
# # def function1(n):
# #     l=4 #Local Variable only used for this function1() you can't use Local variable outside
# #     m=9
# #     # print(l)
# #     print(l,m)
# # function1("This is Your Local Variable")
# #Note:
# #When you dont have any Local variable in your function the program will first check it out where your local variable si defined. if it is not present the  the program will check the Global variable and execute
# #You can't change Global variable . python will not give you permission to change Global variable. For this purpose we use global keyword to varry or change the given value  of global variable
# # l=20 #Global Variable/global scope here you can use this variable anywhere in your whole program
# # def function1(n):
# #     # l=4 #Local Variable only used for this function1() you can't use Local variable outside
# #     m=9
# #     global l #Here I use global variable to varry/change value of global variable
# #     l=l+2
# #     # print(l)
# #     print(l,m)
# # function1("This is Your Local Variable")
# def Tasbeeha():
#     x=4
#     def harry():
#         global x
#         x=99
#         print("Before calling harry()",x)
#         harry()
#         print("after calling Harry",x)
# Tasbeeha()
#
#
#
#
#
#     # print(n,"Hey I have printed function1 argument n")
# # print(l)

#_____________________________________________________________________________________________________________________________________
# # 22-Aug-2022 to 21-Sep-2022
# #Final Taking Course

#Scope, Global Variables and Global Keyword

#Global Variable define globally at the top of the program
#
# m=55 #Global Variable
# def funct1(x):
#     # m=59 #Local Variable you cannot print local variables outside the program
#     #If you want to change Global Variable python will not allow you to change Global Variable for This purpose we use Global Keyword.
#     global m
#     m=m+2
#     print(x,"I Have Printed.",m, "Here m is defined as a Global Variable")
# funct1("Heeey! This is me")
# print(m)

#Nested Functions: A Function in a Function is called Nested Functions.

# #Here we create a one function name's Hamza()
# def Hamza():
#     #In this function we create one Local variable x=44
#     x=44
#     def Saad(): #Here we create an other Function
#         global x  #we create here a Global variable x=77 note that we have no Global Variable x above
#         x=77
#     print("Before Calling Saad() the value od 'x' is",x) #It will give you 'Before Calling Saad() the value od 'x' is 44'
#     Saad() #Saad is only run in Harry() Function because Saad() is Harry's Property
#     print("After Calling Saad() the value od 'x' is",x) #'After Calling Saad() the value od 'x' is 44'
# Hamza()


#Quiz
#What will be the Output
#Here we create a one function name's Hamza()

x=88
def Hamza():
    #In this function we create one Local variable x=44
    x=44
    def Saad(): #Here we create an other Function
        global x  #we create here a Global variable x=77 note that we have no Global Variable x above
        x=77
    # print("Before Calling Saad() the value od 'x' is",x) #It will give you 'Before Calling Saad() the value od 'x' is 44'
    Saad() #Saad is only run in Harry() Function because Saad() is Harry's Property
    print("After Calling Saad() the value od 'x' is",x) #'After Calling Saad() the value od 'x' is 44'
Hamza()
print(x)



