user_input_one = int(input("Enter a number: "))

#integer-division = user_input_one // 2
#integer-modulo = user_input_one % user_input_one

for number in range (2,user_input_one):

    if user_input_one % 2 == 0:
        print(user_input_one ,"is not a prime number")
        break

    else:
        print(user_input_one ,"is a prime number")


