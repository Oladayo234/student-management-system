user_input = int(input("Enter Number: "))

addition_of_numbers = 0

addition_of_numbers = user_input
product_of_numbers = user_input
average_of_numbers = user_input

larger_number = user_input
smaller_number = user_input

for integer in range (3):
    
    user_input = int(input("Enter Number: "))
 
    addition_of_numbers += user_input
    product_of_numbers *= user_input
    average_of_numbers = addition_of_numbers / 4

    if (user_input > larger_number):
        larger_number = user_input 

    if (user_input < smaller_number):
        smaller_number = user_input 
    
print("The sum of number is ",  addition_of_numbers)
print("The product of number is ",  product_of_numbers)
print("The average of number is ",  average_of_numbers)
print("The largest number ", larger_number)
print("The Smallest number ", smaller_number)
