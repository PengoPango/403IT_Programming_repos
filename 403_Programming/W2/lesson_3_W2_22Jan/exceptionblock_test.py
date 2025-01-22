try:
    num = int(input("Enter a number that will divide 10: "))
    print(10 / num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")



try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
