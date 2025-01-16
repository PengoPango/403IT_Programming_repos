#-----------------------------------------------------------------------------
print ("""You are a child in a wartorn land,
Sin is more rampant than ever,
hellspawn hunt the man.
you were sent with your father to find some food and supplies.
you succeeding in finding food for your people,
but your father is dead.

You must find home.

-----------------------------------------------------------------------------""")

print ("""\nWhich way do you go?
Forwards.
Left.
Right.""")

grid0 = input (str("Choose."))

while not grid0.lower () == ("forwards"):
    try:
        grid0 = input (str("""You must continue forwards.
Choose."""))
    except:
        grid0.lower () == ("forwards")

if grid0.lower () == ("forwards"):
    print ("""\nYou continue forwards, leaving the corpse of your father,
you see a deep blistering wound from the beast that killed your father.
You feel sorrow as you looked at the emptiness in your fathers eyes
and dread at what may happen to you.

-----------------------------------------------------------------------------""")

print ("""\nYou continue onwards, you look upon a forsaken land,
there is nothing here but destruction and the dregs of hope.""")

print ("""\nWhich way do you go?
Forwards.
Left.
Right.""")
