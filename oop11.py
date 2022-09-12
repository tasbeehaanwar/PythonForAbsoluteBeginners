#Public: A information which you have written somewhere in paper that you want to share with public
#Protected: A information which you have written somewhere in paper that you want to share with your Family
#Private: A information which you have written somewhere and you don't want to share with anyone else


class Employee:
    no_of_leaves=9   #This is class attribute you cannot overwrite this value for instance variables
    #Public Variable: Access by everyone inside or outside the class
    var=0
    #Protected Variables: Access By the Main class or Child class but can't access by outsider class
    _protec=45
    #Private Variable: Cannot Access easily By Parent or Child class you can access it by unique metyhod
    __private=67


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

    #If you want to create a simple method which print something we use Sataic Methods
    @staticmethod
    def print_good(string):
        print("This is good"+string)

class Programmer(Employee):
    def __init__(self,aname,asalary,arole,alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages=alanguages





    def Programmerdetails(self):
        return f"Name is: {self.name}\nSalary is: {self.salary}\nRole is: {self.role}\nExpertise in Languages: {self.languages}"








sadd=Employee("Saad",400000,"Manager")
Hassan=Employee("Hassan",780000,"Instructor")
Kashan=Employee.from_dash("Kashan-578-Student") #For class Method as a Alternative Constructors we wanna pass this string we

Asad=Programmer("Asad",750000,"Pseudo Programmer",['python','c++'])
Arqam=Programmer("Arqam",900000,"Self Taught pseudo Python Programmer",['python','c++'])
Hassan.change_leaves(34)

print(Employee.var)
print(Programmer._protec) #Protect can access through parent or child class both
print(Employee._Employee__private) #You can access Private variable like this Format This is called Name Mangling


