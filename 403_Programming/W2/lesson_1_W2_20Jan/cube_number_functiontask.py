def cube_number(number):

    return number ** 3

if __name__ == "__main__":
    while True:
        try:
            inputnumber = (int(input("Enter a number to be cubed")))
            number = (int(inputnumber))
            result = (number ** 3)
            print (f"The result of {number} cubed is {result}")
            break

        except ValueError:
            print("Please enter a valid number")


def square_number(number):

    return number ** 2

if __name__ == "__main__":
    while True:
        try:
            inputnumber = (int(input("Enter a number to be squared")))
            number = (int(inputnumber))
            result = (number ** 2)
            print (f"The result of {number} squared is {result}")
            break

        except ValueError:
            print("Please enter a valid number")
