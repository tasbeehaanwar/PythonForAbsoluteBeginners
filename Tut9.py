#Python List Data TYpe
"""Jwellery=["Ring","Neclace","Bangles","Watch","Deodrant"]
print(Jwellery[1])"""
#Numbers=[2,4,6,89,90,90]
#Numbers[1]=900
#print(Numbers)
"""Numbers.append(10) #Append Function is used to add a number in the end of list
Numbers.remove(89)"""
"""Numbers.pop(2)
print(Numbers)"""
"""Numbers.sort() 
print(Numbers)
Numbers.remove(89)"""
"""print(Numbers[::3])
print(len(Numbers))"""
#Lists
#Muteable-can change
#Immutable-cannot change
#List is Mutable wheare as Tupple is Immutable
# tp=(1,2,3,4,5,6)
# print(tp)
# a=8
# b=5
# a,b=b,a
# print(a,b)



#Rtaking_________________________________________________________________________________________________________________________
#List Data Type where you can strore more than one elements
Programming_Languages_list=["Python","C","C++","Java","PHP","Node Js","C sharp",568,700]
# print(Programming_Languages_list)
numbers=[2,3,5,7,9,11,13]
# print(numbers.sort()) #It will return none
# numbers.sort()
# print(numbers) #When you use sort() function like this it will return you the list of Numbers
# numbers.reverse() #It will return you the list in the reverse form
# print(numbers)
# #Slicing of List also starts with zero Index. Slicing will return you a new list by keeping Orignal list remain as it is.
# print(Programming_Languages_list[::])
# #The Original List will remain save
# print(Programming_Languages_list)
# print(numbers)
#Extended Slice
# print(Programming_Languages_list[::2]) #It will skip one element
# print(Programming_Languages_list[1:9:-6]) #-1 will return reverse list
# print(len(Programming_Languages_list))
# print(max(numbers))
# Programming_Languages_list.append("Larval") #Append is used to add something in the end of the list. You acn append one element more than one time
# print(Programming_Languages_list)
# #Standard way of adding something in a list First you have to make a blankn list then by using append Function you will able to add items in the list
# Programming_Languages_list2=[]
# Programming_Languages_list2.append("Python")
# Programming_Languages_list2.append("C")
# Programming_Languages_list2.append("C++")
# Programming_Languages_list2.append("Java")
# Programming_Languages_list2.append("C sharp")
# print(Programming_Languages_list2)
# numbers.insert(0,89) #Insert Function will add something in between in the list
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.pop() #pop will remove last element from the list
# print(numbers)
# numbers.remove(11)
# print(numbers)
#Tupple(immutable)

#Swapping two Numbers
# a=2
# b=4
# print("Before Swapping:",a,b)
# temp=a
# a=b
# b=temp
# print("After Swapping:",a,b)

#shortcut
a=2
b=4
# a,b=b,a
# print(a,b)


#___________________________________________________________________________________________________________________________
#8-August-2022
#List: A container in a Container is called List.

# List_of_my_School_Friends=["Laraib","Fatima Noor", "Yumna Ali", "Malaika DilDar", "Hania", "Fatima Khalid"]
# print(List_of_my_School_Friends)
# #Slicing Of List: Index of list also starts from zero
# print(List_of_my_School_Friends[::-1]) #It will return the reverse of the List
# List_of_my_School_Friends.sort() #Sort Function will change the Orignal List
# print(List_of_my_School_Friends)
# List_of_my_School_Friends.reverse() #Reverse Function will return the reverse of List
# print(List_of_my_School_Friends)
# List_of_my_School_Friends.append("Wadiya Irfan")
# List_of_my_School_Friends.pop(2)
# print(List_of_my_School_Friends)

#Basic Slicing Of Strings
List_of_my_School_Friends=["Laraib","Fatima Noor", "Yumna Ali", "Malaika DilDar", "Hania", "Fatima Khalid"]
# print(len(List_of_my_School_Friends))
# print(List_of_my_School_Friends[5])
# print(List_of_my_School_Friends[:5])

#Extended Slicing
# print(List_of_my_School_Friends[::2]) #Skip 1 Friends
# print(List_of_my_School_Friends[::3]) #Skip 2 Friends
# print(List_of_my_School_Friends[::4]) #Skip 3 Friends
# print(List_of_my_School_Friends[::5]) #Skip 4 Friends

#Negative Index
# print(List_of_my_School_Friends[::-1])
# # print(List_of_my_School_Friends[::-2])
# # print(List_of_my_School_Friends[::-3])
# # print(List_of_my_School_Friends[::-4])
# # print(List_of_my_School_Friends[::-5])
#
# List_of_my_School_Friends.reverse()
# print(List_of_my_School_Friends)
#
# #Do nat Take Negative Index more than -1 Because SomeTimes it doesn't Work
# print(List_of_my_School_Friends[1:4:-2]) #It Doesn't work when you put some Index Values

#Functions Of List
# numbers=[2,3,4,5,6,6,78,9,7,97,9,8,65]
# print(max(numbers))
# print(min(numbers))
# numbers.append(9)
# numbers.pop()
# numbers.insert(0,67)
# numbers.remove(65)
# numbers.reverse()
# print(numbers)

#Mutable= Can Change
#Immutable= Cannot Change

#Tupple
Tupple=(2,3,4,5,6,7,8,9,66,78)
#Tupples are Immutable
# Tupple[0]=1
# print(Tupple) #You cannot Change the values
# print(max(Tupple))
# print(min(Tupple))

#Way Of Writing Tupple
# Tupple2=(2) #If You are Adding one element in Tupple you should add extra comma ,
# print(Tupple2)

# Tupple3=(2,)
# print(Tupple3) #Correct Way

#Traditional Method
# a=7
# b=8
# temp=a
# a=b
# b=temp
# print(a,b)

#By Using Python
# a=7
# b=8
# a,b=b,a
# print(a,b)


#_____________________________________________________________________________________________________________________________________
# 21-Aug-2022 to 21-Sep-2022
#Final Taking Course

#Python List
Grocery=["Harpic","Lemon Max","Oil","LuX Soap",45,66.8,"78"]
# print(Grocery)
# #If you want to access any item from your list
# print(Grocery[0], Grocery[2])
# print(len(Grocery))

#List Slicing
print(Grocery[::-1])
