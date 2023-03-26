import random

students = int(input("Input the number of students: "))
questions = int(input("Input the number of questions: "))

if questions > students:
    student_nums = list(range(1, students+1))
    random.shuffle(student_nums)

    question_numbers = []
    # If you do not want to alternate the questions, then 
    # comment out the lines that create the even_questions and odd_questions lists shown with # after the code,
    # then uncomment: question_numbers = list(range(1, questions+1)) => specified above the code itself

    ###################################################
    if questions % 2 == 0:
        even_questions = list(range(2, questions+1, 2))
        odd_questions = list(range(1, questions+1, 2))
    else:
        even_questions = list(range(2, questions, 2))
        odd_questions = list(range(1, questions+1, 2))
    random.shuffle(even_questions)
    random.shuffle(odd_questions)
    question_numbers.extend(odd_questions)
    question_numbers.extend(even_questions)
    #####################################################

    ################################################
    # uncomment the line below for not alternatingg
    # question_numbers = list(range(1, questions+1))
    ################################################
    assignments = {}

    for i in range(students):
        if i % 2 == 0:
            # for sudá questions
            question_num = question_numbers.pop(0)
        else:
            # for lichá questions
            question_num = question_numbers.pop(1)

        assignments[student_nums[i]] = question_num

    print("The order of students and their assigned questions:")
    for student_num, question_num in assignments.items():
        print(f"student: {student_num}, question: {question_num}")

    with open("assignments.txt", "w") as file:
        for student_num, question_num in assignments.items():
            file.write("Student: " + str(student_num) + ", Question: " + str(question_num) + "\n")
else:
    print("Enter more questions for the students, please.")
