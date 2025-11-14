
first_user_input = int(input("Enter first number: "))
arithmetic_operator = input("Enter an arithmetic sign: ")
second_user_input = int(input("Enter second number: "))
  

addition= first_user_input + second_user_input;
subtraction = first_user_input - second_user_input;
product = first_user_input * second_user_input;
division = first_user_input // second_user_input;

    
if(arithmetic_operator == '+'):
      print(addition)
if(arithmetic_operator == '-'):
      print(subtraction)
if(arithmetic_operator == '*'):
      print(product);
if(arithmetic_operator == '//'):
      print(division);

