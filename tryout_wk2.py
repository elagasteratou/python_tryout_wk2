
good_luck_msg = ["Today is your lucky day", "Be brave! you got this", "Take it nice and easy"]

# choice = int(input("Choose a number between 1-3"))
# if choice == 1:
#     print(good_luck_msg[0])
# elif choice == 2:
#     print(good_luck_msg[1])
# elif choice == 3:
#     print(good_luck_msg[2])
# elif choice > 2 or choice < 1:
#     print("enter a number between 1 and", len(good_luck_msg))

### JW EDIT 1 ###
while True:
    try:
        choice = int(input("Choose a number between 1-3 "))
        if choice == 1:
            print(good_luck_msg[0])
            break
        elif choice == 2:
            print(good_luck_msg[1])
            break
        elif choice == 3:
            print(good_luck_msg[2])
            break
        else:
            print("enter a number between 1 and", len(good_luck_msg))
    except:
        print("enter a number between 1 and", len(good_luck_msg))

## JW EDIT 2 ###
# while True:
#     try:
#         choice = int(input("Choose a number between 1-3 "))
#         if choice in {1,2,3}:
#             break
#         else:
#             print("enter a number between 1 and", len(good_luck_msg))
#     except:
#         print("enter a number between 1 and", len(good_luck_msg))
#
# print(good_luck_msg[choice-1])