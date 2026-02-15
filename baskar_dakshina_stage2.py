"""
Calculator with Result Check (Stage 2)
- Extends Stage 1
- After computing, print whether the result is Positive, Negative, or Zero
"""

def classify_result(value: float) -> str:
    if value > 0:
        return "Positive"
    elif value < 0:
        return "Negative"
    else:
        return "Zero"

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

        print(f"Result = {result}")
        print(classify_result(result))

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()