# # # IF or If Else
# # """var1=67
# # var2=78
# # print("Please Enter a Number:")
# # var3=int(input())
# # if var3 > var2:
# #     print("Greater")
# # elif var3==var2: #elif used as a else if
# #         print("Equal")
# # else:
# #     print("Lesser")"""
# # List1=[1,2,3,4,5,6,7,8,9]
# # #print(99 in List1)
# # """if 5 in List1: #in is a keyword which is used where your required word is present.
# #     print('Yes it is present in the List')"""
# # """if 10 not in List1: #not in is a keyword which is used where your required word is not present.
# #     print("Its not Present in the list")"""
# # #Challenge: Write a program which take the age from the user by using if else statements.
# # #1_If you are 18+ "You are eligible you can Drive".
# # #2_If you are less than 18 "You are not eligible for Driving".
# # ##_ If you are complete 18 "We cannot decide yet, Please visit our centre".
# # """print("Welcome")
# # print("Please Enter Your age")
# # age=int(input())
# # if age>18:
# #     print("Congragulations!, You are Eligible for driving")
# # elif age<18:
# #     print("Sorry!, You are not Eligible for Driving")
# # elif age==18:
# #     print("We cannot decide yet, please visit out centre")
# # else:
# #     print("You are not Eligible")"""
# #
# #
# # print("Welcome")
# # print("Please Enter Your age")
# # age=int(input())
# # if age 1:
# #     print("Congragulations!, You are Eligible for driving")
# # elif age<18:
# #     print("Sorry!, You are not Eligible for Driving")
# # elif age==18:
# #     print("We cannot decide yet, please visit out centre")
# # else:
# #     print("You are not Eligible")
#
#
# #___________________________________________________________________________________________________________________________________
# # 8-August-2022
# # #IF ELSE & ELIF CONDITIONS IN PYTHON
# #
# # var1=3
# # var2=8
# # var3=int(input("Enter a Number:"))
# # #
# # if var3>var2:
# #     print("Greater")
# # if var3==var2:
# #     print("Equal")
# # else:
# #     print("lesser")
#
# #If one condition is True in the given Conditions or we want that the program will not check all conditions at a time.  If One Condition is TRue the program will came out and excecute other statements
# #In this case we use elif to check if one condition is TRue Execute it.
# #These Statements are Called If-Else Ladder
# # if var3>var2:
# #     print("Greater")
# # elif var3==var2:
# #     print("Equal")
# # else:
# #     print("Lesser")
#
# #
# # #Use Of "in" or "not in" Keywords usage
# # #"not" and "in" are two Different Keywords
# # List=[1,2,3,4,5]
# # # print(5 in List) #In Keyword Used where the element is present in the list
# # print(15 not in List)
# # if 6 in List:
# #     print("True")
# # else:
# #     print("False")
#
# #Today's Challenge!
# #Create a Program which takes the user input ask the user about his/her age and print below condition.
# #If your age is Greater than 18 "You Are Eligible For Drive"
# #If your age is equal to 18 "You Can Try"
# #If your age is less than 18 "You Are Not Eligible".
#
# # print("WELCOME TO OUR DRIVING REQUIREMENTS!")
# # age=int(input("Please Enter Your Age:"))
# #
# # if age>18:
# #     print("Congragulations! You Are Eligible For Driving :)")
# # elif age==18:
# #     print("We are Not sure About You!","Kindly Visit Our Branch & we will decide later after your physical TEST.","Thank You!")
# # else:
# #     print("Sorry! You are not Eligible For Driving ;(\n","Try Next Time!\n","Thank You:)")
#
#
# #________________________________________________________________________________________________________________________________
# # 21-Aug-2022 to 21-Sep-2022
# #Final Taking Course
#
# #If Else statement
#
# var1=9
# var2=99
# var3=int(input("Enter a Number:"))
# # if var3>var2:
# #     print("Greater")
# # if var3==var2:
# #     print("Equal")
# # else:
# #     print("Lesser")
#
#
# # if var3>var2:
# #     print("Greater")
# # elif var3==var2:
# #     print("Equal")
# # else:
# #     print("Lesser")
#
# #Quiz
# #Create a Program which takes Human age as a input & then check out the conditions below.
# #if age is greater than 18 print "You are Eligible For Driving"
# #if age==18 print "Please Visit our centre for physical driving test"
# #if age<18 print "You are not eligible"


age=int(input("Please Enter your age:"))
age=100
if age>18:
    print("You are Eligible For Driving")
elif age==18:
    print("Please Visit our centre for physical driving test")
else:
    print("You are not eligible")
    if age>100:
        print("You Entered Invalid age")
