user_input_one = int(input("Enter first Number: "))
user_input_two = int(input("Enter first Number: "))
user_input_three = int(input("Enter first Number: "))

addition_of_numbers = user_input_one + user_input_two + user_input_three
product_of_numbers = user_input_one * user_input_two * user_input_three
average_of_number = addition_of_numbers // 3

largerNumber = user_input_one
smallerNumber = user_input_one

if (user_input_two > largerNumber):
   largerNumber = user_input_two 

if (user_input_three > largerNumber):
   largerNumber = user_input_three 

if (user_input_two < smallerNumber): 
   smallerNumber = user_input_two 

if (user_input_three < smallerNumber):
   smallerNumber = user_input_three 

print("The sum of number is ",  addition_of_numbers)
print("The product of number is ",  product_of_numbers)
print("The average of number is ",  average_of_number)
print("The largest number ", largerNumber)
print("The Smallest number ", smallerNumber)
