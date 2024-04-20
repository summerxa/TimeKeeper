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

default levelHelp = {
    'main': '''
{b}BASIC GAMEPLAY{/b}
Manage your time wisely and complete tasks before it's too late!
Click on the name of a room to go to it, or the up/down arrows on the left to go up/down stairs.
Some furniture will be highlighted, which means there's a task you need to complete.
Click on an item to pick it up, or an empty space to place an item down. You can only carry one item in each hand, so you may be prompted to drop an item before picking up something else.
Hovering over a task or item will show information about it.

{b}LEFT SIDEBAR{/b}
Clock: shows the time and how long you have left.
Notebook: shows your current tasks.
    Be sure to check your notes often, as new tasks could appear at any time.
    Some tasks are related to the story and will be written in italics. You can disable "highlight recommended tasks" in settings to remove this feature.
Map: previews every floor map.
    You can use this to locate a task without physically moving to another room, which takes time!
On-hand: shows the contents of your inventory.
Help: shows this popup!
    The contents of this popup will change based on your current activity.
    If you are currently in a task minigame, it will show instructions on how to complete the task in addition to this text.
Leave: exits the current game state.
    If you are in a main floor map, pauses the game and opens the save menu.
    If you are in a room map, exits to the main floor map.
    If you are using the preview map, closes the map and returns to normal gameplay.
    And if you are in a task minigame, causes you to leave the task. Be careful with this; leaving a task will take some time even if you didn't complete it!

{b}COMPLETION{/b}
The notebook will show your progress using two separate displays.
The first one shows how many major quests you have completed.
    These quests are related to the story, and you are recommended to complete them for the best experience.
The second one is an approval rating, indicating a low/medium/high completion of all tasks.
    Failing to complete certain tasks will lower your approval rating, while succeeding will raise it.
''',
    'grabdishes': '''
Drag a dirty dish from the table to pick it up and place it in your inventory.
To complete the task, collect all dirty dishes from this table.''',
    'dropdishes': '''
Drag a dirty dish from the stack into the sink. This removes the dishes from your inventory.
You can drop off as many dirty dishes as you like at any time, but you will only complete the task after every single dish is dropped off.''',
    'waterpour': '''Click on a cup to select it, and click again to deselect it.
Click on another cup to pour the topmost later of water into it.
You can only pour into a cup if it has at least one empty slot.
To complete the task, sort the drinks until each cup is either empty or contains all one color.
Two or more cups cannot contain the same color.''',
}

# size/pos of room on main floor map
# (topleft x, y, bottomright x, y)
default roomRects = {
    1: {
        0: {
            'ballroom': (490, 85, 1440, 560),
            'kitchen': (850, 600, 1440, 970),
            'laundry': (490, 600, 815, 970)
        },
        1: {
            'room 4': (520, 166, 1476, 816)
        }
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
            'xp': 647,
            'yp': 530,
            'room': 'kitchen',
            'imtask': 'kitchensink'
        },
        'pickuptable': {
            'xp': 459,
            'yp': 560,
            'room': 'kitchen',
            'imtask': 'pickuptable',
            'taskless': 'custom_taskless'
        },
        'kitchen_idk': {
            'xp': 550,
            'yp': 292,
            'room': 'kitchen',
            'imtask': 'kitchenidk'
        },
        'laundry_1': {
            'xp': 910,
            'yp': 330,
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
            'tlabel': 'chap1_test_t1',
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
