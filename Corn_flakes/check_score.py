student_score = int(input("Enter Score: "))

student_pass_mark = 45
failed_student = 0
passed_student = 0

for number in range (0,15):
    if student_score <= student_pass_mark:
        failed_student += 1
    if student_score > student_pass_mark:
        passed_student += 1

    student_score = int(input("Enter Score: "))

print(passed_student,"students passed")
print(failed_student,"students passed")
