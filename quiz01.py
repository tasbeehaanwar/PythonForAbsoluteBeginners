#Its Quiz Time
#Create a List and then detect the item must be a number than check  number should be greater than 6 then print thaht number.
#solution:
num1=["Tasbeeha","Harry",8,7,9]
for item in num1:
    if str(item).isnumeric() and item>6:
        print(item)