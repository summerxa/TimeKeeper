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
        'ndishes': 29,
        'level_threshold': [10, 10, 25], # cleanliness, coverage, service
        'mother_threshold': [20, 40], # below first value is bad, below second value is mid
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
    'quest_idle': "I should help the nobles before working on other tasks.",
    'default_taskless': "No task available right now.",
    'candle_taskless': "These candles are already lit.",
    'handsfull_fail': "My hands are full; I can't pick up any more items.",
    'grabdishes_idle': "Drag the dishes to me :3",
    'dropdishes_fail': "you're not even holding dishes in your inventory?? what???",
    'dropdishes_idle': "Dirty dish tower!!!!",
    'toggle_idle': "Meow",
    'waterpour_idle': "Time to cook :3",
    'waterpour_cup_full': "This glass is full; I can't pour into it.",
    'laundry_idle': "Woahhh it's laundry :o",
    'dropfood_fail': "ur not even holding food smh",
    'lightcandle_fail': "i need matches to light the candle :("
}

default helpText = {
    'main': ['''{size=40}{b}BASIC GAMEPLAY{/b}{/size}
Manage your time wisely and complete tasks before time runs out!
{b}Click{/b} on the name of a room to go to it, or the {b}up/down arrows{/b} on the left to go up/down stairs.
{b}Highlighted{/b} furniture means there's a {b}task{/b} you need to complete.
{b}Click{/b} on an item to pick it up, or a {b}hand icon{/b} to place one down. Only {b}one{/b} item can be carried in {b}each{/b} hand, so you may need to {b}drop{/b} an item before picking up another.
{b}Hovering{/b} over a task or item will show {b}information{/b} about it.

{size=40}{b}LEFT SIDEBAR{/b}{/size}
{b}Clock{/b}: shows the {b}current time{/b} and how long you have left.
{b}Notebook{/b}: shows your current {b}tasks{/b}.''',
'''>{b}Check{/b} this tab often, as {b}new tasks{/b} could appear at any time.
Some {b}tasks{/b} are related to the {b}story{/b} and will be written in {i}italics{/i}.
{b}Remove{/b} this feature by {b}unchecking{/b} "highlight recommended tasks" in {b}settings{/b}.''',
'''{b}Map{/b}: previews every floor map.''',
'''>{b}Locates{/b} a task without physically moving to another room to {b}save time{/b}!''',
'''{b}On-hand{/b}: shows the contents of your inventory.
{b}Help{/b}: shows this popup!''',
'''>Contents of this popup will change based on {b}current activity{/b}.
If currently in a {b}task minigame{/b}, it will show {b}instructions{/b} on how to complete the task in addition to this text.''',
'''{b}Leave{/b}: {b}exits{/b} current game state.''',
'''>If in a {b}main floor{/b} map, pauses the game and opens the save menu.
If in a {b}room{/b} map, exits to the main floor map.
If using the {b}preview{/b} map, closes the map and returns to normal gameplay.
If in a {b}task minigame{/b}, causes you to leave the task. {b}Be careful{/b}: leaving a task will take time even if not completed!''',
'''{size=40}{b}COMPLETION{/b}{/size}
{b}Notebook{/b} will show {b}completion progress{/b} using two separate displays.''',
'''>First one is an {b}approval rating{/b}. Pay attention to this, as your {b}final approval rating{/b} may {b}affect the actions{/b} of other characters!
Failing to complete certain tasks will {b}lower approval rating{/b}, while succeeding {b}raises{/b} it.
Certain tasks will be labeled as {b}"bonus tasks"{/b}. Completing these tasks will {b}award approval points{/b}, but {b}will not subtract points{/b} if left undone.''',
'''The second one shows how many {b}major quests{/b} are completed.''',
'''>These quests are related to the {b}story{/b}, and completing them is {b}recommended{/b} for the {b}best story experience{/b}.'''
],
    'grabdishes': ['''Drag a dirty dish from table to pick it up and place into inventory.

To complete the task, collect all dirty dishes from the table.'''],
    'dropdishes': ['''Drag a dirty dish from the stack into the sink, which removes the dishes from inventory.

Dirty dishes can be dropped off at any time, but the task will only be completed after every single dish is dropped off.'''],
    'waterpour': ['''Click on a cup to select it, and click again to deselect it.

Click on another cup to pour the topmost layer of water into it.

You can only pour into a cup if it has at least one empty slot.

Two or more cups cannot contain the same color.

To complete the task, {b}sort{/b} the drinks until {b}each{/b} cup is either {b}empty{/b} or contains {b}all{/b} of one color.'''],
    'sortlaundry': ['''Drag each article of clothing into the {b}correct{/b} washing machine.
Each {b}washing machine{/b} is set for a {b}certain{/b} amount of time.
{b}Light{/b} clothing needs to be washed for the {b}least{/b} amount of time.
{b}Heavy{/b} clothing needs to be washed for the {b}most{/b} amount of time.
{b}Medium{/b} clothing {b}cannot{/b} be washed for {b}too long{/b} or {b}too short{/b}.''']
}

