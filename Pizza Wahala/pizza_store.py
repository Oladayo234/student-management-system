import math
print("""    
        Hello,
        
                        Welcome to Iya Scambirah Pizza joint

       *********************************MENU********************************
       =====================================================================
       |                      |                     |                      |
       |Pizza Type            | Number of Slices    |Price per Box         |
       =====================================================================
       |                      |                     |                      |
       |Sapa Size             |4                    |2,000                 |
       =====================================================================
       |                      |                     |                      |
       |Small Money           |6                    |2,400                 |
       =====================================================================
       |                      |                     |                      |
       |Big Boys              |8                    |3,000                 |
       =====================================================================
       |                      |                     |                      |
       |Odogwu                |12                   |4,200                 |
       =====================================================================



        """)

number_of_guest = int(input("Enter number of guest: "))
pizza_type = input("Enter pizza type: ").lower().strip()

#number_of_slices= 0
#price_per_box = 1
#number_of_boxes = 1
#remainder = 1
#price = 1
#total = 1

if pizza_type == "sapa size":
    number_of_slices = 4
    price_per_box = 2000

elif pizza_type == "small money":
    number_of_slices = 6
    price_per_box = 2400

elif pizza_type == "big boys":
    number_of_slices = 8
    price_per_box = 3000

elif pizza_type == "odogwu":
    number_of_slices = 12
    price_per_box = 4200

number_of_boxes = math.ceil(number_of_guest / number_of_slices)
remainder = (number_of_slices * number_of_boxes) - number_of_guest
price = price_per_box * number_of_boxes
total = number_of_boxes * number_of_slices


print(f"price = {price}. {price_per_box} per box for {number_of_boxes} boxes.")

print(f"Total slice: {total}. Remaining slices: {remainder} ")

print(f"{pizza_type} pizza contains {number_of_slices} per box. {number_of_boxes} boxes should be sufficient for {number_of_guest} people as it would contain {total} slices in all")





