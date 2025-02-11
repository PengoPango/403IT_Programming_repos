
def calculator(n1, operator, n2):
    try:
        if operator not in ("+", "-", "/", "*"):
            raise CustomException("Invalid operator")
        if operator == '+':
            return n1+n2
        elif operator == '-':
            return n1-n2
        elif operator == '/':
            return n1/n2
        elif operator == '*':
            return n1*n2
        else:
            return ("Invalid operator")
    except ZeroDivisionError:
        return "Divsion by 0 is not allowed"

#loop
while True:
    try:
        n1 = (float(input("Enter the first number")))

        operator = (input("Enter operation (+, -, /, *):"))

        n2 = (float(input("Enter the second number")))

        result = calculator(n1, operator, n2)
        print (f"Result: {result}"),
    
    except ValueError:
        print("You must put a number")

    cont = input("Do you want to continue again? (yes/no)").lower()
    if cont != 'yes':
        print("Goodbye!")
        break

