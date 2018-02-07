world_map = {
    'WESTHOUSE':{
        'NAME': "West of House",
        'Description': "You are west of a white house.",
        'Paths':{
            'NORTH':"NORTHHOUSE",
            'SOUTH':"SOUTHHOUSE"
}
    },
    "SOUTHHOUSE":{
        'NAME': "South of House",
        'Desciption': "Insert description here",
        'Paths':{
              'West': "WESTHOUSE"
}
    },
    'NORTHHOUSE':{
        'NAME':"North of house",
        'DESCRIPTION': "Insert Description here",
        'Paths':{
            'WESTHOUSE'
        }
    }
    }