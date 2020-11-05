from random import randint

command = " "

while command != "exit" :

    command = input("Your turn player 1\n>").lower()

    #ecolhe um número de 1 a 3
    #cada número representa uma jogada diferente
    # 1 - rock, 2 - paper, 3 - scisors
    computer = randint(1,3) 

    if computer == 1:
        computer = "rock"
    elif computer == 2:
        computer = "paper"
    else:
        computer = "scissors"


    if command == computer:
        print(f"computer plays " + computer)
        print("It's a tie")
    elif command == "rock":
        print(f"computer plays " + computer)
        if computer == "paper":
            print("computer wins")
        elif computer == "scissors":
            print("player 1 wins")

    elif command == "paper":
        print(f"computer plays " + computer)
        if computer == "scissors":
            print("computer wins")
        elif computer == "rock":
            print("player 1 wins")

    elif command == "scissors":
        print("computer plays " + computer)
        if computer == "rock":
            print("computer wins")
        elif computer == "paper":
            print("player 1 wins")
        print()
    else:
        if command != "exit" :
            print("command Not valid")
            continue
    
    computer = randint(1,3) 

print("Thanks for playing!")