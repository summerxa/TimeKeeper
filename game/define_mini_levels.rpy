init python:
    def chars_init_and_load():
        charmenu_data = [
            'mc', 'mother', 'amelia', 'bella'
        ]

        for c in charmenu_data:
            if not c in store.chars_current:
                store.chars_current[c] = {
                    'desc': 'desc_default',
                    'small': 'small_default',
                    'big': 'big_default',
                    'alive': True,
                    'friend': False,
                    'friendlvl': 0
                }

    
    def all_init_and_load():
        chars_init_and_load()


default levelInfo = {
    1: {
        't0': 1020,
        'tf': 1200,
        'info': '''Info about the time needed for each task.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAlso did you know this textbox has a scroll bar? :D''',
        'tstairs': 2,
        'nfloors': 2,
        'ndishes': 8
    }
}

default levelHints = {
    'default_start': "Welcome.",
    'default_idle': "...",
    'default_taskless': "No task available right now.",
    'custom_taskless': "A custom idle message.",
    'grabdishes_fail': "imagine having your hands full and not being able to pick up dishes smh",
    'grabdishes_idle': "That's a lot of dirty dishes...",
    'dropdishes_fail': "you're not even holding dishes in your inventory?? what???",
    'dropdishes_idle': "Dirty dish tower!!!!",
    'toggle_idle': "Meow",
    'waterpour_idle': "Time to cook :3",
    'waterpour_cup_full': "This glass is full; I can't pour into it."
}

# dimensions (w,h) of room map img
default roomDims = {
    1: {
        'ballroom': (1920, 1080),
        'kitchen': (1331, 800),
        'laundry': (793, 877),
        'room 4': (1926, 1079)
    }
}

default roomButtons = {
    1: {
        'ballroom': {
            'name': 'ballroom',
            'floor': 0,
            'num': 0,
            'xp': 0.5,
            'yp': 0.2,
        },
        'kitchen': {
            'name': 'kitchen',
            'floor': 0,
            'num': 1,
            'xp': 0.6,
            'yp': 0.7
        },
        'laundry': {
            'name': 'laundry',
            'floor': 0,
            'num': 2,
            'xp': 0.35,
            'yp': 0.7
        },
        'room 4': {
            'name': 'room 4',
            'floor': 1,
            'num': 0,
            'xp': 0.5,
            'yp': 0.5
        }
    }
}

default roomProxim = {
    1: {
        0: [[0,1,1],
            [1,0,5],
            [1,5,0]],
        1: [[0]]
    }
}

default roomArrows = {
    1: {
        'ballroom': [
            {
                'toroom': 'kitchen',
                'dir': 'down',
                'xp': 0.6
            },
            {
                'toroom': 'laundry',
                'dir': 'down',
                'xp': 0.3
            }
        ],
        'kitchen': [
            {
                'toroom': 'ballroom',
                'dir': 'up',
                'xp': 0.6
            },
            {
                'toroom': 'laundry',
                'dir': 'up',
                'xp': 0.3
            }
        ],
        'laundry': [
            {
                'toroom': 'ballroom',
                'dir': 'up',
                'xp': 0.3
            },
            {
                'toroom': 'kitchen',
                'dir': 'up',
                'xp': 0.6
            }
        ]
    }
}

# location of MC's icon on preview map
default mcIconLoc = {
    1: {
        'ballroom': [0.5, 0.3],
        'kitchen': [0.6, 0.8],
        'laundry': [0.3, 0.8],
        'room 4': [0.5, 0.6]
    }
}

default taskButtons = {
    1: {
        't11': {
            'xp': 0.5,
            'yp': 0.5,
            'room': 'ballroom',
            'hidden': True,
            'imtask': 'normal'
        },
        't12': {
            'xp': 0.5,
            'yp': 0.3,
            'room': 'ballroom',
            'imtask': 'normal'
        },
        'sink': {
            'xp': 334,
            'yp': 388,
            'room': 'kitchen',
            'imtask': 'kitchensink'
        },
        'pickuptable': {
            'xp': 146,
            'yp': 418,
            'room': 'kitchen',
            'imtask': 'pickuptable',
            'taskless': 'custom_taskless'
        },
        'kitchen_idk': {
            'xp': 234,
            'yp': 150,
            'room': 'kitchen',
            'imtask': 'kitchenidk'
        },
        'laundry_1': {
            'xp': 440,
            'yp': 201,
            'room': 'laundry',
            'imtask': 'laundrymachine'
        }
    }
}

default taskRoots = {
    1: ['t1', 't2', 't3']
}

