import random


def r_p_s():
    ask = input("Do you wanna play a game? Yes or No: ").lower()
    player_wins = 0
    computer_wins = 0
    ties = 0
    while ask == "yes":
        rps = input("Okay, get ready! \nRock, Paper, Scissors! \nSelect attack: (r) for rock, (p) for paper, (s) for scissors: ").lower()
        
        computer = random.choice(["r", "p", "s"])
        choice = {"r": "Rock", "p": "Paper", "s": "Scissors"}

        if rps == computer:
            ties += 1
            print(f"You chose {choice[rps]}, Python chose {choice[computer]}, It's a Tie")
        elif (rps == "r" and computer == "s") or (rps == "p" and computer == "r") or (rps == "s" and computer == "p"):
            print(f"You chose {choice[rps]}, Python chose {choice[computer]}, You Win!")
            player_wins += 1
        else:
            print(f"You chose {choice[rps]}, Python chose {choice[computer]}, Python Wins!")
            computer_wins += 1

        ask = input("Do you wanna play again? Yes or No ").lower()
    print(f"Player Wins: {player_wins}   Computer Wins: {computer_wins}")
 
r_p_s()