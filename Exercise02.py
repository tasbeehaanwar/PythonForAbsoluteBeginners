# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
# print("My Faulty Calculator")
# tuple=tuple("45*3=555",)
# print("Enter First Value:")
# a=int(input())
# print("Enter Second Value")
# b=int(input())
# if a+b:
#     print("Addition of a & b is:", int(a) + int(b))
# elif a-b:
#     print("Subtraction of a & b is:", int(a) - int(b))
# elif a*b:
#     print("Multiplication of a & b is:",int(a)*int(b))
# print("A Faulty Calculator")
# a=input("Enter First Number\n")
# b=input("Enter Second Number\n")
# c=input("So What you want Now?\n +,-,*,/,%\n")
# if a==45 and b==3 and c=='*':
#     print("555")
# elif a==56 and b==9 and c=='+':
#     print("77")
# elif a==56 and b==6 and c=='/':
#     print("4")
# elif c=="+":
#     print("The Sum of a and b is:",int(a)+int(b))
# elif c=="_":
#     print("The Subtraction of a & b is:",int(a)-int(b))
# elif c=="*":
#     print("The Multiplication of a & b is:", int(a) * int(b))
# elif c=="/":
#     print("The Divison of a & b is:", int(a) / int(b))
# elif c=="%":
#     print("The Reminder of a & b is:", int(a)%int(b))
# else:
#     print("Error! Kindly check your input & try again:)")
# print("My Faulty Calculator")
# x=int(input("Enter First Number:\n"))
# y=int(input("Enter SEcond Number:\n"))
# z=input("Enter Your Choise: +,-,*,/,%\n")
# if x==45 and y==3 and z=="*":
#     print("555")
# elif x==56 and y==9 and z=="+":
#     print("77")
# elif x==56 and y==9 and z=="/":
#     print("4")
# elif z=="-":
#     print("The Sub of x & y is:",int(x)-int(y))
# else:
#     print("Try Again!!!!!!!")


# This Calculator will give all results correctly except the three particular
# operations which shall show the following faulty results
# 45*3 = 555, 56+9=77, 56/6=4
while(True): #Code by Someone else from comments section
    var1 = int(input("Enter the First Operand\n"))
    var2 = int(input("Enter the Second Operand or exponent in case of power calculation\n"))
    operator=input("Enter the Type of Operation, Available Operations: + , - , * , / , ** , %\n")
    if (max(var1, var2) == 45 and min(var1, var2) == 3 and operator == "*"):
        print("Result:", "555")
    elif (max(var1, var2) == 56 and min(var1, var2) == 9 and operator == "+"):
        print("Result:", "77")
    elif (var1== 56 and var2 == 6 and operator == "/"):
        print("Result:", "4")
    else:
        if (operator == "+"):
            print("Result:", var1 + var2)
        elif (operator == "-"):
            print("Result:", var1 - var2)
        elif (operator == "*"):
            print("Result:", var1 * var2)
        elif (operator == "/"):
            print("Result:", var1 / var2)
        elif (operator=="**"):
            print("Result:", var1 ** var2)
        elif(operator=="%"):
            print("Result:", var1 % var2)
    if((input("Do you want to continue calculating? If yes type 'Y' else type 'N' \n")).capitalize()
            =='Y'):
        continue
    else:
        print("Thank You for using the Calculator")
        break





