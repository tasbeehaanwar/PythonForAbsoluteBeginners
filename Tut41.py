# #using *args and **kwargs
# # def name_of_users(a,b,c,d,e,f): #Here I made a simple fuction and passed some arguments/parameters inside it
# #     print("Names of Insaaans:",a,b,c,d,e,f)
# # name_of_users("Tasbeeha","Anabiya","Tasmiya","Sidra","Irtiza","sakeena")
# #if I wanna add another name in it I have to declare above fisrt then pass another name in it So its not a good practice
# #To fulfill this we used *args
#
#
# # list=("Tasbeeha","Anabiya","Tasmiya","Sidra","Irtiza","sakeena") #IF i WANNA pass this list to below function funargs
#
# # for i in list:
# #     print(i)
#
# def funargs(normal,*args,**kwargs): #Here Im creating a function funargs which take *args as a argument
#     """here I made function which names funargs which take two arguments one is a normal argument here the second one is an arg which take list of element.all the element of the list will pass in it in the form of tupple"""
#     # print(args[5])
#     #Here you have to pass normal argument first then you will have to able to pass args argument this is a thumb Rule if you dont follow this strategy there is alot of chances are there to generate an error
#     print(normal)
#     for i in list:
#         print(i)
#         for key, value in kwargs:
#             print(key,value)
#     print(type(args)) #all the element of the list will pass in it in the form of tupple
#
# list=("Tasbeeha","Anabiya","Tasmiya","Sidra","Irtiza","sakeena","ShakunTala","Hameeda","Hashim Zia","Saad Latif","Saad Hafiz","Kinza","Kissa") #IF i WANNA pass this list to below function funargs
# normal="I am a normal argument"
# funargs(normal,*list) #Here I passed this list in above function by using * to pass it will pass in the form of tupple
# #*args argument is used to add more element in the list
# print(funargs.__doc__) #This is the doc string of above function
#
# kw={"Rohan:Monitor","ShakunTala:Fitness Instructor","Tasbeeha:Programmer"}
# funargs(normal,*list,**kw)

#____________________________________________
# # 22-Aug-2022 to 21-Sep-2022
# #Final Taking Course
#
# *args and **kwargs In Python

#What are *args and **kwargs In Python
#Why we use them?

# def some_names_of_users(a,b,c,d,e,f):
#     print(a,b,c,d,e,f)
# some_names_of_users("Tasbeeha", "Hamza", "Saad", "Arwa", "Faiz","Faiza")
# If you want to add more people what will you do?
#For this Purpose we use  *args and **kwargs
har=["Tasbeeha", "Hamza", "Saad", "Arwa", "Faiz","Faiza"]
#
# def funargs(*args):
#     print(args[0],args[2],args[3],args[5])
#     # print(type(args))
#
# funargs(*har) #Here we pass list in funargs() Function
# print(type(har)) #this will print as a tupple

#You can also iterate list by for loop
# def funargs(*args):
#     for item in args:
#         print(item)
#
#
# funargs(*har) #Here we pass list in funargs() Function
# har.append("Shubam")
# print(har)

#You can also use Normal argumeny
def funargs(Normal,*args):
    for item in args:
        print(Normal,item)

Normal="I am a Normal Argument "
funargs(Normal,*har) #Here we pass list in funargs() Function def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def funargs(normal, *argsrohan, **kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}
funargs(normal, *har, **kw)





