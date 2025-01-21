
if __name__ == "__main__":
    while True:
        try:
            user_input = input (str("Will you give me your name? (Yes/No)"))

            if user_input.lower() == "no":
                print (str("Goodbye, Stranger! Have a great day!"))
                break

            elif user_input.lower() == "yes":
                name_input = input (str("What is your name?"))
                print (f"Hello!, {name_input}, Have a great day!")
                break

            elif not user_input.lower() == "":
                print("This is not an option")
                
        except ValueError:
            print ("There is a value error")
