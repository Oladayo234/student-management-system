correct_password = login
counter = 0
password = input("Enter password: ")

while password != correct_password:
    password = input("Enter password: ")

    if(password != correct_password):
        print("Enter password")  
    else: print("login sucessful")
#counter++


print("you have succesfully logged in")
