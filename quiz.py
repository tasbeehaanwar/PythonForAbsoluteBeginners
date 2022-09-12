#Write a program which takes the input from the user till the entered number by the user is greater than 100
"""print("Second Quiz")
print("Please Enter the Number")
num=int(input())
while(True):
    if num<100:
        continue
        print(int(num))
    elif num<=100:
        print("Congragulations You Entered correct number")
        break"""
while(True):
    num=int(input("Enter a Number\n"))
    if num>100:
        print("Congragulations You Entered Number greater than 100")
        break
    else:
        print("Try again ")
        continue






