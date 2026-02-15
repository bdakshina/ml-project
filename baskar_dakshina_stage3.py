"""
Student Grade Calculator (Stage 3)
Input: Student name, 3 subject marks (0-100)
Compute: Total, Percentage, Grade
Grades:
A: >= 75%
B: >= 60%
C: >= 40%
F: < 40%
"""
from typing import Tuple

def compute_total_percentage(m1: float, m2: float, m3: float) -> Tuple[float, float]:
    total = m1 + m2 + m3
    percentage = (total / 300) * 100
    return total, percentage

def grade_from_percentage(p: float) -> str:
    if p >= 75:
        return "A"
    elif p >= 60:
        return "B"
    elif p >= 40:
        return "C"
    else:
        return "F"

def validate_mark(x: float) -> bool:
    return 0 <= x <= 100

def main():
    name = input("Enter student name: ").strip()

    try:
        m1 = float(input("Enter mark 1 (0-100): "))
        m2 = float(input("Enter mark 2 (0-100): "))
        m3 = float(input("Enter mark 3 (0-100): "))
    except ValueError:
        print("Invalid input. Marks must be numbers.")
        return

    # Validate marks
    if not (validate_mark(m1) and validate_mark(m2) and validate_mark(m3)):
        print("Error: Each mark must be between 0 and 100.")
        return

    total, percentage = compute_total_percentage(m1, m2, m3)
    grade = grade_from_percentage(percentage)

    # Output formatting as per example
    print(name)
    print(f"Total: {int(total)}/300" if total.is_integer() else f"Total: {total}/300")
    # Show percentage with one decimal like example (80.0%)
    print(f"Percentage: {percentage:.1f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()