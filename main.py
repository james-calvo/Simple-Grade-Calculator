def calculate_average(grades):
    return sum(grades) / len(grades)

def find_highest_grade(grades):
    return max(grades)

def find_lowest_grade(grades):
    return min(grades)

def count_grades_above_threshold(grades, threshold):
    return sum(1 for grade in grades if grade > threshold)

def get_student_grades():
    grades = []
    while True:
        grade_input = input("Enter student grade (type 'done' to finish): ")
        if grade_input.lower() == 'done':
            break
        try:
            grade = float(grade_input)
            grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a valid grade.")
    return grades

def display_menu():
    print("1. Calculate average grade")
    print("2. Find highest grade")
    print("3. Find lowest grade")
    print("4. Count grades above a threshold")
    print("5. Exit")

def handle_menu_choice(student_grades, choice):
    if choice == '1':
        print("Average Grade:", calculate_average(student_grades))
    elif choice == '2':
        print("Highest Grade:", find_highest_grade(student_grades))
    elif choice == '3':
        print("Lowest Grade:", find_lowest_grade(student_grades))
    elif choice == '4':
        threshold = float(input("Enter threshold: "))
        print("Number of Students with Grades Above", threshold, ":", count_grades_above_threshold(student_grades, threshold))
    elif choice == '5':
        print("Exiting program. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please enter a valid option.")

def main():
    # Get student grades from user input
    student_grades = get_student_grades()

    while True:
        # Display menu
        display_menu()

        # Get user choice
        choice = input("Enter your choice: ")

        # Handle user choice
        handle_menu_choice(student_grades, choice)

if __name__ == "__main__":
    main()
