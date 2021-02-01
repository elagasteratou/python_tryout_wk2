
good_luck_msg = ["Today is your lucky day", "Be brave! you got this", "Take it nice and easy"]


choice = int(input("Choose a number between 1-3"))
if choice == 1:
    print(good_luck_msg[0])
elif choice == 2:
    print(good_luck_msg[1])
elif choice == 3:
    print(good_luck_msg[2])
elif choice > 2 or choice < 1:
    print("enter a number between 1 and", len(good_luck_msg))


