guess_number = int(input("Enter a number: "))

fixedNumber = 100

while guess_number != fixedNumber:
        
    if guess_number > fixedNumber:
        print("Too high! Try again")

    elif guess_number < fixedNumber:
        print("Too low! Try again")

    elif guess_number == fixedNumber:
        print("you are correct")

    guess_number = int(input("Enter a number: "))
print("The value is",fixedNumber,"You won")
