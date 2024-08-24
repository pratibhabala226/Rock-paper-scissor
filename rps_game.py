import random

# Define the game choices
gameIcons = ['rock', 'paper', 'scissors']

# Main game loop
while True:
    try:
        userChoice = int(input('What is your choice? 0-rock, 1-paper, 2-scissors: '))
        if userChoice < 0 or userChoice > 2:
            raise ValueError("Invalid choice, please select 0, 1, or 2.")
    except ValueError as e:
        print(e)
        continue

    # Computer randomly selects a choice
    compChoice = random.choice([0, 1, 2])

    # Determine the outcome
    if userChoice == compChoice:
        print('It\'s a draw!')
    elif (userChoice == 0 and compChoice == 2) or (userChoice == 1 and compChoice == 0) or (userChoice == 2 and compChoice == 1):
        print('You win!')
    else:
        print('You lose!')

    # Display choices
    print(f'Computer chose: {gameIcons[compChoice]}')
    print(f'You chose: {gameIcons[userChoice]}')

    # Ask if the player wants to play again
    play_again = input('Do you want to play again? (y/n): ')
    if play_again.lower() != 'y':
        break

print('Thanks for playing!')
