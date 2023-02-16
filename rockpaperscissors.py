import random

print("Let's play Rock Paper Scissors!")

choices = ['rock', 'paper', 'scissors']

rules = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

while True:
    player_choice = input("Choose an option (rock/paper/scissors): ")
    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors")
        continue
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        print("It's a tie!")
    elif rules[player_choice] == computer_choice:
        print("You win!")
    else:
        print("You lose!")
    play_again = input("Would you like to play again (y/n): ")
    if play_again != 'y':
        break
print("Thank you for playing!")


