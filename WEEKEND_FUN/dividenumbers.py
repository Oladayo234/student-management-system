first_user_input = int(input("Enter a number: "))
second_user_input = int(input("Enter a number: "))

division_of_numbers = first_user_input // second_user_input

if (second_user_input != 0):
    print("Answer equals to: ", division_of_numbers)

if (second_user_input == 0):
    print("cannot divide by zero")