default infoText = {
    'notes': ['''Notebook shows all current tasks.''',
'''>{b}Check{/b} this tab often, as {b}new tasks{/b} could appear at any time.
Some {b}tasks{/b} are related to the {b}story{/b} and will be written in {i}italics{/i}.
{b}Remove{/b} this feature by {b}unchecking{/b} "highlight recommended tasks" in {b}settings{/b}.''',
'''
{b}Notebook{/b} will show {b}completion progress{/b} using two separate displays.''',
'''>First one is an {b}approval rating{/b}. Pay attention to this, as your {b}final approval rating{/b} may {b}affect the actions{/b} of other characters!
Failing to complete certain tasks will {b}lower approval rating{/b}, while succeeding {b}raises{/b} it.
Certain tasks will be labeled as {b}"bonus tasks"{/b}. Completing these tasks will {b}award approval points{/b}, but {b}will not subtract points{/b} if left undone.''',
'''The second one shows how many {b}major quests{/b} are completed.''',
'''>These quests are related to the {b}story{/b}, and completing them is {b}recommended{/b} for the {b}best story experience{/b}.'''],
    'onhand': ['''{b}Pick up items{/b} by finding them around the map or by completing certain tasks.

You can only hold {b}two items{/b} at a time, so use {b}hand icon{/b} around the map to keep track of all your items!

{b}Stackable items{/b}, like empty plates, will only count as 1 item once stacked.
'''],
    'trade': ['''Normally, grabbing or dropping an item will be done automatically when clicking on an item.
    
However, if both of your hands are full, you will be prompted to choose which item you want to remove from your inventory.
''']
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
            'imtask': 'kitchen_pickup'
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
        },
        'gr_l_candle1': {
            'p': (592, 275),
            'room': 'guestroom l',
            'imtask': 'candle',
            'taskless': 'candle_taskless'
        },
        'gr_l_candle2': {
            'p': (1115, 796),
            'room': 'guestroom l',
            'imtask': 'candle',
            'taskless': 'candle_taskless'
        },
        'gr_l_candle3': {
            'p': (398, 796),
            'room': 'guestroom l',
            'imtask': 'candle',
            'taskless': 'candle_taskless'
        },
        'gr_r_candle1': {
            'p': (795, 796),
            'room': 'guestroom r',
            'imtask': 'candle',
            'taskless': 'candle_taskless'
        },
        'gr_r_candle2': {
            'p': (1320, 275),
            'room': 'guestroom r',
            'imtask': 'candle',
            'taskless': 'candle_taskless'
        }
    }
}

