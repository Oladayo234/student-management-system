number_list = [1, 2, 30, 40, 50, 3, 5, 60, 70, 6]

counter = 0
largest_number = number_list[0]

for item in number_list:
    if item  > largest_number:
        largest = item
#        counter += 1

print("largest is: ", largest)
