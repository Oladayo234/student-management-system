

user_input = int(input("Enter any number (Enter -1 to exit): "))

zero = 0
negative_number = 0
positive_number = 0

sentinel = -1

if  user_input == sentinel:
    print("Enter a number (Enter -1 to exit)")
    

while user_input != sentinel:
    
    user_input = int(input("Enter any number (Enter -1 to exit): "))

    if  user_input < 0:
        negative_number += user_input

    elif user_input > 0:
        positive_number += user_input

    elif user_input == 0:
        zero += user_input

print("Total Positive numbers are: ", positive_number)
print("Total Negative numbers are: ", negative_number)
print("Total zero numbers are: ", zero);