default taskTemplates = {
    'donothing': {
        't0': -1,
        'tf': 9999,
        'desc': 'Optional: Sit in the corner and do nothing',
        'tlabel': 'task_c1_donothing',
        'scorebonus': 0,
        'scorepenalty': 0,
        'tags': [Task.DONOTHING, Task.NON_ROOT]
    },
    'fetchquest': {
        'tcost': 10,
        'type': 'none',
        'attributes': [0,0,0]
    },
    'fetchquest_end': {
        'tcost': 10,
        'type': 'medium',
        'attributes': [1,1,3]
    },
    'grabdishes': {
        'tcost': 5,
        'type': 'none',
        'desc': 'Clear the table',
        'tlabel': 'task_c1_grabdishes',
        'fail_id': 'handsfull_fail',
        'item_req': ['air', 'dish_dirty'],
        'attributes': [0,0,0],
        'nxt': 'dropdishes'
        # after completing this part, next generated task will be of type "dropdishes"
    },
    'dropdishes': {
        'tcost': 5,
        'type': 'medium',
        'desc': 'Drop off dirty dishes',
        'tlabel': 'task_c1_dropdishes',
        'fail_id': 'dropdishes_fail',
        'item_req': ['dish_dirty'],
        'attributes': [3,1,1],
        'nxt': 'grabdishes'
    },
    'waterpour': {
        'tcost': 20,
        'type': 'large',
        'desc': 'Pour drinks at the bar',
        'tlabel': 'task_c1_waterpour',
        'attributes': [1,3,6]
    },
    'sortlaundry': {
        'tcost': 20,
        'type': 'large',
        'tlabel': 'task_c1_sortlaundry',
        'desc': 'Sort the laundry',
        'attributes': [4,4,2]
    },
    'grabfood': {
        'tcost': 5,
        'type': 'none',
        'tlabel': 'task_c1_grabfood',
        'desc': 'Pick up finished dishes',
        'tags': [Task.NO_FADE],
        'fail_id': 'handsfull_fail',
        'item_req': ['air'],
        'attributes': [0,0,0],
        'nxt': 'dropfood'
    },
    'dropfood': {
        'tcost': 5,
        'type': 'medium',
        'tlabel': 'task_c1_dropfood',
        'desc': 'Drop off finished dishes',
        'tags': [Task.NO_FADE],
        'fail_id': 'dropfood_fail',
        'item_req': ['food'],
        'attributes': [1,2,2],
        'nxt': 'grabfood'
    },
    'lightcandle': {
        'tcost': 1,
        'type': 'small'
        'tlabel': 'task_c1_lightcandle',
        'desc': 'Light the candles',
        'item_req': ['matches'],
        'fail_id': 'lightcandle_fail',
        'tags': [Task.NO_FADE],
        'attributes': [0,0,1]
    }
}

