# """a=4
# b=4
# c=sum((a,b)) #These are called Built in Functions
# print(c)
# #User Defined Functions are defined by the user the "def" keyword is used for user defined Functions"""
# """def function1():
#     print("Here you Entered in Function 1")
#
# print(function1()) #None is here because we use print command if wanna print only ur function you can only write a function
# function1() #You can print your function a number of times
# function1()
# function1()
# function1()
# function1()
# def callF1():
#     print("Hello this is your first user define function in python")
# callF1()"""
# #Functiom can also take input
# def function2(x,y):
#     """This is the function which will calculate the average of two numbers""" #"doc string" basically a string which we write inside the function for your better understanding of your code or you can also print your function
#     # average=(x+y)/2
#     # print(average)
#     # return average #return function is used here to return the average of x & y
# #function2(5,2)
#
# # v=function2(5,2)
# # print(v)
# # #WE can print doc string
# # print(function2.__doc__)


#__________________________________________________________________________________________________________________________________
# 21-Aug-2022 to 21-Sep-2022
#Final Taking Course

#Functions
#In Python we have two categories of Functions
#1= Built In Functions
#2_ User Define Function
#User Define Functions

# def my_name():
#     print("Tasbeeha")
#     print("She is very obidient student")
#
# my_name()

#Function Can take Input as well
# def func1(a,c):
#     print(a+c)
# func1(2,2)

#If you want to return somthing from function we use return function
def function2(a,b):
    """This is a Function which will calculate the avearge of two numbers"""
    average=(a+b)/2
    # print(average)
    return average #When I store value in v this value will store in the return
#If I wan to store my answer is any variable
v=function2(2,2)
print(v)

#Docstrings
""" this is Docstrings syntax"""
print(function2.__doc__) #Way to print doc strings of functions
