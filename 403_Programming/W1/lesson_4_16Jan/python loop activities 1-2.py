print ("Activity 1, print odd numbers 1 to 15")
i = 1

while i <= 15:
    print (i)
    i += 2

e = 3
j = 1

#--------

print ("\nActivity 2, print multiples of 3")

while j <=10:
    print (f"{j*e}", end = (""))
    j += 1
    print ()

#--------
    
print ("\nActivity 3, While loop, countdown from 10 to 1")
f = 10

while f >= 1:
    print (f)
    f -= 1
    if f == 0:
        print ("Blast off!")

#---------
        
print ("\nActivity 4, For Loop, Reserve a string")

string = ("Python")
reversed_string = ("")

for char in string:
    reversed_string = char + reversed_string

print (reversed_string)

#----------

print ("\nStretch Activity 1: Creat a pyramid with numbers")

j = ""

for i in range (1, 6):
    j += (str(i))
    print (j)
