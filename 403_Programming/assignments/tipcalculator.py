#Student ID 15228802
print("""This is Ocean's Tip Calculator""")


#class for menu list
menu = {
    'fries': 4,

    'cheeseburger': 7,

    'spaghetti': 12.5,

    'pizza': 10,

    'coffee': 2.5,

    'tea': 2
    }

print(f"\nHere is the menu to select your items for your order")

#empty list to be added to as your order
addedorder = []
ordertotal = 0

#display the menu
for item, price in menu.items():
    print(f" {item}: {price}")
    
#ordering loop
ordereditem = input("What would you like to order? ")

if ordereditem in menu:
    print (f"You have added {ordereditem} to your order")
    ordertotal += menu[ordereditem]
    print (f"Your bill is currently £{ordertotal}")
else:
    print("This is not on the menu")
    
