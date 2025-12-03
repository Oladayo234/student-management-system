count = 0
sentinel_value = -1
while count != sentinel_value:
    
    gallon_used = float(input("Enter the gallon used or -1 to end: "))
    miles_driven = float(input("Enter the miles driven or -1 to end: "))
    miles_per_gallon  = miles_driven / gallon_used

    
    print("Miles per gallon is : ",  miles_per_gallon);