default tasks = {
    1: {
        't1': {
            'name': 't1',
            'desc': 'Clear the table',
            'btn': 't11',
            'tlabel': 'task_c1_grabdishes',
            'fail_id': 'grabdishes_fail',
            'item_req': ['air', 'dirty_dishes'],
            'tcost': 10,
            't0': 1020,
            'tf': 1030,
            'scorebonus': 10,
            'scorepenalty': 1,
            'tags': [],
            'game': {
                'type': 'grabdishes',
                'goal': 5,
                'drag': [
                    {
                        'xp': 0.2, 'yp': 0.3
                    },
                    {
                        'xp': 0.5, 'yp': 0.3
                    },
                    {
                        'xp': 0.3, 'yp': 0.3
                    },
                    {
                        'xp': 0.5, 'yp': 0.5
                    },
                    {
                        'xp': 0.5, 'yp': 0.2
                    }
                ],
                'drop': [
                    {
                        'n': 'goal','xp': 0.2, 'yp': 0.6, 'im': 'mini/btn_item/test_item0_idle.jpg'
                    }
                ],
                'hint': [2, 'this is a very helpful hint']
            }
        },
        't2': {
            'name': 't2',
            'desc': 'Drop off dirty dishes',
            'btn': 'sink',
            'tlabel': 'task_c1_dropdishes',
            'fail_id': 'dropdishes_fail',
            'item_req': ['dirty_dishes'],
            'tcost': 10,
            't0': -1,
            'tf': 9999,
            'scorebonus': 1,
            'scorepenalty': 1,
            'tags': [],
            'game': {
                'type': 'dropdishes',
                'xp': 0.5,
                'im': 'mini/icon_map_mc_idle.png',
                'drop': [
                    {
                        'n': 'goal','xp': 0.2, 'yp': 0.6, 'im': 'mini/btn_item/test_item0_idle.jpg'
                    }
                ],
                'hint': [2, 'this is another hint']
            }
        },
        't3': {
            'name': 't3',
            'desc': 'Drop off test item 3',
            'btn': 'laundry_1',
            'tlabel': 'c1_t1',
            'tcost': 5,
            't0': -1,
            'tf': 9999,
            'scorebonus': 0,
            'scorepenalty': 0,
            'tags': [Task.SPECIAL]
        },
        't4': {
            'name': 't4',
            'desc': 'Click on all the Cat MC pictures :D',
            'btn': 'pickuptable',
            'tlabel': 'task_c1_toggle',
            'tcost': 5,
            't0': -1,
            'tf': 9999,
            'scorebonus': 1,
            'scorepenalty': 1,
            'tags': [Task.SPECIAL],
            'game': {
                'type': 'toggle',
                'goal': [True, True],
                'xp': [0.3, 0.7],
                'yp': [0.5, 0.5],
                'off': ['mini/icon_map_mc_%s.png', 'mini/icon_map_mc_%s.png'],
                'on': ['mini/btn_item/test_item0_%s.jpg', 'mini/btn_item/test_item0_%s.jpg'],
                'hint': [1, 'Click on the items to pick them up/put them down']
            }
        },
        't5': {
            'name': 't5',
            'desc': 'MC we need to cook',
            'btn': 't12',
            'tlabel': 'task_c1_waterpour',
            'tcost': 5,
            't0': -1,
            'tf': 9999,
            'scorebonus': 1,
            'scorepenalty': 0,
            'tags': [],
            'game': {
                'type': 'waterpour',
                'yp': 0.5,
                'cups': [
                    {
                        'xp': 0.24,
                        'colors': ['#920e0e']
                    },
                    {
                        'xp': 0.38,
                        'colors': ['#920e0e', '#a4f910', '#920e0e', '#eedfab']
                    },
                    {
                        'xp': 0.52,
                        'colors': ['#eedfab', '#a4f910', '#a4f910', '#920e0e']
                    },
                    {
                        'xp': 0.66,
                        'colors': ['#eedfab', '#eedfab', '#a4f910']
                    }
                ]
            }
        }
    }
}

# normally "air" would be a transparent image but it's visible for testing purposes lol
default itemsAll = {
    'air': {
        'name': 'empty',
        'im': 'mini/btn_item/test_item0_%s.jpg',
        'desc': 'An empty spot. An item can be placed here.',
        'stackable': False
    },
    'test_3': {
        'name': 'test item 3',
        'im': 'mini/btn_item/test_item3_%s.jpg',
        'desc': 'I guess this is an item too?? It\'s called test item 3.',
        'stackable': False
    },
    'dirty_dishes': {
        'name': 'dirty dishes',
        'im': 'mini/btn_item/test_item1_%s.jpg',
        'desc': 'A stack of dirty dishes.',
        'stackable': True
    }
}

default itemHolders = {
    1: {
        'h11': {
            'item': {
                'id': 'dirty_dishes',
                'stack': 1
            },
            'xp': 0.2,
            'yp': 0.1,
            'room': 'ballroom'
        },
        'h12': {
            'item': {
                'id': 'dirty_dishes',
                'stack': 2
            },
            'xp': 0.6,
            'yp': 0.5,
            'room': 'ballroom'
        },
        'h21': {
            'item': {
                'id': 'test_3'
            },
            'xp': 0.6,
            'yp': 0.1,
            'room': 'ballroom'
        },
        'h31': {
            'item': {
                'id': 'test_3'       
            },
            'xp': 0.2,
            'yp': 0.5,
            'room': 'ballroom'
        }
    }
}
