import copy

# Define a function to display student information
def display_students(students):
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}")

# Create a list of students
student1 = {'name': 'Alice', 'age': 20}
student2 = {'name': 'Bob', 'age': 21}
student3 = {'name': 'Charlie', 'age': 19}

students = [student1, student2, student3]

# Display the original list of students
print("\nOriginal Students:")
display_students(students)

# Create a shallow copy of the list of students
shallow_copy = students

# Display the shallow copied student list
print("\nShallow Copied Students:")
display_students(shallow_copy)

# Modify a student's name in the shallow copied list
shallow_copy[0]['name'] = 'Alicia'

# Add a new student to the shallow copied list
shallow_copy.append({'name': 'David (Shallow)', 'age': 22})

# Display the modified shallow copied student list
print("\nModified Shallow Copied Students:")
display_students(shallow_copy)

# Display the original student list
print("\nOriginal Students (changed by shallow copy):")
display_students(students)  # The original list remains unchanged

# Create a deep copy of the original list of students
deep_copy = copy.deepcopy(students)

# Display the deep copied student list
print("\nDeep Copied Students:")
display_students(deep_copy)

# Modify a student's name in the deep copied list
deep_copy[1]['name'] = 'Bobby'
deep_copy.pop(-1)   # Removed the last element details

# Add a new student to the deep copied list
new_student_deep = {'name': 'Eva (Deep)', 'age': 23}
deep_copy.append(new_student_deep)

# Display the modified deep copied student list
print("\nModified Deep Copied Students:")
display_students(deep_copy)

# Display the original student list
print("\nOriginal Students (unchanged by deep copy):")
display_students(students)
