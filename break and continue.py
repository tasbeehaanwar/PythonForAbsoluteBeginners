# i=0
# while(1):
#     if i+1<5:
#         i=i+1
#         continue
#         print(i + 1)
#     if(i==44):
#         break #stop the Loop
#         i=i+1
# age=20
# while(True):
#     y=int(input("Enter Your agae:\n"))
#     if y>20:
#         continue
#         print("Congragulations! You Can Drive")
#     elif y==20:
#         print("We Think about you")
#     else:
#         if y<20:
#             print("You are not elogible")
# i=0
# while(True):
#     i=i+1
#     if i==45:
#         print(i)
#         break
# i=0
# while(True):
#     i=i+1
#     print(i)
#     if (i>45):
#         break
#         i=i+1
#Create a program which takes the input from the user until the input number>100. when someone enter a number which is less rhan 100 your program won't stop.
# while(True): #Tasbeeha's code
#     x=int(input("Enter the Number\n"))
#     if x<100:
#         print("Try again")
#         continue
#     elif x==100:
#         print("Congragulations! You Won")
#         break

# while(True): #Harry's Code
#     x=int(input("Enter a Number\n"))
#     if x>100:
#         print("Congragulations! You Won")
#         break
#     else:
#         print("Try Again!!!!!!!!!")
#         continue



#____________________________________________________________________________________________________________________________________
# 21-Aug-2022 to 21-Sep-2022
#Final Taking Course

#Break and Continue Statements
#
# i=0
# while i<100:
#     print(i)
#     i=i+1



# i=0
# while(True):
#     print(i+1)
#     if(i==55):
#         break
#     i=i+1
#
#
# i=0
# while(True):
#     print(i+1)
#     if (i==45):
#         break #stop the loop
#     i=i+1



# i=0
# while(True):
#     if i+1<5:
#         i = i + 1
#         continue
#     print(i+1)
#     if (i==44):
#         break #stop the loop
#     i=i+1


#Create a Program which will take a number as a input untill number is less than 100. When user enter number greater than 100 program will
#be finished

while (True):
    user_input=int(input("Enter a Number:"))
    if user_input>100:
        print("Congragulations! You Entered Graeter than 100")
        break
    else:
        print("Try Again")
        continue


