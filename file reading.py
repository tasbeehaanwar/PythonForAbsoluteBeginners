# #How to read a file
# # f=open("tasbeeha2.txt",'a') #here a argument is used to append/add some text
# # a=f.write("Tasbeeha is a good girl\n\n") #Here I used \n to rewrite the line as a new line character
# # print(a)
# # f.close()
# #Write mode is used to remove extra text from the file where as append "a" mode is used to add more text in a file
# f=open("tasbeeha3.txt",'a') #here a argument is used to append/add some text
# a=f.write("Tasbeeha is a good girl\n\n") #Here I used \n to rewrite the line as a new line character
# print(a)
# f.close()
# # How to Handle read and write both
# f=open("tasbeeha.txt","r+")
# print(f.read())
# f.write("Thank you to remain calm You are amazing enough")

#____________________________________________________________________________________________________________________________________
# # 22-Aug-2022 to 21-Sep-2022
# #Final Taking Course

#Read and Write both are defaults modes
#How to Write in a File.
#First Create a txt file

#How to read any File
# f=open("Saad.txt", "rt") #This file is open in 'rt' Mode Read text Mode
# content=f.read()
# print(content)
# f.close() #You Must have to close the file


#If you want to read your content line by line you can iterate lines
# f=open("Saad.txt", "rt") #This file is open in 'rt' Mode Read text Mode
# # content=f.read()
# for line in f:
#     print(line, end="")
#
# f.close() #You Must have to close the file

#usage of readline() Function
# f=open("Saad.txt", "rt") #This file is open in 'rt' Mode Read text Mode
# print(f.readline(),end="") #You can read line by line by using raed line function
# print(f.readline(), end="")
# print(f.readline())
# # content=f.read()
# # for line in f:
# #     print(line, end="")
#
# f.close() #You Must have to close the file

#If you want to store your content in the form of list you can use readlines() function as well.
f=open("Saad.txt", "rt") #This file is open in 'rt' Mode Read text Mode
print(f.readlines())  #If you want to store your content in the form of list you can use readlines() function as well.

f.close() #You Must have to close the file