user_input_one = int(input("Enter first number: "))
user_input_two = int(input("Enter second number: "))
user_input_three = int(input("Enter third number: "))

largerNumber = user_input_one

if (user_input_two > user_input_three and largerNumber):
   largerNumber = user_input_two 

if (user_input_three > user_input_two and largerNumber):
   largerNumber = user_input_three 

print("The largest number ", largerNumber)

