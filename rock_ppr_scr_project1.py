#rock, paper, scissor game with computer
#0 for rock, 1 for paper, 2 for scissors
import random
list = ['Rock', 'Paper', 'Scissor']
user_input=input("Please enter your choice of 'Rock, Paper, Scissor' indicated by 0, 1 or 2: ")

user_choice=int(user_input)
if (user_choice >= 3 or user_choice < 0):
    print("You entered invalid number")
else:

    comp_choice = random.randint(0,2)
    print(f"You entered {list[user_choice]}")
    print(f"Computer entered {list[comp_choice]}")

    #comparing the two choices to see who wins

    if (user_choice == comp_choice):
        print("Draw!")
    elif (user_choice == 0):
        if (comp_choice == 1):
            print("You lose!")
        elif (comp_choice == 2):
            print("You win!")
    elif (user_choice == 1):
        if (comp_choice == 2):
            print("You lose!")
        elif (comp_choice == 0):
            print("You win!")
    elif (user_choice == 2):
        if (comp_choice == 0):
            print("You lose!")
        elif (comp_choice == 1):
            print("You win!")

