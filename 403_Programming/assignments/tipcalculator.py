#Student ID 15228802
print("""This is Ocean's Tip Calculator""")


#dictionary for menu list
menu = {
    'fries': 4,

    'cheeseburger': 7,

    'spaghetti': 12.49,

    'pizza': 10,

    'coffee': 2.75,

    'tea': 2.5
    }

print(f"\nHere is the menu to select your items for your order")

#empty list to be added to as your order
addedorder = []
#price for order
ordertotal = 0
while True:
    while True:
        try:
            #display the menu
            for item, price in menu.items():
                print ()
                print(f"""{item}: {price}
----------------------""")
                
            #ordering loop
            ordereditem = input("""Press 'f' to finish your order
What would you like to order? """)
            #makes it lowercase to accept any input
            ordereditem = ordereditem.lower()

            if ordereditem in menu:
                print (f"You have added {ordereditem} to your order")
                #adds menu item price to order price
                ordertotal += menu[ordereditem]
                #adds menu item to order list
                addedorder.append(ordereditem)
                #shows order and its price
                print (f"\nYour current order is {addedorder}")
                print ("Your bill is currently £",round(ordertotal, 2))

            #breaks the loop that asks for you order to continue onwards
            elif ordereditem == 'f':
                break
            else:
                #for incorrect inputs (mistypes of invalid options)
                print("This is not on the menu")
        #except block to complete loop       
        except:
            ValueError
            
    #tip calculator function
    def tipcalculator(ordertotal, tipamount):
        try:
            if tipamount not in ("5", "10", "20", "custom", "none"):
                raise CustomException("Not an option")
            elif tipamount == '5':
                return ordertotal * 1.05
            elif tipamount == '10':
                return ordertotal * 1.1
            elif tipamount == '20':
                return ordertotal * 1.2
            elif tipamount == 'custom':
                return (ordertotal * customamount/100) + ordertotal
            else:
                tipamount == 'none'
                return ordertotal * 1
        except ValueError:
            print("This is not an option")

    #prompts what option you will pick, recalls to the calculator
    print("\nYour final order is",addedorder, "and costs £",round(ordertotal, 2))

#while loop to repeatedly ask until a valid input is put in, breaks when valid input is put in, continuing code onwards
    while True:
        try:
            tipamount = input("""\nWould you like to add a tip?
5%, 10%, 20%, Custom, None
What would you like to tip: """)

            #makes word lowercase
            tipamount = tipamount.lower()

            #for if custom is picked
            if tipamount == 'custom':
                customamount = int(input("What % tip would you like to add: "))
                break
            #for other valid
            elif tipamount in ("5", "10", "20", "none"):
                break
            #for inputs that aren't valid
            elif tipamount not in ("5", "10", "20", "none"):
                print("This is not an option, If you wish to add a custom amount, choose the 'Custom' option")
        except ValueError:
            print("This is not an option, If you wish to add a custom amount, choose the 'Custom' option")
            
    #shows the result of the order with tip
    result = tipcalculator(ordertotal, tipamount)
    print ("\nYou have paid £",round(ordertotal, 2), "for the bill, You have paid overall £",round(result, 2))
    tiptotal = result-ordertotal
    print("You tipped £",round(tiptotal, 2), "Thank you for your purchase!")

    #added total and order blocks again to reset list after completion
    #empty list to be added to as your order
    addedorder = []
    #price for order
    ordertotal = 0

    repeat = input ("\nWould you like to order again? Yes/No :")
    #makes repeat lower, so capital  NO and YES accepted
    repeat = repeat.lower()
    
    #make process repeat to try order again
    if repeat == 'yes':
        continue
    elif repeat == 'no':
        break
    else:
        print("This is not an option")
