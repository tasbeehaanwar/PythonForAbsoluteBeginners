                                                                                                     #Tut#57
#Class Method as a Alternative Constructors

class Employee:
    no_of_leaves=9   #This is class attribute you cannot overwrite this value for instance variables
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole


    #Alternative method by self function
    def printdetails(self):
        return f"Name is {self.name}, Salary is {self.salary}, & Role is {self.role}"

    #Class Method/class method decorator : This method is used to change or overwrite the class method
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    #Use of class Method as a alternative method
    @classmethod
    def from_dash(cls,string):
        # params=string.split("-") #Params will return you a List. #Split will return you a list
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))  #One Liner






sadd=Employee("Saad",400000,"Manager")
Hassan=Employee("Hassan",780000,"Instructor")
Kashan=Employee.from_dash("Kashan-578-Student") #For class Method as a Alternative Constructors we wanna pass this string we

Hassan.change_leaves(34)

# sadd.name="Saad Humaiyun"
# sadd.salary=400000
# sadd.role="Manager"
# sadd.no_of_leaves=12
#
# Hassan.name="Hassan"
# Hassan.salary=300000
# Hassan.role="Instructor"
# print(Kashan.salary)
# print(Employee.no_of_leaves)


#_________________________________________________________________________________________________________________________
# 25-August-2022

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

    @classmethod
    def from_slash(cls,string):
        # params=string.split("-") #This params will return a list due to split() function
        # # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("/"))





Hassan=Employee("hassan",400000,"Frontend developer") #To pass these Instance Arguments will pass to init
Hashim=Employee("Hashim",10000,"Python Programmer") #To pass these Instance Variables Values we use Constructors

# Saad=Employee.from_dash("Saad-670-Insructor") #Pass this Instance String to the class method from_str()
Saad=Employee.from_slash("Saad/670/Insructor") #Pass this Instance String to the class method from_str()
print(Saad.salary)
