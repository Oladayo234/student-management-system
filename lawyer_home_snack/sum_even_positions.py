number_list = [1, 2, 30, 40, 50, 3, 5, 60, 70, 6]

sum_of_positions = 0

for index, item, in enumerate(number_list):
    if index % 2 == 0:
        sum_of_positions = sum_of_positions + item
        print(sum_of_positions)
