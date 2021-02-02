import random

# Function generates random advice based on how user says they feel.
# IDEA: as a future feature, make it so that can't have advice you've already been given

def give_advice(dictionary, adjectives):
    user_cont = 1
    used = []
    issue_gen = (random.randint(1, len(dictionary))) - 1
    while user_cont == 1:
        while issue_gen in used:
            issue_gen = (random.randint(1, len(dictionary))) - 1
        q = str("Do you feel " + adjectives[issue_gen] + "? ")
        choice_1 = yes_no_q(q)
        used.append(issue_gen)

        if choice_1 == "y":
            print(dictionary[adjectives[issue_gen]])
            if len(adjectives) == len(used):
                print("... and that was the last piece of advice we had! Sorry :( ")
                user_cont = 0
            else:
                q = "Do you want more advice? "
                choice_2 = yes_no_q(q)
                if choice_2 == "n":
                    user_cont =0
        else:
            if len(adjectives) == len(used):
                print("Sorry, we're all out of advice :( ")
                user_cont = 0
            pass

# Function asks Y/N question and moderates user input.
def yes_no_q(question):
    while True:
        try:
            choice = str(input(question + "Y/N: "))
            if choice in ["y", "n"]:
                break
        except:
            print("Please enter \"y\" or \"n\".")

    return choice
