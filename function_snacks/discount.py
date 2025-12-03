def discount (item, price, code):

    if code.upper() == "SAVE10":
        discount_price  = 0.10 * price 
        print(discount_price)

    elif code.upper() =="HALFOFF":
        discount_price =  0.50 * price 
        print (discount_price)

    else:
        print("no valid code apply, no code")
        print(price)

discount ("bread", 5000, "HALFOFF")





   



