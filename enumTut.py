# #Enumerate Fubction:
# #Suppose Markzurkburk's wife call hima nd said k yr ye ye Samziyan le ana wo list fwd krdeti usko. after few second she call him back & said me to mzazak krrhi th bs Aloo or Bhindi le ana baki list k sab items ko ignore krdena
#
# list=["Bhindi","Aloo","Chopsticks","chowmin"]
# i=1
# for item in list:
#     if i%2 != 0:
#         print(f"Jarvis please buy{item}")
#         i+=1
#
# #To amke our worl aesier we use enumerate function
# for index,item in enumerate(list):
#     if index%2==0:
#         print(f"Jarvis please buy{item}")

#_________--------------------------------______________________________________________________________________________________________
# 24-Aug-2022 to 21-Sep-2022


list=["Bhindi","Aloo","Chopsticks","chowmin"]
i=1
for item in list:
    if i%2 != 0:
        print(f"Jarvis please buy {item}")
        i+=1

#To amke our worl aesier we use enumerate function
for index,item in enumerate(list):
    if index%2==0:
        print(f"Jarvis please buy {item}")


