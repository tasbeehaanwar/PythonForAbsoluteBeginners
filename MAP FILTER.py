#MAP FUNCTION: If you want to apply the function at more than one element you have map function for this purpose
# numbers=["34","78","70"] #here I wanna apply int function on all the elememnts of the list Then I use map function
#
# numbers=list(map(int,numbers)) #Shortcut by using map function
#
# #Long method
# # for i in range(len(numbers)):
# #     numbers[i]=int(numbers[i])
# #
# # numbers[2]=numbers[2]+2
# # print(numbers[2])
#
#
# def sq(a):
#     return a*a
# # num=[2,3,4,5,6,7,8,9,10]
# # square=list(map(sq,num))
# # print(square)

#You can also use lamba function with map
# num=[2,3,4,5,6,7,8,9,10]
# square=list(map(lambda x:x*x,num))
# print(square)

#Filter Function: filer function is used to filter any element
# list1=[1,2,3,4,5,6,7,8,9]
#
# def is_greater_5(num):
#     return num>5
# gr_thn_5=list(filter(is_greater_5,list1)) #Type casting into list
# print(gr_thn_5)

# #Reduse
# #If I want a sum of all the elements in the list
# num=0
# list1=[2,3,4,5,6,7,8,3]
# # for i in list1:
# #     num=num+i
# # print(num) #Sum of all the elements in the list

#More Pythonic way for this
from functools import reduce
list1=[2,3,4,5,6,7,8,3]
num=reduce(lambda x,y:x+y,list1)
print(num)



