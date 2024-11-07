#Initialize an empty list to store grades
grades = []

# Loop to get grades from the user
while True:
    grades_input = input("Enter grade of student (or type done finish): ")
    
    if grades_input.lower() == 'done': 
        break  # Exit the loop if the user types 'done'
    
    try: 
        grade = float(grades_input)  # Convert input to float 
        
        # Check of the grade is within the valid range 
        if 40 < grade < 100:
            grades.append(grade) # Add the grade to the list 
        else: 
            print("Please enter a grade between 40 and 100.")
    except ValueError:1
    print("Please enter a valid grade or 'done' to finish.")
        
# Calculate average grade
if grades: # Check if the grades list is not empty 
    average_grade = sum(grades) / len(grades) 
    print(f"/nAverage grade: {sum(grades)} / {len(grades)} = {average_grade:.2f}")
else: 
    print("No grades entered.")
    
# Calculate passing grades
passing_grade = 75
passed_students = [grade for grade in grades if grade > passing_grade]
num_passed = len[passed_students]
total_students = len[grades]

# Calculate and display passing percentage
if total_students > 0:
    passing_percentage = (num_passed / total_students) * 100 
    print (f"/nNumber of students passed: {num_passed} out of {total_students}")
    print (f"Passing percentage: {num_passed}/{total_students} = {passing_percentage:.2f}%")
else:
    print("No students to evaluatre")
    
    

        

        