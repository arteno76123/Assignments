import random

try:
    students = int(input("Enter the number of students: "))
    questions = int(input("Enter the number of questions: "))
    
    while students > questions or students <= 0 or questions <= 0:
        print("You have entered incorrect number of students or questions. Try again.\n\n")
        students  = int(input("Enter the number of students  : "))
        questions = int(input("Enter the number of questions : "))
    
    student_list = [i+1 for i in range(students)]
    random.shuffle(student_list)
    
    question_list  = [i+1 for i in range(questions)]
    odd_questions  = question_list[::2] 
    even_questions = question_list[1::2]
    
    random.shuffle(odd_questions)
    random.shuffle(even_questions)
    
    question_list = odd_questions + even_questions
    
    # if the even-odd is not important, uncomment the line below
    # random.shuffle(question_list)
    
    # display the students
    question_pos = 0
    with open("output_questions.txt", "w", encoding = "utf-8") as output_file:
        for i in range(students):
            question = question_list.pop(-question_pos)
            print(f"{i:3}. student: {student_list[i]:3}, question: {question: 3}")
            output_file.write(f"{i:3}. student: {student_list[i]:3}, question: {question: 3}\n")
            
            # this calculation should keep alternating between 0  and 1 - with the minus in the pop() it should work
            question_pos = 1 - question_pos
    
except ValueError:
    print("You have entered a non-integer value. The program is about to stop ...")