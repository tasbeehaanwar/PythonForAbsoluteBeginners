# # File IO Basics
# # For Example we have two Basic TYpes of Memories
# # RAM (volitile) When the power is off your data will be lost
# # Hardisk (Non Volitile) Your data will be saved forever
# # "Modes of Files
# # Read Mode "r"-open file for reading-default mode
# # Write Mode "w"-open file for writing
# # Exclusive Creation Mode "x"-creates files if not exist then this mode will be useful otherwise it doesn't work.
# # Append Mode "a"-add more content to a file in the last
# # Text Mode "t"-If I want to open my file in a text mode-default mode
# # Binary Mode "b"_read your text in a Binary mode we use this mode to update the file
# # Plus Mode "+"-To read or write both"
# """Question of the day?
# Write the syntax of Doc string
# syntax:"""
# # def function1():
# #     """Heyyyyyyy! Here is your doc_string Vrooo!"""
# #     print("Heyyyy! You are in Your Function 1")
# # print(function1())
# # print(function1.__doc__)
# def function2():
#     """Heyyyyy! You are here"""
#     print("Yor are in Your Function 2")
#     print(function2())
#     print(function2.__doc__)
# # def function1():
# #     """Heyyyyyyy! Here is your doc_string Vrooo!"""
# #     print("Heyyyy! You are in Your Function 1")
# # print(function1())
# # print(function1.__doc__)
# print(function2.__doc__)



#__________________________________________________________________________________________________________________________________
# # 22-Aug-2022 to 21-Sep-2022
# #Final Taking Course

#File IO Basics

#What are Files in Python?
# WE already know that we have two types of memories
#Volatile (RAM) ________data will be lost when power is switched off
#Non-Volatile (Hard Disk) _______________________________________data will not lost when power is switched off

#Which Modes you can open a file

"""
'r' = Read mode (open File for reading)
'w' = Write Mode (open File for writing)
'x' = Exclusive Creation (If file is already exists this method will be fail a new file will create if not exists)
'a'=  Append Mode (Add more Content in a file)
't'= Text Mode (It means that your file contains some text)
'b'= Binary Mode (Open file in Binary mode)
'+'= Plus Mode (Open file for reading and witing)
"""
