total_bill = float(input("Enter bill: "))
membership = input("Do you have membership? ")

is_member = 0.10
not_member = 0.05

memberhip_discount = total_bill - (total_bill * is_member)
not_member_discount = total_bill - (total_bill * not_member)

if total_bill >= 1000 and membership == "yes":
    print("your total is: ", memberhip_discount )

elif total_bill >= 1000 and membership == "no":
    print("your total is: ", not_member_discount)

else: 
    print("your total is: ", total_bill) 



