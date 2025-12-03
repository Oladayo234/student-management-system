#create a loop to recieve two inputs
#sum the numbers and display them
#ask if user wants 



user_input_one = int(input("Enter a first number or 0 to stop: "))
user_input_two = int(input("Enter a second number or 0 to stop: "))

total = 0
counter =0

for number in range (0,10):

    addition_of_numbers = user_input_one + user_input_two
    total += addition_of_numbers

    print("sum of numberis: ", total)

#while counter != 0:
#    if user_input_one == 0 and user_input_two == 0:
#        break
#
#    addition_of_numbers = user_input_one + user_input_two
#    total += addition_of_numbers
#
#    user_input_one = int(input("Enter a number: "))
#    user_input_two = int(input("Enter a number: "))
#    counter += 1
#
#print("sum of number is: ", total)
