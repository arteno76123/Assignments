try:
    # open the file
    with open("ordered_meals.txt") as source:
        
        # create an empty dictionary of meals
        # item structure > key: value --> meal_letter: number of orders
        orders = {}
        students = {}
        
        # read the file content
        for line in source:
            student_id, meal_code = line.split()
            
            # put the student to the dictionary
            # if the student is not in the dict, it will add him/her,
            # otherwise it should overwrite him/her and keep the most recent choice
            students[student_id] = meal_code
            
            # add the meal code to the orders
            # any meal present in the file ends up in the dictionary
            orders[meal_code] = 0
        
        # got through all students and get the meal ordered by the student - it will be added to the respective item
        for meal in students.values():
            orders[meal] += 1
        
        each_meal_ordered = True
        for meal in orders:
            print(f"{meal} has been ordered: {orders[meal]}x")
            if orders[meal] < 20:
                each_meal_ordered = False
                print("-->  This meal has been ordered less than 20-times")
            print("-" * 50)

        if each_meal_ordered:
            print("Each of the meal types has been ordered 20-times or more?")
        
    
except FileNotFoundError:
    print("The file is not available")
except Exception as unknown_error:
    print(f"An unexpected error has been detected - {unknown_error}.")
  