default tasks = {
    1: {
        'donothing': {
            'btn': '4_1',
            'tcost': 180,
            'game': {'type': 'donothing'}
        },
        'fetch1': {
            'desc': 'Talk to noble',
            'btn': '4_5',
            'tlabel': 'c1_fetch1',
            't0': 1100,
            'tags': [Task.SPECIAL],
            'nxt': ['fetch1_end'],
            'game': {'type': 'fetchquest'}
        },
        'fetch1_end': {
            'desc': 'Bring wine to noble',
            'btn': '4_5',
            'tlabel': 'c1_fetch1_end',
            'tags': [Task.SPECIAL, Task.NON_ROOT],
            'game': {'type': 'fetchquest_end'}
        },
        'fetch2': {
            'desc': 'Talk to noble',
            'btn': '6_5',
            'tlabel': 'c1_fetch2',
            't0': 1125,
            'tags': [Task.SPECIAL],
            'nxt': ['fetch2_end'],
            'game': {'type': 'fetchquest'}
        },
        'fetch2_end': {
            'desc': 'Bring jacket to noble',
            'btn': '6_5',
            'tlabel': 'c1_fetch2_end',
            'tags': [Task.SPECIAL, Task.NON_ROOT],
            'game': {'type': 'fetchquest_end'}
        },
        'fetch3': {
            'desc': 'Talk to noble',
            'btn': '6_5',
            'tlabel': 'c1_fetch3',
            't0': 1150,
            'tags': [Task.SPECIAL],
            'nxt': ['fetch3_end'],
            'game': {'type': 'fetchquest'}
        },
        'fetch3_end': {
            'desc': 'Ask the chefs for desserts',
            'btn': 'kitchen_idk',
            'tlabel': 'c1_fetch3_end',
            'tags': [Task.SPECIAL, Task.NON_ROOT],
            'game': {'type': 'fetchquest_end'}
        },
        'fetch4': {
            'desc': 'Talk to noble',
            'btn': 'long1',
            'tlabel': 'c1_fetch4',
            't0': 1170,
            'tags': [Task.SPECIAL],
            'game': {'type': 'fetchquest_end'}
        }
        ### BELOW IS ONLY FOR REFERENCE

        # 'candles_l1': {
        #     'btn': 'gr_l_candle1',
        #     'game': {
        #         'type': 'lightcandle'
        #     }
        # },
        # 'grabdish_1030': {
        #     'btn': '6_2',
        #     't0': 1030,
        #     'game': {
        #         'type': 'grabdishes',
        #         'goal': 5
        #     }
        # },
        # 'grabfood 1030': {
        #     'btn': 'pickuptable',
        #     't0': 1030,
        #     'game': {
        #         'type': 'grabfood'
        #     },
        #     'nxt': ['dropfood 1030']
        # },
        # 'dropfood 1030': {
        #     'btn': '4_3',
        #     't0': -2,
        #     'game': {
        #         'type': 'dropfood'
        #     }
        # },
        # 'waterpour_1': {
        #     'btn': 'bar',
        #     't0': 1050,
        #     'game': {
        #         'type': 'waterpour',
        #         'cups': [
        #             {
        #                 'xp': 0.24,
        #                 'colors': ['#920e0e']
        #             },
        #             {
        #                 'xp': 0.38,
        #                 'colors': ['#920e0e', '#a4f910', '#920e0e', '#eedfab']
        #             },
        #             {
        #                 'xp': 0.52,
        #                 'colors': ['#eedfab', '#a4f910', '#a4f910', '#920e0e']
        #             },
        #             {
        #                 'xp': 0.66,
        #                 'colors': ['#eedfab', '#eedfab', '#a4f910']
        #             }
        #         ]
        #     }
        # },
        # 'laundry_1': {
        #     'btn': 'laundry_1',
        #     't0': 1140,
        #     'game': {
        #         'type': 'sortlaundry'
        #     }
        # },
        # 'dropdish': {
        #     'btn': 'sink',
        #     't0': 1030,
        #     'tf': 1190,
        #     'game': {
        #         'type': 'dropdishes',
        #         'xp': 0.5,
        #         'drop': [
        #             {
        #                 'n': 'goal', 'p': (369, 356), 'w': 784, 'h': 525
        #             }
        #         ],
        #         'in_sink': {
        #             'p': (778, 618), 'im': 'mini/tgame/grab_dropdishes/plate_clean.png'
        #         },
        #         'overlay': [
        #             {
        #                 'p': (678, 413), 'im': 'mini/tgame/grab_dropdishes/dropdishes_faucet.png'
        #             }
        #         ]
        #     }
        # }
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
        'name': 'dark green jacket',
        'desc': 'A dark green jacket with three pockets.',
        'im': 'shirt',
        'stackable': False
    },
    'food': {
        'name': 'plate of food',
        'desc': 'A plate of food.',
        'im': 'food',
        'stackable': False
    },
    'matches': {
        'name': 'box of matches',
        'desc': 'A box of matches. Can be used to light candles.',
        'im': 'matches',
        'stackable': True
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
                'id': 'matches',
                'stack': 5
            },
            'p': (795, 275),
            'room': 'guestroom l'
        }
    }
}
