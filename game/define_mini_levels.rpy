init python:
    def chars_init_and_load():
        charmenu_data = [
            'mc', 'mother', 'amelia', 'bella'
        ]

        for c in charmenu_data:
            if not c in store.chars_current:
                store.chars_current[c] = {
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
        'tstairs': 2,
        'nfloors': 2,
        'ndishes': 12,
        'threshold': [-20, 30],
        'nonRoots': ['donothing', 'fetch1_end', 'fetch2_end', 'fetch3_end'],
        'quests': {
            'Fetch quest 1': False,
            'Fetch quest 2': False,
            'Fetch quest 3': False,
            'Fetch quest 4': False
        },
        'room0': 'ballroom',
        'floor0': 0
    }
}

default levelHints = {
    'default_start': "Welcome.",
    'default_idle': "...",
    'default_taskless': "No task available right now.",
    'custom_taskless': "A custom idle message.", # TODO remove this placeholder text
    'grabdishes_fail': "imagine having your hands full and not being able to pick up dishes smh",
    'grabdishes_idle': "That's a lot of dirty dishes...",
    'dropdishes_fail': "you're not even holding dishes in your inventory?? what???",
    'dropdishes_idle': "Dirty dish tower!!!!",
    'toggle_idle': "Meow",
    'waterpour_idle': "Time to cook :3",
    'waterpour_cup_full': "This glass is full; I can't pour into it.",
    'laundry_idle': "Woahhh it's laundry :o"
}

