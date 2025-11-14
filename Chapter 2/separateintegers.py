user_input = int(input("Enter first Number: "))

divide_one = user_input // 10000
divide_two = (user_input // 1000) %10
divide_three = (user_input // 100) % 10
divide_four = (user_input % 100) // 10
modulo_five= user_input % 10

result = divide_one,  divide_two,  divide_three,  divide_four,  modulo_five

print(result)


