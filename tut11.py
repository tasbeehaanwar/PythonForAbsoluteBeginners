# #Exercise:1 Create your own dictionary based on 5 To 10 Words and take the input from the user and return the meanimg of the dictionary
# print("This is my First Dictionary ")
# d1={"Mutable":"can change","Unmutable":"cannot change","Abandon":"ive up completely (a practice or a course of action)",}
# d1["conflicts"]="a serious disagreement or argument, typically a protracted one"
# print(d1)
# print("Please Enter Your Desired Word")
# s1=input()
# print("Your required word meaning is:",d1[s1])
# print("Thanks For using my Dictionary")
# #Examples From Comments
# """print("Welcome to Dictionary")
# Dictionary={"abase":" cause to feel shame", "benefit":"advantage", "callow":"young and inexperienced", "dally":"waste time", "endear":"make attractive"}
# print("The required meaning is:")
# Search=input()
# print(Dictionary[Search])
# print("Thanks for using Dictionary")"""
# #Example 2
# """Oxford ={"mutable":"can be change","unmutable":"can not be changed","precisely":"very carefully","trapped":"bounded"}
# print("Enter a word whose meaning you want!");
# word=input();
# print("the meaning of "+ word +" is " + Oxford.get(word));"""



#_________________________________________________________________________________________________________________________________
#7-August-2022
#Exercise#01: Create a Dictionary based on 3 to 4 Key Value Pairs. Ask the user To Enter Their Desired word & program will be return the meaning of that word.

MyDictionary={"Set":"A set is a Collection Of well Define Objects", "Built-IN functions":"These Function are already written in Library Files to make the user work easy","Mutable":"Can Change"}
user_Input=input("Enter Your Desired Word:")
print("Your Desired Word Meaning is:", MyDictionary[user_Input])