#                                                                                         #  Tut#56
# class Employee:
#     no_of_leaves=9   #This is class attribute you cannot overwrite this value for instance variables
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
#     #Class Method/class method decorator : This method is used to change or overwrite the class method
#     @classmethod
#     def change_leaves(cls,newleaves):
#         cls.no_of_leaves=newleaves
#
#     #Use of class Method as a alternative method
#     @classmethod
#     def from_str(cls):
#
#
#
#
# sadd=Employee("Saad",400000,"Manager")
# Hassan=Employee("Hassan",780000,"Instructor")
#
# Hassan.change_leaves(34)
#
# # sadd.name="Saad Humaiyun"
# # sadd.salary=400000
# # sadd.role="Manager"
# # sadd.no_of_leaves=12
# #
# # Hassan.name="Hassan"
# # Hassan.salary=300000
# # Hassan.role="Instructor"
# print(Employee.no_of_leaves)

#______________________________________________________________________________________________________________________________________
# 25-Aug-2022 to 21-Sep-2022
#Class Methods In Python

class Employee:
    no_of_leaves=10 #This is class variable valid for all objects/Tepletes belongs to this class. You can access this variable through objects

    #Here I Create Contructors which used to handle instance variables. We use Consructors when we do not want to create Instance variables manually
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

     #Here we create a self method which is called class Methods
    def printdetails(self):
        return f"Name of Employee is {self.name}, Salary is about {self.salary}, Role is {self.role} "

    # Class Method/class method decorator : This method is used to change or overwrite the class method
    @classmethod
    def change_leaves_function(cls,newleaves):
        cls.no_of_leaves=newleaves


Hassan=Employee("hassan",400000,"Frontend developer") #To pass these Instance Arguments will pass to init
Hashim=Employee("Hashim",10000,"Python Programmer") #To pass these Instance Variables Values we use Constructors


Hashim.change_leaves_functpion(50)
#If You want to print class Variable
print(Employee.no_of_leaves)
print(Hassan.no_of_leaves)
print(Hashim.no_of_leaves) #This is the method of access class Variable

