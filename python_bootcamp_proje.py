import random


def tas_kagit_makas_beyza_avci():
    print("Welcome to the Rock, Paper, Scissors Game!")
    print("Rules of the game: Rock beats paper. Paper beats scissors. Scissors beats stone.")

    number_games = 0
    gamer_point = 0
    computer_point = 0
    options = ["rock", "paper", "scissors"]

    while True:
        number_games += 1
        gamer_point = 0
        computer_point = 0

        print(f"\nGame {number_games} has started!")

        while gamer_point < 2 or computer_point < 2:
            print(options)
            gamer_selected = input("Choose one of 3 options: ")
            print('*' * 40)

            if gamer_selected not in options:
                print("Invalid selection! Please try again.")
                print('#' * 40)
                continue

            computer_selected = random.choice(options)
            print(f"Selection of computer: {computer_selected}")
            print(f"Your choice: {gamer_selected}")

            if gamer_selected == computer_selected:
                print('Tie! Both players chose the same action.')
            elif gamer_selected == 'paper' and computer_selected == 'rock':
                print('You won this round.')
                gamer_point += 1
            elif gamer_selected == 'paper' and computer_selected == 'scissors':
                print('The computer won this round.')
                computer_point += 1
            elif gamer_selected == 'scissors' and computer_selected == 'rock':
                print('The computer won this round.')
                computer_point += 1
            elif gamer_selected == 'scissors' and computer_selected == 'paper':
                print('You won this round.')
                gamer_point += 1
            elif gamer_selected == 'rock' and computer_selected == 'paper':
                print('The computer won this round.')
                computer_point += 1
            elif gamer_selected == 'rock' and computer_selected == 'scissors':
                print('You won this round.')
                gamer_point += 1

            print(f"Score: Gamer {gamer_point} - Computer {computer_point}")
            print('#' * 40)

            if gamer_point == 2:
                print("Congratulations! You won the game!")
                print('#' * 40)
                break
            elif computer_point == 2:
                print("Unfortunately, the computer won the game!")
                print('#' * 40)
                break

        gamer_continue_answer = input("Do you want to play another game? (y/n): ")
        if gamer_continue_answer != 'y':
            print("Game over!")
            break

        computer_continue_answer = random.choice(['y', 'n'])
        if computer_continue_answer != 'y':
            print("The computer does not want to continue the game. Game over!")
            break


tas_kagit_makas_beyza_avci()
