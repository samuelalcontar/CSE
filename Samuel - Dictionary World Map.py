world_map = {
    'HOUSE': {
        'NAME': "House",
        'DESCRIPTION': "You have a lot of gold inside of your house.There is two exits. One exit is "
                       "to the East and one to the South",
        'PATHS': {
            'EAST': "STORE",
            'SOUTH': "JAIL"
        }
    },
    "STORE": {
        'NAME': "Store",
        'DESCRIPTION': "allot of things to purchase. the to exits you have are to the south and west",
        'PATHS': {
            'WEST': "HOUSE",
            'SOUTH': 'SHED'
        }
    },
    'JAILHOUSE': {
        'NAME': "Jailhouse",
        'DESCRIPTION': "You see a bunch of delinquents.They are armed.The exits are to East,South,and North",
        'PATHS': {
            'EAST': 'SHED',
            'SOUTH': 'GANG ALLEY',
            'NORTH':  'HOUSE'
        }
    },
    "GANG ALLEY": {
        'NAME': 'Gang Alley',
        'DESCRIPTION': "The kids broke out of jai and they have dogs.WATCH OUT for them. Run to either the North,East, " 
                       "or the south.",
        'PATHS': {
            'NORTH': 'JAILHOUSE',
            'EAST': 'ABANDONED STORE',
        }
    },
    'SHED': {
        'NAME': 'Shed',
        'DESCRIPTION': "They're is an oxygen Tank and and a sword.The exits are to the West,East,and South of you",
        'PATHS': {
            'WEST': 'BASEMENT',
            'EAST': 'YARD',
            'SOUTH': 'JAILHOUSE'
        }
    },
    'YARD': {
        'NAME': 'Yard',
        'DESCRIPTION': 'this yard has very long grass.it also has a bunch of fruit trees.If you want to leave this '
                       'place you can go to the East,South,or West.',
        'PATHS': {
            "EAST": 'FOREST',
            "SOUTH": 'TRAIL_OF_ROOTS',
            "WEST": 'SHED'
        }
    },
    'FOREST': {
        'NAME': 'Forest',
        'DESCRIPTION': 'This forest is enchanted you will run into allot of people out of the ordinary.This forest '
                       'also holds the tallest trees known to man.If you want to leave this glorious place go to the'
                       ' South or West',
        'PATHS': {
            'SOUTH': 'Trail',
            'WEST': 'Yard'
        }
    },
    'TRAIL': {
        'NAME': "Trail_of_Roots",
        'DESCRIPTION': 'The roots are so overgrown.This is still part of the enchanted forest so watch out they might'
                       ' be alive.there is two ways out.West and East.',
        'PATHS': {
            'WEST': 'WATERFALLS',
            'EAST': 'FOREST'
        }
    },
    'WATERFALLS': {
        'NAME': 'Waterfalls',
        'DESCRIPTION': 'The magical falls will make you stay young forever.There is so much good meat and fruit but who'
                       ' left it here?.If you feel unsafe and you wanna leave go to the South,East,or West.',
        'PATHS': {
            'South': 'UNDERWATER_WORLD',
            'EAST': "TRAIL",
            'WEST': 'ABANDONED_STORE'
        }
    },
    'UNDERWATER_WORLD': {
        'NAME': 'OCEAN',
        'DESCRIPTION': 'This is where the Watergod lives.He may be your friend for this adventure and he may not '
                       'SO BE CAREFUL. You can go to the EAST and NORTH',
        'PATHS': {
            'EAST': "NOT_SO_MAGICAL_CLIFF",
            'NORTH': 'WATERFALLS'
        }
    },
    'ABANDONED_STORE': {
        'NAME': 'Store',
        'DESCRIPTION': 'You can geet stuff for free form here but there is alwasy shoplifters.How the store gets'
                       ' restocked nobody nows.There is alout of thiefs and cime around here. '
                       'The exits are to EAST,SOUTH,and WEST.',
        'PATHS': {
            'EAST': 'WATERFALLS',
            'SOUTH': 'DEATH_DUNGEON',
            'WEST': 'GANG_ALLEY '
        }
    },
    'NOT_SO_MAGICAL_CLIFF': {
        'NAME': 'Deadly_cliff',
        'DESCRIPTION': "If you dont watch your step you may die.This cliff has a bunch of weapons laying around."
                       "You can go to  the SOUTH or WEST.",
        'PATHS': {
            'SOUTH': 'YOU FELL OFF THE CLIFF',
            'WEST': 'UNDERWATER_WORLD'
        }
    },
    'YOU FELL OFF THE CLIFF': {
        'NAME': 'DEATH',
        'DESCRIPTION': 'YOU HAVE FALLEN OFF NOT_SO_MAGICAL_CLIFF. IF YOU WISH TO CONITINUE THIS GAME AND NOT FALL OF'
                       ' THIS CLIFF PRESS REFRESH. THE NEXT TIME YOU PLAY THIS GAME DONT FALL TO YOUR DEATH.AND BTW'
                       ' I AM YOUR CONSCIOUS TELLING YOU TO BE SMART.',
        'PATHS': {
            'NONE'
        }
    },
    'DEATH_DUNGEON': {
        'NAME': 'DUNGEON',
        'DESCRIPTION': 'This dungeon has a whole lot of dead people. The butcher sees you and starts comming towards '
                       'you. you look around and see the only exit is back behind you(NORTH).',
        'PATHS': {
            'NORTH': 'ABANDONED STORE'
        }
    },
    'BASEMENT': {
        'NAME': 'BASEMENT',
        'DESCRIPTION': 'its pretty scary down here.You can only go back the way you came.you can only go EAST.',
        'PATHS': {
            'EAST': 'SHED'
        }
    },
    'DEATH': {
        'NAME': 'DEATH',
        'DESCRIPTION': 'If you wanna get out of death then you should not have died.REFRESH TO PLAY AGAIN',
        'PATHS': 'NONE'
    }
 }

current_node = world_map['HOUSE']
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']


while True:

    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command == 'JUMP':
            print('WOO')
    elif command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print('You can not go this way')
    else:
        print('Command not recognized')
