# # 22-Aug-2022 to 21-Sep-2022
# #Final Taking Course


#How to Write in a File
#First you have to open a file pointer
# f=open("Saad2.txt",'w') #This method will craete a new file
# f.write("Saad Bhoi Bhut achy hain")
# f.close()

#If you want to append some text in a file you can use append function
# f=open("Saad2.txt",'a') #'a' append Mode is open this function will append more text in a blank file
# f.write("Saad Bhoi Bhut achy hain\n")
# f.close()

#If you want to know about how many characters you wrote in text file you just point your content in a pointer
# f=open("Saad2.txt",'w') #'a' append Mode is open this function will append more text in a blank file
# a=f.write("Saad Bhoi Bhut achy hain\n")
# print(a) #This will give you the length of characters you write
# f.close()


#Important Note
# If you open your file in a write Mode 'w' all the content you append will remove and the file is ready for add new content
# If you open your file in append Mode 'a' your file will be raedy to append add more content file will take

#How to handle Read and write Both
f=open("Saad2.txt", 'r+')
print(f.read())
#If you want to add or write something in a file
print(f.write("Thank you;)"))
f.close()