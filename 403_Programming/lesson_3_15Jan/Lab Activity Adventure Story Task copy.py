#-----------------------------------------------------------------------------

#game catalogue

location = {



  'grid0': {
        "description": """\nYou are stood, looking upon the traces of your father,
there is no point spending more time here.

You must continue forwards.""",
        "choices": {
            "1": "Forwards"
        },
        "paths": {
            "Forwards": 'grid1'
        },
    },
      
#forward goes to grid1, no other directions
    
    'grid1': {
        "description": """\nYou continue onwards, leaving the corpse of your father,
you see a deep blistering wound from the beast that killed your father.
You feel sorrow as you looked at the emptiness in your fathers eyes
and dread at what may happen to you,
you look upon a forsaken land,
there is nothing here but destruction and the dregs of hope.

Which way do you go?""",
        "choices": {
            "1": "Upwards",
            "2": "Left",
            "3": "Right"
            },
        "paths": {
            "Upwards": 'grid4',
            "Left": 'N/A',
            "Right": 'grid2'
            },
        },

  'grid1nofather': {
      "description": """\nyou look upon a forsaken land,
there is nothing here but destruction and the dregs of hope.

Which way do you go?""",
       "choices": {
            "1": "Upwards",
            "2": "Left",
            "3": "Right"
            },
        "paths": {
            "Upwards": 'grid4',
            "Left": 'N/A',
            "Right": 'grid2'
            },
        },
      
#upwards goes to grid 4, left is no accepted, right goes to grid2
    
    'grid2': {
        "description": """\nYou continued onwards,
you find a remnant of the old religion in a place to peak those who wander's attention,
it is surprising to you that any would still follow the Lord after he left us,
nonetheless there is a sign pinned to the remnant,
inviting survivors to find sanctuary at the chapel,
Maybe you could find some help or knowledge, the chapel must be nearby.

Which way do you go?""",
        "choices": {
            "1": "Upwards", 
            "2": "Left",
            "3": "Right"
            },
        "paths": {
            "Upwards": 'grid5',
            "Left": 'grid1',
            "Right": 'grid3'
            },
        },
#ppwards goes to grid3, left goes to grid5, right is no accepted

    'grid3': {
        "description": """\nYou find yourself at a chapel,
the area is adorned with crosses and other religious depictions,
seemingly in a way to ward demons away.
There is corpses of monsters littering the location close to the church.
Your eyes move along the location to the chapel entrance,
there is an open gate, you see a lonesome priest through the gateway distracted in prayer.

Do you enter the chapel?""",
        "choices": {
            "1": "Ignore the chapel",
            "2": "Enter the chapel"
            },
        "paths": {
            "Ignore the chapel": 'grid3ignore',
            "Enter the chapel": 'grid3enter'
            },
        },

#options for talking to priest need coding in
    
    
    'grid3ignore': {
        "description": """\nYou ignore the chapel,
deciding to continue your search of home""",
        "choices": {
            "1": "Upwards",
            "2": "Left",
            "3": "Right",
            },
        "paths": {
            "Upwards": 'grid6',
            "Left": 'grid2',
            "Right": 'N/A'
            },
        },
    
    'grid3enter': {
        "description": """\nYou enter the chapel,
your footsteps make the priest exit prayer and start to rise,
as he turns, you see unease on his face,
it quickly softens as he realises you are a threat.
The priest wears scuffed and damaged armour adorned with religious icons,
"Hello my child, what brings you here alone."

"You must have many questions, but I can only answer one.""",
        "choices": {
            "1": "What happened here?",
            "2": "Do you know where my home is?",
            "3": "Where is God?",
            "4": "Leave"
            },
        },

#need to code responses
        
    'grid4': {
        "description": """\nYou continue onwards,
you immediately start to smell the stench of something burning,
you look onwards to find many people dying and dead, and those who are not, grieving,
the mourners take no notice of you.
These people were clearly just attacked, whether from the devils that wander,
or those who denounced everything, even their own humanity.

What do you do?""",
        "choices": {
            "1": "Upwards",
            "2": "Left",
            "3": "Right",
            "4": "Downwards",
            "5": "Talk to the mourning"
            },
        "paths":{
            "Upwards": 'grid7',
            "Left": 'N/A',
            "Right": 'grid5',
            "Downwards": 'grid1nofather',
            "Talk to the mourning": 'grid4_mourners'
            },
        },

  
    
    'grid4_mourners': {
        "description": """\nIt would be best to leave the people to grieve.

Which way do you go?""",
        "choices": {
            "1": "Upwards",
            "2": "Left",
            "3": "Right",
            "4": "Downwards"
            },
        "paths":{
            "Upwards": 'grid7',
            "Left": 'N/A',
            "Right": 'grid5',
            "Downwards": 'grid1nofather'
            
            },
        },
    
    'grid5': {
        "description": """\nYou continue onwards,
you find yourself in a darkened passage covered by the canopy of tall trees,
amongst these trees lies a man, breathing heavy, he looks pained and injured.

What do you do?""",
        "choices": {
            "1": "Upwards",
            "2": "Left",
            "3": "Right",
            "4": "Downwards"
            },
        "paths": {
            "Upwards": 'grid8',
            "Left": 'grid4',
            "Right": 'grid6',
            "Downwards": 'grid2'
            },
        },
    
    'grid6': {
        "description": """\nYou continue onwards,
there is nothing but a large cross that takes your attention,
as you approach the cross there is a sign pinned to it,
it invites survivors to find the chapel,
Maybe you could find some help or knowledge, the chapel must be nearby.

Which way do you go?""",
        "choices": {
            "1": "Upwards",
            "2": "Left",
            "3": "Right",
            "4": "Downwards"
            },
        "paths": {
            "Upwards": 'grid9',
            "Left": 'grid5',
            "Right": 'N/A',
            "Downwards": 'grid3'
            },
        },
    
    'grid7': {
        "description": """\nYou continue onwards,
you find a large demon, it is pinned still to a cross,
the Demon wriggles and writhes at the sight of you,
it is unable to move due to the nails pinning it still,
eventually it gives up its attempts,
"What do you want human child."

Do you ignore the demon?""",
        "choices": {
            "1": "Talk to the demon",
            "2": "Ignore the demon"
            },
        "paths": {
            "Talk to the demon": 'grid7talk',
            "Ignore the demon": 'grid7ignore'
            },
        },
    
    'grid7talk': {
        "description": """\nYou move towards the demon,
it tries to lunge at you, the cross shaking as it attempts,
"You wish to ask me questions?""",
        "choices": {
            "1": "Why do you attack us?",
            "2": "Why does God not help us?",
            "3": "Leave"
            },
        },

#need to program interactions and paths
        
    'grid7ignore': {
        "description": """\nYou ignore the demon, it snarls at you as you pass it

Which way do you go?""",
        "choices": {
            "1": "Upwards",
            "2": "Left",
            "3": "Right",
            "4": "Downwards"
            },
        "paths": {
            "Upwards": 'N/A',
            "Left": 'N/A',
            "Right": 'grid8',
            "Downwards": 'grid4'
            },
        },
    
    'grid8': {
        "description": """\nYou continue onwards,
there is nothing here, it would be wise to not stay long,
you decide to continue onwards quickly

Which way do you go?""",
        "choices": {
            "1": "Upwards",
            "2": "Left",
            "3": "Right",
            "4": "Downwards"
            },
        "paths": {
            "Upwards": 'N/A',
            "Left": 'grid7',
            "Right": 'grid9',
            "Downwards": 'grid5'
            },
        },

    'grid9': {
        "description": """\nYou continue onwards,
you find a familiar marking, it is from your people,
your home is near.

Which way do you go?""",
        "choices": {
            "1": "Upwards",
            "2": "Left",
            "3": "Right",
            "4": "Downwards"
            },
        "paths": {
            "Upwards": 'home',
            "Left": 'grid8',
            "Right": 'lose',
            "Downwards": 'grid6'
            },
        },
    
    'home': {
        "description": """\nYou continue onwards, walking towards the familiar sight.
your feet are calloused and pained from the miles you have walked,
but after all your search you finally have found home.

You win! Congrats"""
        },

    'lose': {
        "description": """\nYou continue onwards, walking towards the sight of people,
your feet are calloused and pained, but you endure at the sight of what you believe are your people,
as you close in, you are overwhelmed with dread, the people arise from their ritual,
they're covered in viscera and blood, they start to walk towards you,
you attempt to run but your legs refuse to move, the pain has become too much and you are frozen in fear,
you only pray God will save you.

You lose."""
        },

}
#------------------------------------------------------------------------------

