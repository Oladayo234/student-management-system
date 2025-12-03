number_list = [1, 2, 30, 40, 50, 3, 5, 60, 70, 6]

sum_of_positions = 0
average_of_list = 1
counter = 0

for item in number_list:
    counter += 1
    sum_of_positions += item

average_of_list = sum_of_positions / counter
print("Average is: ", average_of_list)