default helpText = {
    'main': '''{b}BASIC GAMEPLAY{/b}
Manage your time wisely and complete tasks before time runs out!
Click on the name of a room to go to it, or the up/down arrows on the left to go up/down stairs.
Some furniture will be highlighted, which means there's a task you need to complete.
Click on an item to pick it up, or an empty space to place an item down. You can only carry one item in each hand, so you may be prompted to drop an item before picking up something else.
Hovering over a task or item will show information about it.

{b}LEFT SIDEBAR{/b}
Clock: shows the current time and how long you have left.
Notebook: shows your current tasks.
    Be sure to check this tab often, as new tasks could appear at any time.
    Some tasks are related to the story and will be written in {i}italics{/i}.
    You can remove this feature by unchecking "highlight recommended tasks" in settings.
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
The notebook will show your completion progress using two separate displays.
The first one is an approval rating. Pay attention to this, as your final approval rating may affect the actions of other characters!
    Failing to complete certain tasks will lower your approval rating, while succeeding will raise it.
    Certain tasks will be labeled as "bonus tasks". These tasks will award approval points upon completion, but will not subtract points if left undone.
The second one shows how many major quests you have completed.
    These quests are related to the story, and you are recommended to complete them for the best story experience.
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
    'laundry': '''Drag each article of clothing into the correct washing machine.
Each washing machine is set to a certain amount of time.
Light clothing needs to be washed for the least amount of time.
Heavy clothing needs to be washed for the most amount of time.
Lastly, medium clothing cannot be washed for too long or too short.'''
}

default infoText = {
    'notes': '''The notebook shows all your current tasks.
    Be sure to check this tab often, as new tasks could appear at any time.
    Some tasks are related to the story and will be written in {i}italics{/i}.
    You can remove this feature by unchecking "highlight recommended tasks" in settings.

The notebook will show your completion progress using two separate displays.
The first one is an approval rating. Pay attention to this, as your final approval rating may affect the actions of other characters!
    Failing to complete certain tasks will lower your approval rating, while succeeding will raise it.
    Certain tasks will be labeled as "bonus tasks". These tasks will award approval points upon completion, but will not subtract points if left undone.
The second one shows how many major quests you have completed.
    These quests are related to the story, and you are recommended to complete them for the best story experience.''',
    'onhand': '''You can pick up items by finding them around the map or by completing certain tasks.
You can only hold two items at a time, so make use of empty spaces around the map to keep track of all your items!
Finally, some items, like empty plates, can be stacked on top of each other and will only count as one item once stacked.
''',
    'trade': '''Normally, grabbing or dropping an item will be done automatically when you click on an item around the map.
However, if both of your hands are full, you will be prompted to choose which item you want to remove from your inventory.
'''
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
            'guestroom l': (340, 278, 904, 746),
            'guestroom r': (924, 278, 1489, 746)
        }
    }
}

default roomButtons = {
    1: {
        'ballroom': {
            'name': 'ballroom',
            'floor': 0,
            'num': 0
        },
        'kitchen': {
            'name': 'kitchen',
            'floor': 0,
            'num': 1
        },
        'laundry': {
            'name': 'laundry',
            'floor': 0,
            'num': 2
        },
        'guestroom l': {
            'name': 'left guestrooms',
            'floor': 1,
            'num': 0
        },
        'guestroom r': {
            'name': 'right guestrooms',
            'floor': 1,
            'num': 1
        }
    }
}

default roomProxim = {
    1: {
        0: [[0,1,1],
            [1,0,2],
            [1,2,0]],
        1: [[0,1],
            [1,0]]
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
        ],
        'guestroom l': [
            {
                'toroom': 'guestroom r',
                'dir': 'up',
                'xp': 0.5
            }
        ],
        'guestroom r': [
            {
                'toroom': 'guestroom l',
                'dir': 'down',
                'xp': 0.5
            }
        ]
    }
}

default taskButtons = {
    1: {
        '4_1': {
            'p': (547, 272),
            'room': 'ballroom',
            'imtask': 'br_4seat',
            'rot': 30
        },
        '4_2': {
            'p': (677, 285),
            'room': 'ballroom',
            'imtask': 'br_4seat',
            'rot': 10
        },
        '4_3': {
            'p': (815, 269),
            'room': 'ballroom',
            'imtask': 'br_4seat',
            'rot': -10
        },
        '4_4': {
            'p': (540, 793),
            'room': 'ballroom',
            'imtask': 'br_4seat',
            'rot': 15
        },
        '4_5': {
            'p': (667, 800),
            'room': 'ballroom',
            'imtask': 'br_4seat',
            'rot': 5
        },
        '4_6': {
            'p': (810, 790),
            'room': 'ballroom',
            'imtask': 'br_4seat',
            'rot': -15
        },
        'long1': {
            'p': (981, 375),
            'room': 'ballroom',
            'imtask': 'br_longtable'
        },
        'long2': {
            'p': (981, 683),
            'room': 'ballroom',
            'imtask': 'br_longtable'
        },
        'bar': {
            'p': (1120, 542),
            'room': 'ballroom',
            'imtask': 'br_bar'
        },
        '6_1': {
            'p': (1240, 391),
            'room': 'ballroom',
            'imtask': 'br_6seat'
        },
        '6_2': {
            'p': (1240, 529),
            'room': 'ballroom',
            'imtask': 'br_6seat'
        },
        '6_3': {
            'p': (1240, 667),
            'room': 'ballroom',
            'imtask': 'br_6seat'
        },
        '6_4': {
            'p': (1360, 327),
            'room': 'ballroom',
            'imtask': 'br_6seat'
        },
        '6_5': {
            'p': (1360, 461),
            'room': 'ballroom',
            'imtask': 'br_6seat'
        },
        '6_6': {
            'p': (1360, 596),
            'room': 'ballroom',
            'imtask': 'br_6seat'
        },
        '6_7': {
            'p': (1360, 729),
            'room': 'ballroom',
            'imtask': 'br_6seat'
        },
        '6_8': {
            'p': (1480, 391),
            'room': 'ballroom',
            'imtask': 'br_6seat'
        },
        '6_9': {
            'p': (1480, 529),
            'room': 'ballroom',
            'imtask': 'br_6seat'
        },
        '6_10': {
            'p': (1480, 667),
            'room': 'ballroom',
            'imtask': 'br_6seat'
        },
        'sink': {
            'p': (647, 530),
            'room': 'kitchen',
            'imtask': 'kitchen_sink'
        },
        'pickuptable': {
            'p': (459, 558),
            'room': 'kitchen',
            'imtask': 'kitchen_pickup',
            'taskless': 'custom_taskless'
        },
        'kitchen_idk': {
            'p': (550, 292),
            'room': 'kitchen',
            'imtask': 'kitchen_idk'
        },
        'laundry_1': {
            'p': (910, 330),
            'room': 'laundry',
            'imtask': 'laundry_machine'
        },
        'gr_1': {
            'p': (405, 360),
            'room': 'guestroom l',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '401',
                'style': 'plaque1_font'
            }
        },
        'gr_2': {
            'p': (600, 360),
            'room': 'guestroom l',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '402',
                'style': 'plaque1_font'
            }
        },
        'gr_3': {
            'p': (795, 360),
            'room': 'guestroom l',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '403',
                'style': 'plaque1_font'
            }
        },
        'gr_4': {
            'p': (1120, 360),
            'room': 'guestroom l',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '404',
                'style': 'plaque1_font'
            }
        },
        'gr_5': {
            'p': (1315, 360),
            'room': 'guestroom l',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '405',
                'style': 'plaque1_font'
            }
        },
        'gr_6': {
            'p': (1510, 360),
            'room': 'guestroom l',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '406',
                'style': 'plaque1_font'
            }
        },
        'gr_7': {
            'p': (405, 720),
            'room': 'guestroom l',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '407',
                'style': 'plaque1_font'
            }
        },
        'gr_8': {
            'p': (600, 720),
            'room': 'guestroom l',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '408',
                'style': 'plaque1_font'
            }
        },
        'gr_9': {
            'p': (795, 720),
            'room': 'guestroom l',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '409',
                'style': 'plaque1_font'
            }
        },
        'gr_10': {
            'p': (1120, 720),
            'room': 'guestroom l',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '410',
                'style': 'plaque1_font'
            }
        },
        'gr_11': {
            'p': (1315, 720),
            'room': 'guestroom l',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '411',
                'style': 'plaque1_font'
            }
        },
        'gr_12': {
            'p': (1510, 720),
            'room': 'guestroom l',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '412',
                'style': 'plaque1_font'
            }
        },
        'gr_21': {
            'p': (405, 360),
            'room': 'guestroom r',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '421',
                'style': 'plaque1_font'
            }
        },
        'gr_22': {
            'p': (600, 360),
            'room': 'guestroom r',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '422',
                'style': 'plaque1_font'
            }
        },
        'gr_23': {
            'p': (795, 360),
            'room': 'guestroom r',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '423',
                'style': 'plaque1_font'
            }
        },
        'gr_24': {
            'p': (1120, 360),
            'room': 'guestroom r',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '424',
                'style': 'plaque1_font'
            }
        },
        'gr_25': {
            'p': (1315, 360),
            'room': 'guestroom r',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '425',
                'style': 'plaque1_font'
            }
        },
        'gr_26': {
            'p': (1510, 360),
            'room': 'guestroom r',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '426',
                'style': 'plaque1_font'
            }
        },
        'gr_27': {
            'p': (405, 720),
            'room': 'guestroom r',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '427',
                'style': 'plaque1_font'
            }
        },
        'gr_28': {
            'p': (600, 720),
            'room': 'guestroom r',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '428',
                'style': 'plaque1_font'
            }
        },
        'gr_29': {
            'p': (795, 720),
            'room': 'guestroom r',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '429',
                'style': 'plaque1_font'
            }
        },
        'gr_30': {
            'p': (1120, 720),
            'room': 'guestroom r',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '430',
                'style': 'plaque1_font'
            }
        },
        'gr_31': {
            'p': (1315, 720),
            'room': 'guestroom r',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '431',
                'style': 'plaque1_font'
            }
        },
        'gr_32': {
            'p': (1510, 720),
            'room': 'guestroom r',
            'imtask': 'guestr_plaque',
            'tx': {
                'text': '432',
                'style': 'plaque1_font'
            }
        }
    }
}

default taskTemplates = {
    'grabdishes': {
        'tcost': 5,
        'tdur': 20,
        'scorebonus': 2,
        'scorepenalty': 1,
        'desc': 'Clear the table',
        'tlabel': 'task_c1_grabdishes',
        'fail_id': 'grabdishes_fail',
        'item_req': ['air', 'dish_dirty'],
    },
    'dropdishes': {
        'tcost': 5,
        'scorebonus': 5,
        'scorepenalty': 1,
        'desc': 'Drop off dirty dishes',
        'tlabel': 'task_c1_dropdishes',
        'fail_id': 'dropdishes_fail',
        'item_req': ['dish_dirty'],
        'scorebonus': 1,
        'scorepenalty': 1
    },
    'waterpour': {
        'tcost': 10,
        'tdur': 30,
        'scorebonus': 4,
        'scorepenalty': 0,
        'desc': 'Bonus task: MC we need to cook',
        'tlabel': 'task_c1_waterpour'
    },
    'laundry': {
        'tlabel': 'task_c1_laundry',
        'desc': 'Bonus task: Sort the laundry',
        'tcost': 15,
        'tdur': 30,
        'scorebonus': 3,
        'scorepenalty': 0
    }
}

default tasks = {
    1: {
        'donothing': {
            'btn': '4_1',
            'tcost': 180,
            't0': -1,
            'tf': 9999,
            'desc': 'Bonus task: Sit in the corner and do nothing',
            'tlabel': 'task_c1_donothing',
            'scorebonus': 0,
            'scorepenalty': 0,
            'tags': [Task.DONOTHING]
        },
        'fetch1': {
            'desc': 'Talk to noble',
            'btn': '4_5',
            'tlabel': 'c1_fetch1',
            'tcost': 0,
            't0': -1,
            'tf': 9999,
            'scorebonus': 0,
            'scorepenalty': 0,
            'tags': [Task.SPECIAL],
            'nxt': ['fetch1_end']
        },
        'fetch1_end': {
            'desc': 'Bring wine to noble',
            'btn': '4_5',
            'tlabel': 'c1_fetch1_end',
            'tcost': 5,
            't0': -2,
            'tf': 9999,
            'scorebonus': 10,
            'scorepenalty': 5,
            'tags': [Task.SPECIAL],
            'nxt': ['fetch2']
        },
        'fetch2': {
            'desc': 'Talk to noble',
            'btn': '6_5',
            'tlabel': 'c1_fetch2',
            'tcost': 0,
            't0': -2,
            'tf': 9999,
            'scorebonus': 0,
            'scorepenalty': 0,
            'tags': [Task.SPECIAL],
            'nxt': ['fetch2_end']
        },
        'fetch2_end': {
            'desc': 'Bring jacket to noble',
            'btn': '6_5',
            'tlabel': 'c1_fetch2_end',
            'tcost': 5,
            't0': -2,
            'tf': 9999,
            'scorebonus': 10,
            'scorepenalty': 5,
            'tags': [Task.SPECIAL],
            'nxt': ['fetch3']
        },
        'fetch3': {
            'desc': 'Talk to noble',
            'btn': '6_5',
            'tlabel': 'c1_fetch3',
            'tcost': 0,
            't0': -2,
            'tf': 9999,
            'scorebonus': 0,
            'scorepenalty': 0,
            'tags': [Task.SPECIAL],
            'nxt': ['fetch3_end']
        },
        'fetch3_end': {
            'desc': 'Ask the chefs for desserts',
            'btn': 'kitchen_idk',
            'tlabel': 'c1_fetch3_end',
            'tcost': 5,
            't0': -2,
            'tf': 9999,
            'scorebonus': 10,
            'scorepenalty': 5,
            'tags': [Task.SPECIAL],
            'nxt': ['fetch4']
        },
        'fetch4': {
            'desc': 'Talk to noble',
            'btn': 'long1',
            'tlabel': 'c1_fetch4',
            'tcost': 10,
            't0': -2,
            'tf': 9999,
            'scorebonus': 10,
            'scorepenalty': 5,
            'tags': [Task.SPECIAL]
        },
        'grabdish_1': {
            'btn': '6_2',
            't0': 1020,
            'game': {
                'type': 'grabdishes',
                'goal': 5,
                'im': 'mini/tgame/grab_dropdishes/plate_dirty.png'
            }
        },
        'grabdish_2': {
            'btn': 'long2',
            't0': 1040,
            'game': {
                'type': 'grabdishes',
                'goal': 3,
                'im': 'mini/tgame/grab_dropdishes/plate_dirty.png'
            }
        },
        'grabdish_last': {
            'btn': '6_2',
            't0': 1160,
            'game': {
                'type': 'grabdishes',
                'goal': 4,
                'im': 'mini/tgame/grab_dropdishes/plate_dirty.png'
            }
        },
        'dropdish': {
            'btn': 'sink',
            't0': -1,
            'tf': 1180,
            'game': {
                'type': 'dropdishes',
                'xp': 0.5,
                'im': 'mini/tgame/grab_dropdishes/plate_dirty.png',
                'drop': [
                    {
                        'n': 'goal', 'p': (369, 356), 'w': 784, 'h': 525
                    }
                ],
                'in_sink': {
                    'p': (778, 618), 'im': 'mini/tgame/grab_dropdishes/plate_clean.png'
                },
                'overlay': [
                    {
                        'p': (678, 413), 'im': 'mini/tgame/grab_dropdishes/dropdishes_faucet.png'
                    }
                ]
            }
        },
        'getfood_1': {
            'desc': 'Click on all the Cat MC pictures :D',
            'btn': 'pickuptable',
            'tlabel': 'task_c1_toggle',
            'tcost': 5,
            't0': -1,
            'tf': 9999,
            'scorebonus': 1,
            'scorepenalty': 1,
            'game': {
                'type': 'toggle',
                'goal': [True, True],
                'p': [(0.3, 0.5), (0.7, 0.5)],
                'off': ['mini/icon_map_mc_%s.png', 'mini/icon_map_mc_%s.png'],
                'on': ['mini/btn_item/item_air_%s.png', 'mini/btn_item/item_air_%s.png']
            }
        },
        'waterpour_1': {
            'btn': 'bar',
            't0': 1040,
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
        },
        'laundry_1': {
            'btn': 'laundry_1',
            't0': 1100,
            'game': {
                'type': 'laundry'}
        }
    }
}

# normally "air" would be a transparent image but it's visible for testing purposes lol
default itemsAll = {
    'air': {
        'name': 'empty',
        'desc': 'An empty spot. An item can be placed here.',
        'im': 'air',
        'stackable': False
    },
    'test_3': {
        'name': 'test item 3',
        'desc': 'I guess this is an item too?? It\'s called test item 3.',
        'im': 'test_3',
        'stackable': False
    },
    'dish_dirty': {
        'name': 'dirty dishes',
        'desc': 'A stack of dirty dishes.',
        'im': 'food',
        'stackable': True
    },
    'wine_bottle': {
        'name': 'bottle of wine',
        'desc': 'A bottle of wine.',
        'im': 'wine_bottle',
        'stackable': False
    },
    'candle_lit': {
        'name': 'candle',
        'desc': 'A lit candle.',
        'im': 'candle',
        'stackable': False
    },
    'jacket_red': {
        'name': 'red jacket',
        'desc': 'A red jacket with golden trim.',
        'im': 'shirt',
        'stackable': False
    },
    'jacket_darkblue': {
        'name': 'dark blue jacket',
        'desc': 'A dark blue jacket with silver trim.',
        'im': 'shirt',
        'stackable': False
    },
    'jacket_black': {
        'name': 'black jacket',
        'desc': 'A black jacket with light gold trim.',
        'im': 'shirt',
        'stackable': False
    },
    'jacket_darkgreen': {
        'name': 'darkgreen jacket',
        'desc': 'A dark green jacket with three pockets.',
        'im': 'shirt',
        'stackable': False
    }
}

default itemHolders = {
    1: {
        'kitchen1': {
            'item': {
                'id': 'air'       
            },
            'p': (392, 266),
            'room': 'kitchen'
        },
        'kitchen2': {
            'item': {
                'id': 'wine_bottle'
            },
            'p': (1355, 269),
            'room': 'kitchen'
        },
        'laundry1': {
            'item': {
                'id': 'jacket_red'
            },
            'p': (803,889),
            'room': 'laundry'
        },
        'laundry2': {
            'item': {
                'id': 'jacket_darkblue'
            },
            'p': (902,731),
            'room': 'laundry'
        },
        'laundry3': {
            'item': {
                'id': 'jacket_black'
            },
            'p': (558,420),
            'room': 'laundry'
        },
        'laundry4': {
            'item': {
                'id': 'jacket_darkgreen'
            },
            'p': (562,182),
            'room': 'laundry'
        },
        'gr_l1': {
            'item': {
                'id': 'candle_lit'
            },
            'p': (795, 275),
            'room': 'guestroom l'
        }
    }
}
