print("""This is Ocean's Palindrome Checker,
This Checker only accepts letter
numbers and special characters are removed""")
while True:
    while True:
        try:
            #input word to be reversed
            word = input(str("""\npress 'q' to quit
What word would you like to test :"""))

            #makes capitals into lower case
            word = word.lower()


            for letter in word:

                #if there is a space as a character, replaces space with void
                if letter in " ":
                    word=word.replace(letter,'')

                     
            #catalogue to remove special characters, punctuation, spaces
            for letter in word:

                #if any other invalid characters prints its an invalid input and doesnt reverse
                if letter not in "abcdefghijklmnopqrstuvwxyz":
                    word = "Invalid Input"
         
        finally:
            if word == 'q':
                print("\nGoodbye!")
                quit()

            #where invalid character, word is defined as invalid input, if word is invalid input,
            #it breaks the process and doesnt check if its a palindrome
            if word == "Invalid Input":
                print("This is not a valid input")
                break
            
            #code to reverse word
            reversed_word = word[::-1] #reverses order of a string, slices from the first to last character in string
            print (f"This is {word} reversed: {reversed_word}")
            #how the script checks if it is/isn't a palindrome
            if word == reversed_word:
                print("\nThis is a palindrome")
            else:
                print ("\nThis is not a palindrome")



