# #Dictionary is nothing but key value pairs
# d1={"Harry":"Burger","Tasbeeha":"Sandwitches","Arqum":"Strawberry","Ebad":"Chocolate"}
# """print(type(d1))
# d1["Maham"]="Juice"
# d1["Sakeena"]="Cheese Mayo Roles"
# d1["Unais Ali"]="Samosas"
# del d1["Maham"] #To remove any Element from the dictionary we used "del" Function"""
# """print(d1.copy())
# d3=d1 #Basically Here d3 is a mew pointer here and d1 is has already has its own list
# d3=["Harry"]
# print(d3)
# d3=d1.copy()"""
# #print(d1.get("Ebad"))
# """d1.update({"Saad":"Oranges"})
# print(d1)"""
# print(d1.keys())

#Retaking_____________________________________________________________________________________________________________
# d1={"Tasbiha":"Anwar Adil","Arqum":"Shahabuddin","Saad":"Latif"}
# print(type(d1))
# print(d1)
#You can create dictionary in a dictionary
# d1={"Tasbiha":"Anwar Adil","Arqum":"Shahabuddin","Saad":"Latif","Shubam":{"Breakfast":"Rooti","Lunch":"Sabzi","Dinner":'Salaad'}}
# """Here I Create a Dictionary of students with their Father name & also create another Dict in it which is called Shubam meal routine"""
# #
# # print(d1["Shubam"])
# # print(d1["Arqum"])
# # print(d1["Tasbiha"])
#
# #If I Want to add another Item in the list
# d1["Aqsa"]="Arqum's Sister"
# d1["Irtiza"]="Tasbeeha's Sister"
# print(d1)
# #If we wanna delete someone or something from the list we use del function
# del d1["Shubam"] #Shubbam will be delete after that
# print(d1)


#Using Dictionary Functions
# d1={"Tasbiha":"Anwar Adil","Arqum":"Shahabuddin","Saad":"Latif","Shubam":{"Breakfast":"Rooti","Lunch":"Sabzi","Dinner":'Salaad'}}
# d2=d1
# del d1["Tasbiha"]
# print(d2.copy()) #It will Return the value of a d1 after deleting "Tasbiha", copy function will retuen the copy of a Function.
# d2.update({"Leena":"Toffee"}) #Update Function will update the List Key Value pairs
# print(d2)
# print(d2.keys()) #It will resturn the keys of the dictionary
# print(d2.values()) #It will Return the values
# print(d2.items()) #It will Return the key value pairs



#______________________________________________________________________________________________________________________________________
# 7-August-2022

#Dictionary
#Dictionary is Nothing But Key Value Pairs
dict1={"Harry":"Burger","Saad":"Banana","Hamza":"Yougurt","Moazzam":"Juice","Hassan":{"B":"Salan","l":"Roti","M":"Milk"}}
# print(type(dict1))
# print(dict1)
# print(dict1["Hamza"]) #To fetch Out Dictionary items
# print(dict1["Harry"])
# print(dict1["Hassan"]) #You can Make Dictionary In a Dictionary
# print(dict1["Hassan"]["B"]) #You can also Fetch Items
# #If you want to add More Items
# dict1["Tasmeena"]="Healthy Food"
# dict1["Sameena"]="Junk Food"
# #Key of the string can be any Number or String
# dict1[438]="Cake"
# del dict1[438] #If you want to delete any Key value pairs
# print(dict1)
# print(dict1.update({"Lena":"Toffi"}))
#
# print(dict1)
# print(dict1.keys())
# print(dict1.items())


#_______________________________________________________________________________________________________________________________
#8-August-2022
#List: A container in a Container is called List.
d1=[{}]
print(type(d1))

mydict={"Tasbeeha":"Burger","Saad":"Crispy Fried Chicken","Hamza":"Halwa"}
print(mydict)
print(mydict["Tasbeeha"],mydict["Saad"])

#You can also Create Dictionary in a dictionary
mydict={"Tasbeeha":"Burger","Saad":"Crispy Fried Chicken","Hamza":"Halwa","Hassan":{"Braekfast":"Yogurt","Lunch":"Egg","Dinner":"Salad"}}
print(mydict["Hassan"]["Braekfast"])

#If you want to add more elements in your list
# mydict["Hamamad"]="Nihari"
# #If you wanna delete any element we use del function
# del mydict["Tasbeeha"]
print(mydict)

