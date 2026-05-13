
arr1 = [[2,3], [3,2]]
arr3 = [1,2,3,4,5]
arr2 = [[2,4,5], [3,3,5], [6,4,1]]

def perfect_square (number):
    sumOfRow = []
    sumOfColumn = []

    for count in range (len(number)):
        row = 0
        column = 0
        for index in range (len(number)):
            row += number[count][index]
            column += number[index][count]
        sumOfRow.append(row)
        sumOfColumn.append(column)

    all_sums = sumOfRow + sumOfColumn

    if len(set(all_sums)) == 1:
        return True
    else:
        return False
 
print(perfect_square(arr1))
print(perfect_square(arr2))
