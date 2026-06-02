def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("❌ Invalid input! Please enter a number.")


def calculator():
    print("\n🧮 Welcome to Advanced Calculator")

    result = None  # stores previous result

    while True:
        print("\n===== MENU =====")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (^)")
        print("6. Modulus (%)")
        print("7. Exit")

        choice = input("Choose operation (1-7): ")

        if choice == '7':
            print("👋 Exiting Calculator...")
            break

        if choice not in ['1','2','3','4','5','6']:
            print("❌ Invalid choice!")
            continue

        # Ask if user wants to continue with previous result
        if result is not None:
            use_prev = input(f"👉 Use previous result ({result})? (y/n): ").lower()
            if use_prev == 'y':
                num1 = result
            else:
                num1 = get_number("Enter first number: ")
        else:
            num1 = get_number("Enter first number: ")

        num2 = get_number("Enter second number: ")

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = power(num1, num2)
        elif choice == '6':
            result = modulus(num1, num2)

        print(f"✅ Result: {result}")


# Run program
calculator()