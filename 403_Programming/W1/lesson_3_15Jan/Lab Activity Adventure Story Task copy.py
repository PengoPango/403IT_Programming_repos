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
      "description": """\nYou continue onwards,
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
            "Left": 'grid1nofather',
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
        "visited_description": """\n You find yourself back at the chapel,
there is no value in reentering the chapel""",
        "choices": {
            "1": "Ignore the chapel",
            "2": "Enter the chapel"
            },
        "paths": {
            "Ignore the chapel": 'grid3ignore',
            "Enter the chapel": 'grid3enter'
            },
        "one_time_action": ["Enter the chapel"]
        },
    
    
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

"You must have many questions, but I can only answer one." """,
        "choices": {
            "1": "Do you know where my home is?",
            "2": "What happened here?",
            "3": "Where is God?",
            },
        "paths": {
            "Do you know where my home is?": 'priestguide',
            "What happened here?": 'priestsgrief',
            "Where is God?": 'priestgod'
            },
        },

    'priestsgrief': {
        "description": """\n"This chapel was once a house of God,
protecting those in need and faith from the creatures that now roam,
I protected and preached for all in need of hope.
However one led too far astray, beseeched and lied to me,
they asked me to come with them to help their people,
I was foolish enough to join them in belief of helping those in need,
however all i found was blasphemous horror.
Upon my return my chapel and those i protected were desecrated and slaughtered.
May God forgive my failings, for i shaln't forgive my own." """,
        "choices": {
            "1": "Leave the priest",
            },
        "paths": {
            "Leave the priest":'grid3leavechapel',
            },
        },
  
    'priestguide': {
        "description": """\n"I have seen a many wander these lands my child,
I pray i am not incorrect but based on similar apparrel to yours,
I had seen one a band of travellers travel upwards from this chapel,
it is a dangerous path however, i pray God protects you on this path for I cannot accompany you,
I must protect this chapel, I shall not falter in my duty twice." """,
        "choices": {
            "1": "Leave the priest",
            },
        "paths": {
            "Leave the priest":'grid3leavechapel',
            },
        },
  
    'priestgod': {
        "description": """\n"You surprise my child, to ask such a question at your age,
I shall answer still as that was my word;

Just as Enoch tells us, there was a war between the Angels of Heaven and those that had fallen,
God also joined his children in this battle against the fallen, however he was wounded in this battle,
having to kill one of his most beloved sons who turned on him, he faltered,
leading to a blow which shook both heaven and hell.

Ever since, God had not stepped foot on Earth, but always kept watch from heaven,
keeping his epistemic distance but guiding us to flourish.
yet now God has left our lands, that is why these abominations roam the lands,
they are a pox upon God's light, it truly sickens me.
I do not know why God has left us now, but I have faith God shall return,
God cannot... no.
God will not abandon us.
Have faith in this as i do, child." """,
        "choices": {
            "1": "Leave the priest"
            },
        "paths": {
            "Leave the priest":'grid3leavechapel'
            },
        },
  
  'grid3leavechapel': {
      "description": """\nYou begin to leave the chapel...
"Before you leave my child, beware upwards, there is a great demon to be careful of,
I was able to bind him, but he still persists, you have no chance of victory"

the priest turns and returns to prayer as you leave,
you hope the wisdom he has granted you aids your perspective,
you look back out upon the twisted, ruinous land.
You cannot forget your purpose, you must find your family, they need you.

Which way do you go?""",
        "choices": {
            "1": "Upwards",
            "2": "Left",
            "3": "Right"
            },
        "paths": {
            "Upwards": 'grid6',
            "Left": 'grid2',
            "Right": 'N/A'
            },
        },

        
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

#starting game print
print("""Welcome to your quest,
You are a child in a wartorn land,
Sin is more rampant than ever,
hellspawn hunt the man.
you were sent with your father to find some food and supplies.
you succeeding in finding food for your people,
but your father is dead.

You must find home.""")

visited = {}

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
        action = location_data['choices'][player_choice]
        next_location = location_data['paths'][action]

            #if player repeats an unrepeatable task eg 'trying to talk to priest again'
     
        if 'one_time_action' in location_data:
            if location_name not in visited:
                visited[location_name] = set ()
            if action in location_data["one_time_action"] and action in visited[location_name]:
                print("""\nYou cannot perform this action again!
Please choose another option.""")
                show_location(location_name)
                return
            else:
                visited[location_name].add(action)

        
        # If the path is N/A, prompt again without moving
        if next_location == "N/A":
            print("""\nThis path is not available. You think going this way would be a bad idea.
Please choose another option.""")
            show_location(location_name)  # Stay in the current grid and prompt again
        else:
            show_location(next_location)  # Move to the next location

    else:
        print("\nInvalid choice. Please try again.")
        show_location(location_name)  # Stay in the current grid and prompt again
        
        if next_location == 'home' / 'lose':
            quit ()
        else:
            show_location(next_location)  # Move to the next location
            

# Start the game at grid0
show_location('grid0')


