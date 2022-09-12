# #Super() & Overriding in Classes
#
# class A:
#     classvar1="I am a variable of class A in Classvar1 variable"
#     def __init__(self):
#         self.var1="I am in class A's Constructor"
#         self.classvar1="I am an instance variable in class var1"
#         self.special="I am special"
# class B(A):
#     classvar2="I am in class B"
#     def __init__(self): #Overriding a constructor of class B
#         # super().__init__()
#         self.var1="I am in class B's Constructor"
#         self.classvar1="I am an instance variable in class B"
#         super().__init__()
# #When we override a method then it consider a overriding method and ignore the first method. If we want to use old method we use super() method to access old method
#
# a=A()
# b=B()
#
# # print(B.classvar1)
# # print(b.classvar1) #Here we access instance variable of class A through b
# # print(a.var1)
# print(b.classvar1)
#
# print(b.special, b.classvar1,b.var1)


#________________________________________________________________________________________________________________________________________
# 28-Aug-2022

# Use od super() and overriding in Python Classes Concept
