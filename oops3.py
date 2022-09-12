# # class Employee:                                                                                Tut#55
# #     no_of_leaves=9   #This is class attribute you cannot overwrite this value for instance variables
# #     #Alternative method by self function
# #     def printdetails(self):
# #         return f"Name is {self.name}, Salary is {self.salary}, & Role is {self.role}"
# #
# # sadd=Employee()
# # Hassan=Employee()
# #
# # sadd.name="Saad Humaiyun"
# # sadd.salary=400000
# # sadd.role="Manager"
# # sadd.no_of_leaves=12
# #
# # Hassan.name="Hassan"
# # Hassan.salary=300000
# # Hassan.role="Instructor"
# #
# # print(Hassan.printdetails())
# # print(sadd.printdetails())
# # print(sadd.no_of_leaves)
# # print(Hassan.no_of_leaves)
# # print()
#
#
#
#
# # Use of Constructor: When I made a object Employee I gave instance variables manually one by one if I wanna give argument to the Employee we use constructors
#
# class Employee:
#     no_of_leaves=9   #This is class attribute you cannot overwrite this value for instance variables
#     #Constructor/__init__
#     def __init__(self,aname,asalary,arole):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole
#
#
#     #Alternative method by self function
#     def printdetails(self):
#         return f"Name is {self.name}, Salary is {self.salary}, & Role is {self.role}"
#
# sadd=Employee("Saad",400000,"Manager")
# Hassan=Employee("Hassan",780000,"Instructor")
#
# # sadd.name="Saad Humaiyun"
# # sadd.salary=400000
# # sadd.role="Manager"
# # sadd.no_of_leaves=12
# #
# # Hassan.name="Hassan"
# # Hassan.salary=300000
# # Hassan.role="Instructor"
# print(Hassan.printdetails())
# print(sadd.printdetails())



#_--------------------------__________________________________________________________________________________________
# 25-Aug-2022 to 21-Sep-2022

# Instance & Class Variables

class Employee:
    no_of_leaves=10 #This is class variable valid for all objects/Tepletes belongs to this class. You can access this variable through objects
    pass

Hassan=Employee()
Hashim=Employee()

Hashim.name="Hashim"
Hashim.salary=10000
Hashim.role="Python Programmer"


Hassan.name="hassan"
Hassan.salary=400000
Hassan.role="Frontend developer"

Employee.no_of_leaves=11 #If you want to change class variable through Hashim or Hassan you cannot change it. it will create new Instance variable in which object you want to change no_of_leaves
print(Hashim.__dict__) #This Function will return all Instance Variables of Hashim in the form of Key value pairs
Hashim.no_of_leaves=13
print(Hashim.__dict__)

print(Employee.no_of_leaves)
#
# print(Hashim.no_of_leaves)
# print(Hassan.no_of_leaves) #You can Access Class Variables through objects
