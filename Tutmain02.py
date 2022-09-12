import Tutmain1
print(Tutmain1.printharr("Tasbeehay ye Function ham Tutmain1 se import kr k yahan use karrhy hen Vroo!"))
#There is a big flex while you are importing function from different files this will excecute the whole content/functions in the same file which you obviously don't wanna execute
#For this pupose you have to make "main" function
# if __name__ == '__main__':

print("And the name is:",__name__) #Whenever you ran a function from another file the value of the __name__ will be:the file name from where you import
