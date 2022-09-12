# List1=[1,2,3,4,5,6,7,8,9]
# for item in List1:
#     print(item)
# List=["Tasbeeha","Anabiya","Enzul","Zaid","Zainab Fatima"]
# for item in List:
#     print(item)
# """list1 = [ ["Harry", 1], ["Larry", 2],
#            ["Carry", 6], ["Marie", 250]]
# for item,lollypop in list1:
#     print(item, "and lolly is",lollypop)"""
# """list1 = [ ["Harry", 1], ["Larry", 2],
#            ["Carry", 6], ["Marie", 250]]
# dict1=dict(list1) #Typecasting list into dictionary
# for item in dict1:
#     print(item)"""
# """for item,lollypop in dict1.items():
#     print(item, "and lolly is",lollypop)"""
# #Its Quiz Time
# #Create a List and then detect the item must be a number than check  number should be greater than 6 then print thaht number.
# #solution:
# # num1=["Tasbeeha","Harry",8,7,9]
# # for item in num1:
# #     if str(item).isnumeric() and item>6:
# #         print(item)



#_____________________________________________________________________________________________________________________________________
# 8-August-2022
#FOR LOOP
# list=["SAAD","hAMZA","hASHIM","HASSAN","ZUNAIRA"]
# print(list[0],list[1],list[2],list[3]) #to print item of the list this will be time taking method of iterating each element one by one
# # For this Purpose we use for Loop
# for item in list:
#     print(item)

#If we have List in a List
# List1=[["Harry","Burger"], ["Marie","Pizza"],["Tarry","Paratha"] ,["Karie","Jelly"]]
# for item in List1:
#     print(item) #This will Return a List

# List1=[["Harry","Burger"], ["Marie","Pizza"],["Tarry","Paratha"] ,["Karie","Jelly"]]
# for item , Junkfood in List1:
#     print(item, "like to eat", Junkfood) #You can Unpack any List like that

# dict=dict(List1)
# print(dict) #You can Assigned your List in the Form of Dictionary
# for item in dict.items(): #You can Iterate Dictionary Items by Using .item Function
#     print(item)

# for item, JunkFood in dict:
#     print(item,"like to eat", JunkFood)  #You cannot unpack Dictionary Items

# for item, JunkFood in dict.items(): #You can unpack Dictionary Items Like that by using .items() Function
#     print(item,"like to eat", JunkFood)


#Quiz: Create a List and then iterate only those items which are numbers and greater than 6.
#If the item is Number than check that the number is greater than 6 than print that number.

#My Code
# List2=[1,2,3,6,7,8,9,44]
# for item in List2:
#     if item>6:
#         print(item)


# #Harry's Code
# List_Of_Harry=[int,float,str,"Tasbeeha","Saad","Hammad",2,3,4,7,8,9,77,75,4,5,3,33,32]
# for item in List_Of_Harry:
#     if str(item).isnumeric() and item>6:
#         print(item)

#_______________________________________________________________________________________________________________________________
# 21-Aug-2022 to 21-Sep-2022
#Final Taking Course

#loops in Python
# List1=[["Harry","Burger"], ["Marie","Pizza"],["Tarry","Paratha"] ,["Karie","Jelly"]]
# for item, food in List1:
#     print(item, "loves to eat" ,food)
#
# dict=dict(List1)
# print(dict)

#Quiz:
#Craete a program which generates a List of numbers greater than 6
my_list=["Tasbeehay","Saad","Siemon",66,77,12,4,5,2,4,5]
for item in my_list:
    if str*(item).isnumeric() and item>6:
        print(item)

