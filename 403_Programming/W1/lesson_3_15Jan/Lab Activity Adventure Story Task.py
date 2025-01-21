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

grid0 = input (str("Choose. - "))

while not grid0.lower () == ("forwards"):
    try:
        grid0 = input (str("""You must continue forwards.
Choose. - """))
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

grid1 = input (str("Choose. - "))

while grid1.lower () == ("left"):
    try:
        grid1 = input (str("""You know this path will lead you astray,
You must choose another path onwards. - """))
    except when:
        grid1.lower () == ("forwards", "right")

if grid1.lower () == ("forwards"):
    print: grid4 == ("""\n You continue forwards, you immediately start to smell the stench of something burning,
you look onwards to find many people dying and dead, and those who are not, grieving,
these people were clearly just attacked, whether from the devils that wander,
or those who denounced everything, even their own humanity.

-----------------------------------------------------------------------------""")
    
#move onto grid 4, need to connect to grid 5(right) or 7(forwards)
#-------------------

if grid1.lower () == ("right"):
    print: grid2 == ("""\nYou continued on a path to your right,
you find a remnant of the old religion in a place to peak those who wander's attention,
it is surprising to you that any would still follow the Lord after he left us,
nonetheless it is  inviting survivors to find sanctuary at the chapel,
Maybe you could find some help or knowledge, the chapel must be nearby.

-----------------------------------------------------------------------------""")

#move onto grid 2, need to connect to grind 3(right) or 5(forwards)
#-------------------





