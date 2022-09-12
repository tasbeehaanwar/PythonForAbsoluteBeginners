#Create  a program in which you hide a a number and let the user guess what the number is.
#no of guesses are Max 9 or Min 5
#print No of guesses
#print Number of Guesses he took to Finished
#When number of guesses finished print "Game Over"
# n=18
# number_of_guesses=9
# while(number_of_guesses<9):
#     guess_number=int(input("Enter a Number\n"))
#     if guess_number>18:
#         print("Your Entered number is very high! Please Enter Lower Number")
#     elif guess_number<18:
#         print("Your Entered number is very Low! Please Enter Higher Number")
#     elif guess_number==18:
#         print("Congragulations! You Entered Correct Number you Won!")
#     else:
#         if number_of_guesses>9:
#             print("Game Over")
import time

initial=time.time()
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")
print("Execution program ran in:",time.time()-initial,"seconds")

