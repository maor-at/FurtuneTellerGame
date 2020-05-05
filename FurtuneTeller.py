import random

print("welcome to the Furtune Teller game! \n "
      + "Select a color and a number and i will tell you what future holds for you!")

answer = True

while answer:
    color = input("please select a color of the following: [red,blue,green,yellow] ").lower()
    if color == "red" or color == "blue":
        number = int(input("please select a number [1,3,6,9]"))
        if number == 1:
            print("you are lucky! you will find your meaning in 3 years")
        elif number == 3:
            print("if love is what you seek, then don't worry you will meet her/him soon")
        elif number == 6:
            print("you will be a famous person ")
        elif number == 9:
            print("you will have a great family with 6 kids!")
        else:
            print("only the number [1,3,6,9] allowed! ")

    elif color == "green" or color == "yellow":
        number = int(input("please select a number [2,4,5,7]"))
        if number == 2:
            print("you will be a millionaire")
        elif number == 4:
            print("you will buy your dream house")
        elif number == 5:
            print("don't worry about your career, you will find the job for you")
        elif number == 7:
            print("you will be surrounded with friends")
        else:
            print("only the number [2,4,5,7] allowed! ")
    else:
        print("only the colors [red,blue,green,yellow] allowed")

    answer = input("want to continue play ? (y/n)")
    if answer == "y":
        answer = True
    else:
        answer = False
