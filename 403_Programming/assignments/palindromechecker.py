while True:
    try:
        #input word to be reversed
        word = input(str("""\npress 'q' to quit
What word would you like to test :"""))

        #makes capitals into lower case
        word = word.lower()           
    
        #catalogue to remove special characters, punctuation, spaces
        for letter in word:
            if letter not in "abcdefghijklmnopqrstuvwxyz":
                word=word.replace(letter,'')
    finally:
        if word == 'q':
            print("Goodbye!")
            break
        
        #code to reverse word
        reversed_word = word[::-1]
        print (f"This is {word} reversed: {reversed_word}")

        #how the script checks if it is/isn't a palindrome
        if word == reversed_word:
            print("\nThis is a palindrome")
        else:
            print ("\nThis is not a palindrome")


