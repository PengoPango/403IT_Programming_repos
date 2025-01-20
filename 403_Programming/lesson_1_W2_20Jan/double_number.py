def double_number(number):
    """
    This function takes a number as input and returns double its value.

    Parameters:
        number (int or float): The number to be doubled.

    Returns:
        int or float: The result of doubling the input number.
    """

    return number * 2

if __name__ == "__main__":
    while True: #Loop to allow recalling the function
        try:
            #Get input from the user
            user_input = input("Enter a number to double (or type 'exit' to quit: ")

            #Check if the user wants to exit
            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            #Convert input to a float and call the function
            number = float(user_input)
            result = double_number(number)
            print (f"The double of {number} is {result}")
        except ValueError:
            #Handle invalid input
            print("Please enter a valid number.")
