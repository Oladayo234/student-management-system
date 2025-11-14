current_father_age = int(input("Enter father age: "))  
current_son_age  = int(input("Enter son age: "))

years_difference = 2 * current_son_age - current_father_age;

if(current_father_age > 80 or current_son_age > 80):
    print("OUT OF RANGE")
else: 
    print(years_difference, "years ago the father was twice the age of the son. " )
