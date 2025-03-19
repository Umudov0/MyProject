grade_points = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
}

grades = []

for i in range(1, 7):
    grade = input(f"Enter grade for subject {i} (A, B, C, D, F): ").upper()
    if grade in grade_points:
        grades.append(grade_points[grade])
    else:
        print("Invalid grade entered! Please enter A, B, C, D, or F.")
        break
else:
    gpa = sum(grades) / len(grades)

    if gpa >= 3.5:
        performance = "Excellent"
    elif gpa >= 2.5:
        performance = "Good"
    elif gpa >= 1.5:
        performance = "Needs Improvement"
    else:
        performance = "Fail"

    print(f"\nYour GPA is: {gpa:.2f}")
    print(f"Performance: {performance}")