print("""Welcome to your quest,
You are a child in a wartorn land,
Sin is more rampant than ever,
hellspawn hunt the man.
you were sent with your father to find some food and supplies.
you succeeding in finding food for your people,
but your father is dead.

You must find home.""")

# The main loop of the game
def show_location(location_name):
    location_data = location[location_name]
    print(location_data['description'])
    
    # Display available choices
    for choice, text in location_data['choices'].items():
        print(f"{choice}: {text}")
    
    # Handle the player's input
    player_choice = input("Choose. (number): ").strip()
    
    # If the player chooses a valid path
    if player_choice in location_data['choices']:
        next_location = location_data['paths'][location_data['choices'][player_choice]]
        
        # If the path is N/A, prompt again without moving
        if next_location == "N/A":
            print("This path is not available. Please choose another option.")
            show_location(location_name)  # Stay in the current grid and prompt again
        else:
            show_location(next_location)  # Move to the next location
    else:
        print("Invalid choice. Please try again.")
        show_location(location_name)  # Stay in the current grid and prompt again
        if next_location == 'home' / 'lose':
            quit ()
        else:
            show_location(next_location)  # Move to the next location
    else:
        print("Invalid choice. Please try again.")
        show_location(location_name)  # Stay in the current grid and prompt again

# Start the game at grid0
show_location('grid0')


