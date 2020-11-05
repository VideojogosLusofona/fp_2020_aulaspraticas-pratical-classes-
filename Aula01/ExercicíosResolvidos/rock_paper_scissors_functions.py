from random import randint

'''
Autor:  Fernando Manuel Soares
NOTAS:  Código não comentado propositadamente,
        irá posteriormente ser usado para fazer revisão
        de docstrings na aula prática 2
'''

command = ""
valid_comands = ("rock", "paper", "scisors", "exit")
computer_command = ""


def computer_hand():
    r = randint(1, 3)

    if r == 1:
        return "rock"
    elif r == 2:
        return "paper"
    else:
        return "scissors"


def check_winner():

    if command == computer_command:
        return "Both - Game ends in a tie"

    elif command == "rock":
        if computer_command == "paper":
            return "Computer"
        return "Player 1"

    elif command == "paper":
        if computer_command == "scissors":
            return "Computer"
        return "Player 1"

    elif command == "scissors":
        if computer_command == "rock":
            return "Computer"
        return "Player 1"


while command != "exit":
    print("__________________")
    command = input("Your turn player 1\n>").lower()

    if command not in valid_comands:
        print("Command not Valid")
        continue

    if command == "exit":
        print("Thanks for Playing!")
        break

    computer_command = computer_hand()
    
    print("Player 1 plays: " + command)
    print("Computer plays: " + computer_command)

    print("Winner: " + check_winner())
   