# Health-Management
#import datetime
import time

#def gettime():
    #return datetime.datetime.now().strftime("%d-%m-%y")
def gettime2():
    return time.asctime(time.localtime(time.time()))


print("\t\t\tWelcome to Health Management\n\nDo you want to Retrive or Log your values\n")
user_input = int(input("Press 1 to Log and press 2 to Retrive\n"))
if user_input == 1:
    user_input2 = int(input("Press 1 for Exercise and 2 for Food\n"))
    if user_input2 == 1:
        user = str(input("Type your name first, for creating account. \nYou need to remember that name to retrive your account\n"))
        userdata = str(input("Type here\n"))
        with open(f"{user}exercise.txt", "a") as e:
            e.write(f"{str([str(gettime2())])} : {userdata} \n")
        print("successfully added")
    elif user_input2 == 2:
        user = str(input("Type your name first, for creating account. \nYou need to remember that name to retrive your account\n"))
        userdata = str(input("Type here\n"))
        with open(f"{user}food.txt", "a") as e:
            e.write(f"{str([str(gettime2())])} : {userdata} \n")
        print("successfully added")

if user_input == 2:
    user_input2 = int(input("Press 1 for Exercise and 2 for Food\n"))
    if user_input2 == 1:
        userdata2 = str(input("Please type your account name\n"))
        with open(f"{userdata2}exercise.txt") as g:
            for i in g:
                print(i, end=" ")
    elif user_input2 == 2:
        userdata2 = str(input("Please type your account name\n"))
        with open(f"{userdata2}food.txt") as g:
            for i in g:
                print(i, end=" ")

b = int(input("Do you want to exit or again Log/Retrive your account\nIf you want to RETRIVE your account then press 1\nIf you want to LOG your account then press 2\n"))


print("\t\t\t\nThanks for using our HEALTH MANAGEMENT")
f = input()

