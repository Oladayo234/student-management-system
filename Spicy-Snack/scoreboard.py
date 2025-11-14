first_grade = int(input("Enter score: "))
second_grade = int(input("Enter score: "))
third_grade = int(input("Enter score: "))

addition = first_grade + second_grade + third_grade
average = addition / 3

if(average >= 90):
    print('A')

elif(average >= 80):
    print('B')

elif(average >= 70):
    print('C')

elif(average >= 60):
    print('D')

else:
    print('F')

