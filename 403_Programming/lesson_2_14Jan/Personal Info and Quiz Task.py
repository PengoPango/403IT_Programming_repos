name = input("What is your name?")
surname = input ("What is your surname")
age = int(input("How old are you?"))


print ("My name is", name, "\nI am here!", "\nMy surname is", surname, "\nI am",age, "years old and will be", age+1, "next.")

print ("\n\n Next we will ask you some questions")

print ("\nWhat is the purpose of the 'input ()' function in Python?")

print("a)To print data to the screen"
"\nb)To collect user input"
"\nc)To calculate a mathematical result"
"\nd)To store a variable's value")

Q1 = input (str("Which is correct?"))

if Q1.lower()==("b"):
    print ("Correct!")
else:
    print ("Incorrect!")

print ("\nWhich of the following is the correct syntax to convert a string input to an integer in Python?")

print("a)'int (input())'"
"\nb)'str (input())'"
"\nc)'bool (input())'"
"\nd)'float (input())'")

Q2 = input (str("Which is correct?"))

if Q2.lower()==("a"):
    print ("Correct!")
else:
    print ("Incorrect!")

print("\nWhat does the 'bool ()' function do in Python?")

print("a)Converts input into a string"
"\nb)Converts input into boolean (T/F)"
"\nc)Converts input into an integer"
"\nd)Converts input into a float")

Q3 = input (str("Which is correct?"))

if Q3.lower()==("b"):
    print ("Correct!")
else:
    print ("Incorrect!")

print ("\nHow do you correctly print a message in Python, combining a string and a variable?")

print("a)'print('Hello'+name)'"
"\nb)'print('Hello' name)'"
"\nc)'print('hello,name')'"
"\nd)'print('Hello',name)'")

Q4 = input (str("Which is correct?"))

if Q4.lower()==("d"):
    print ("Correct!")
else:
    print ("Incorrect!")

input("""\n Congrats on completing the quiz!
What did you get?""")
