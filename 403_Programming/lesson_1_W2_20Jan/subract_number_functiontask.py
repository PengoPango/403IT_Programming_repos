def subract_numbers (a, b):

    return a - b

if __name__ == "__main__":
    while True:
        try:
            input_a = (int(input("Enter the first number:")))
            input_b = (int(input("Enter the second number:")))
            a = (int(input_a))
            b = (int(input_b))
            result = (a - b)
            print (f"the result of {a} subract {b} is {result}")
            break

        except ValueError:
            print("Please enter a valid number")
            

            

        

    
