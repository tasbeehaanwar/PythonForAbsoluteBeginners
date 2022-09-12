# class Employee:                                                                               #Tut#454
#     no_of_leaves=9   #This is class attribute you cannot overwrite this value for instance variables
#     pass
#
# sadd=Employee()
# Hassan=Employee()
#
# sadd.name="Saad Humaiyun"
# sadd.salary=400000
# sadd.role="Manager"
# sadd.no_of_leaves=12
#
# Hassan.name="Hassan"
# Hassan.salary=300000
# Hassan.role="Instructor"
# # print(Hassan.no_of_leaves) Here you can access the class attribute through instance variables
# print(Employee.no_of_leaves) #Or Here you can access the class attribute through orignal class as well
# #You cannot change the class attribute through instance variables you cannot overwrite the orignal value but if you wanna update the instance variables values you can overwrite these individually
# print(sadd.no_of_leaves)
# print(sadd.__dict__) #here I use dict attribute which returns a list

#________________________________________________________________________________________________________________________________________

# # 25-Aug-2022 to 21-Sep-2022

#WE Create our first Class

class myStudents: #Here I create a class
    pass #If you do not use pass the program will give you an error

Saad=myStudents() #Here Saad and Hammad Both are dufferent objects belongs to myStudent() Class
Hammad=myStudents()

#Here we Create Instance Variables for above Objects
Saad.name="Saad"
Saad.Sec="A"
Saad.dep="BSCS"

Hammad.name="Hammad"
Hammad.Sec="C"
Hammad.dep="BSSE"
Hammad.subjects=["Conputer Fundamentals","Physics","Calculus"]

# #What do you think Saad and hammad are same as they both are belongs to the same Class?
# #Let's Check it out
# print(Saad,Hammad) #It will return the different Location of both objects it means that they are not same
print(Hammad.subjects)

