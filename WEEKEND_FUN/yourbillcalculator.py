total_bill = float(input("Enter bill: "))
membership = input("Do you have membership? ")

if total_bill >= 1000 and membership == "yes":
    print("You have 10% off" )

elif total_bill >= 1000 and membership == "no":
    print("You have 5% off")

else: 
    print("No discount. Your final bill is", total_bill) 



