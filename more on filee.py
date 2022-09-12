# f=open("tasbeeha.txt")
# # print(f.tell()) #f.tell() function is used to tell where your pointer is rn
# print(f.readline())
# f.seek(10) #f.seek() function is used to reset the pointer
# # print(f.tell())
# print(f.readline())
# # print(f.tell())
# print(f.readline())
# # print(f.tell())
# f.close()


#__________________________________________________________________________________________________________________________________
# # 22-Aug-2022 to 21-Sep-2022
# #Final Taking Course

# Seek(), tell() & More On Python Files

f=open("Saad.txt")
# print(f.tell()) #tell() Function will tell you where your pointer is write now on which character
print(f.seek(20))
print(f.readline())
# print(f.tell())
print(f.readline())
# print(f.seek(0)) #seek() will be take an argument as a number from where you wanna point your pointer
# print(f.tell())
print(f.readline())
f.close()