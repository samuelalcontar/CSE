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
    'JAIL': {
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
        'DESCRIPTION': 'This forest is enchanted you will run into alot of people out of the ordinary.This forest also '
                       'holds the tallest trees known to man.If you want to leave this glorious place go to the'
                       ' South or West',
        'PATHS': {
            'SOUTH': 'Trail_of_Roots',
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
        }
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
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print('You can not go this way')
    else:
        print('Command not recognized')
