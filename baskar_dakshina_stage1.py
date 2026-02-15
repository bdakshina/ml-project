"""
Basic Calculator (Stage 1)
Requirements:
- Take two numbers and an operator (+, -, *, /)
- Use if-elif-else
- Handle division by zero
"""

def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ").strip()

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = a / b
        else:
            print("Invalid operator. Use one of +, -, *, /")
            return

        # Output format per requirement
        print(f"Result = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()