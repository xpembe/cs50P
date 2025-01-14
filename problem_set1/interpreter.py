# Asking for the expression from the user
expression: list = input("Expression: ").strip().split(" ")

# unpack the expression values to an appropriate variables
num1: float = float(expression[0])
num2: float = float(expression[-1])
operator: str = expression[1]

# Checking for the operation to be done
if operator == "+":
    print(f"{(num1 + num2):.1f}")

if operator == "-":
    print(f"{(num1 - num2):.1f}")

if operator == "*":
    print(f"{(num1 * num2):.1f}")

if operator == "/":
    print(f"{(num1 / num2):.1f}")
