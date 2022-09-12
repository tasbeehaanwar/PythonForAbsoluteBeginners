# #Time Module Excecution
# #if I wanna calculate the time execution of program we use time module
# import time
#
# initial1=time.time() #Here I used Time function this time fuction is the function of above time module. This will give you number of tics(1 tic=1sec)
# # print("Excecution time of While loop",initial1)
#
# print("Implementation of while Loop")
# k=0
# while(k<45):
#     print("Harry Bhoooi")
#     time.sleep(2) #time.sleep() function is used here which take argument 2 this function will give you the output after two sec & thn sleep
#     k=k+1
# print("While Loop ran in:",time.time()-initial1,"seconds")
#
#
# # initial2=time.time()
# # print("Execution time of for Loop:",initial2)
# # print("For Loop:",initial1-initial2)
# # print("Implementation of for Loop")
# # for i in range(34):
# #     print("Harry Bhoooi")
# # print("For Loop ran in:",time.time()-initial2,"seconds")
# # time.sleep(2)
#
#
#
# # #Another Time Function this function give us our local time
# # localtime=time.asctime(time.localtime(time.time())) #
# # print(localtime)

#____________________________________________________________________________________________________________________________________
# 24-Aug-2022 to 21-Sep-2022
#Final Taking Course

# Time Module In Python
import time

# initial_time=time.time() #this will return in the form of clock tick (1 tick = 1 sec)
#
# x=0
# while(x<=44):
#     print("This is my while Loop")
#     x+=1
# print("While loop ran in ", time.time()-initial_time,"seconds")
#
# initial_time2=time.time()
# print("Above Program by using for Loop")
# #Above Program bt using for Loop
# for i in range(45):
#     print("This is my For Loop")
# print("For Loop ran in ", time.time()-initial_time2,"seconds")

local_time=time.asctime(time.localtime(time.time())) #How to calculate Local time
initial=time.time()
time.sleep(3)
print(local_time)
time.sleep(3)
print(local_time)
time.sleep(3)
print(local_time)
time.sleep(3)
print(local_time)
time.sleep(8)
print(local_time)
print("This is the excecution time: ",initial-time.time())