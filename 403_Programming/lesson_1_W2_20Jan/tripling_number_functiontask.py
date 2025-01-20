def triple_number(number):
    """
    This function takes a number as input and returns tripled its value.

    Parameters:
        number (int or float): The number to be tripled.

    Returns:
        int or float: The result of tripling the input number.
    """

    return number * 3

if __name__ == "__main__":
    while True: #Loop to allow recalling the function
        try:
            #Get input from the user
            user_input = input("Enter a number to triple (or type 'exit' to quit: ")

            #Check if the user wants to exit
            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            #Convert input to a float and call the function
            number = float(user_input)
            result = triple_number(number)
            print (f"The triple of {number} is {result}")
        except ValueError:
            #Handle invalid input
            print("Please enter a valid number.")

