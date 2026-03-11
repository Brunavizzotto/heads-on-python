import random

user_choice = input("Choose rock, paper or scissors: ")

if user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice.")
    exit()

choices = ["rock", "scissors", "paper"]

computer_choice = random.choice(choices)

if computer_choice == user_choice:
    print("It's a tie!")
elif computer_choice == "rock" and user_choice == "scissors":
    print("Computer wins!")
elif computer_choice == "scissors" and user_choice == "paper":
    print("Computer wins!")
elif computer_choice == "paper" and user_choice == "rock":
    print("Computer wins!")
else:
    print("You win!")

print("I choose", computer_choice, "and you choose", user_choice)