
    
weight = int(input("Enter your weight in kilograms: "));
    
height = int(input("Enter your height in kilograms: "));
    
bmi = weight / height * height

if (bmi <= 18.5):
    print("You are Underweight")
     
elif (bmi <= 25.0):
    print("You are Normal");
     
elif (bmi <= 30.0):
    print("You are Overweight")
     
else:
    print("You are Obese")
     
   

