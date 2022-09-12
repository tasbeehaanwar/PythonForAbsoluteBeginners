# with open("tasbeeha.txt") as f: #With block is a function which handle your file open() and close() function by itself you have no need to open() or close you file again
#     a=f.read(9)
#     print(a)
# # # f=open("tasbeeha.txt")
# # print(f.readline())
# # # f.close()


#____________________________________________________________________________________________________________________________________
# # 22-Aug-2022 to 21-Sep-2022
# #Final Taking Course

#Using With Block To Open Python Files
#What is With Block? How it works?
#With Block is basically a method of reading or writing files. You do not need to close the file with block will automatically handle ur files
#Why we use With block?
#Because you do not worried about close file .


#Syntax
with open("Saad.txt") as f:
    # v=f.read()
    # x=f.readline()
    # print(f.readline())
    # print(f.seek(20))
    # print(f.readline())
    print(f.readable())
    print(f.readlines())
    # print(x)