#1. Rock beats Scissors looses to Paper
#2. Paper beats Rock but looses to Scissors
#3. Scissors beats Paper but looses to Rock

player_one = input("Choose between rock, paper and scissors: ")
player_two = input("Choose between rock, paper and scissors: ")

rock = 'rock'
paper = 'paper'
scissors = 'scissors'

if player_one == rock and player_two == scissors:
    print("rock wins")

elif player_one == paper and player_two == rock:
    print("paper wins")

elif player_one == scissors and player_two == paper:
    print("scissors wins")

if player_two == rock and player_one == scissors:
    print("rock wins")

elif player_two == paper and player_one == rock:
    print("paper wins")

elif player_two == scissors and player_one == paper:
    print("scissors wins")

else: print("Invalid entry")



