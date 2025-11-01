import math

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a*b
def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error! You cannot divide by Zero!"
def expo(a, b):
    return a**b
def sqrt(a):
    return math.sqrt(a)


operators = { 
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
    "^": expo,
    "~": sqrt
}

def main():
    print("Hello and welcome to your handy-dandy calculator.\nPress ""q"" to exit if you're finished.")

    choice = 0
    while True:
        print("Please choose one of the following:\n+: Addition\n-: Subtraction\n*: Multiplication\n/: Division\n^: Exponents\n~: Rooting")
        choice = input().strip().lower()

        if choice == "q":
            break
        
        if choice not in operators:
            print("Invalid operator! Please try again.")
            continue

        

        if choice == "~":
            num = input("What number would you like to find the square root of?\n")
            try:
                num = float(num)
                result = sqrt(num)
                print("The square root of:", num, "is", result)
            except ValueError:
                print("Invalid input! Please try again.")
                continue
        
            while True:
                dec = input("\nWould you like to continue?\nYes\nNo\n")
                if dec.strip().lower() == "yes":
                    break
                elif dec.strip().lower() == "no":
                    return
                else:
                    print("Invalid input, please try again!\n")

            continue

        num1 = input("What is your first number?\n")    
        num2 = input("What is your second number?\n")

        try:
            num1, num2 = float(num1), float(num2)
            result = operators[choice](num1, num2)
            print("Calculator print!\nYour result is: ", result)
        except ValueError:
            print("Invalid input, please try again.\n")
        except Exception as e:
            print(f"Error: {e}")

        while True:
            dec = input("\nWould you like to continue?\nYes\nNo\n")
            if dec.strip().lower() == "yes":
                break
            elif dec.strip().lower() == "no":
                return
            else:
                print("Invalid input, please try again!\n")


main()
print("Thank you! Have a good day.")
        

