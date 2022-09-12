# #Multilevel Inheritance
# class Daad:
#     Basketball=2
#
# class Son(Daad):
#     dance=4
#     def isdance(self):
#         return f"I love dancing {self.dance} no of times"
#
# class GrandSon(Son):
#     dance=6
#     #Grandson can also create or update their own methof or used inherited method from class Son
#     def isdance(self):
#         return f"Hay Jackson Yeahh!!! I love dancing {self.dance} no of times"
#
# Darry=Daad()
# Sarry=Son()
# Garry=GrandSon()
#
# print(Garry.isdance())
# print(Garry.Basketball)



#EASY EXERCISE
#Create three Classes ElectronicDevices, PocketGaget, Phone by using Concept of multilevel Inheritance.

#__________________________________________________________________________________________________________________________________
# 27-Aug-2022

#Multilevel Inheritance

class Dad():
    pass

class Son(Dad):
    pass
class GrandSon(Son):
    pass
