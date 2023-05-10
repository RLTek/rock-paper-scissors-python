#A rock paper scissors game to help learn Python
import random

player_choice =  str(input("Choose rock, paper or scissors")).strip().lower()

def play_game():

    #lists the choices for the computer and picks a random one
    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)

    #prints the choices for the computer and player and reminds the player to choose rock, paper or scissors if they choose somethign else
    if player_choice != 'rock' and player_choice != 'paper' and player_choice != 'scissors':
        print('Invalid choice. Please try again and choose rock, paper or scissors.')
    else:
        print('You chose ' + player_choice.lower())
        print('Computron chose ' + computer_choice)

    #handles tie game
    if player_choice == computer_choice:
        print('Tie game! Play again!')

    #handles player choosing rock
    elif player_choice == 'rock' and computer_choice == 'paper':
        print('Paper covers rock! You lose!')
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print('Rock crushes scissors! You win!')
    
    #handles player choosing paper
    elif player_choice == 'paper' and computer_choice == 'rock':
        print('Paper covers rock! You win!')
    elif player_choice == 'paper' and computer_choice == 'scissors':
        print('Scissors cuts paper to shreds! You lose!')

    #handles player choosing scissors
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print('Scissors cuts paper to shreds! You win!')
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print('Rock crushes scissors! You lost!')


#starts the game by calling the function play_game
play_game()