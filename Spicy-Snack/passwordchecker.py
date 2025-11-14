password = input("Enter number: ")
   
length = len(password)
   
if(length > 10):
    print("Strong Password")    

elif(length >= 10):
    print("medium Password")    

elif(length <= 6):
    print("weak Password")    

elif(length < 1):
    print("invalid Password")
