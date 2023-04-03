import random

words = []
with open("vocab_learning.txt", "r", encoding="utf-8") as input_file:
    for line in input_file:
        words.append(line.strip())
        
slovak = words[::2]
english = words[1::2]

print("Choose the language you would like to practice the translation FROM:")
choice = input("Slovak --> enter SK, English --> enter EN:  ")

while choice not in ['SK', 'EN']:
    print("You have entered a wrong choice. Please, repeat the process.")
    print("Choose the language you would like to practice the translation FROM:")
    choice = input("Slovak --> enter SK, English --> enter EN:  ")
    
if choice == "SK":
    words_from = slovak
    words_to = english
else:
    words_from = english
    words_to = slovak

pairs = list(zip(words_from, words_to))
# The same as above could be achieved by the following code:
# pairs = []
# for i in range(len(words_from)):
#     pairs.append((words_from[i], words_to[i]))

# you could make a simple verification here, whether the number is in the required range - I was too lazy to add it ;-p    
count = int(input(f"Enter the number of words to be tested (between 1 and {len(slovak)}):"))

tested = []
for i in range(count):
    tested.append(pairs.pop(random.randint(0,len(pairs))))

wrong = []
correct = incorrect = 0

for pair in tested:
    answer = input(f"Translate: {pair[0]}: ")
    if answer == pair[1]:
        print("CORRECTO UZASNO!")
        correct += 1
    else:
        print("TA TO CO TO?")
        wrong.append(pair)
        incorrect += 1

print(f"You score: {correct} correct answers, {incorrect} incorrect answers.")
with open("wrong_answers.txt", "w", encoding="utf-8") as output_file:
    for pair in wrong:
        output_file.write(f"{pair[0]} --> {pair[1]}\n")
