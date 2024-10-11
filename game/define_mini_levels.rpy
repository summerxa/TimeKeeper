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
        'level_threshold': [25, 25, 25], # cleanliness, coverage, service
        'mother_threshold': [50, 80], # below first value is bad, above second is good, between is mid
        'quests_done': set(),
        'bonus_remaining': 5,
        'room0': 'ballroom',
        'floor0': 0,
        'task_popup_text': """Mother has instructed that your assignment this time should maintain a good balance between cleanliness and coverage, with an emphasis on exceptional service.
        
{b}Should any guest have a request, it is imperative to immediately fulfill it.{/b}"""
    }
}

default levelHints = {
    'default_start': "Welcome.",
    'default_idle': "...",
    'quest_idle': "One of the guests requires assistance. I should go help.",
    'quest_taskless': "I should help the nobles before working on other tasks.",
    'default_taskless': "There aren't any tasks here right now.",
    'candle_taskless': "These candles don't need to be lit right now.",
    'handsfull_fail': "My hands are full; I can't pick up any more items.",
    'grabdishes_idle': "Drag the dishes to me.",
    'dropdishes_fail': "I need to drop off dirty dishes here.",
    'dropdishes_idle': "Drop the dishes off in the sink.",
    'waterpour_idle': "The drinks must be sorted according to color.",
    'waterpour_cup_full': "This glass is full; I can't pour into it.",
    'sortlaundry_idle': "Sort the laundry into separate batches and start the machines.",
    'dropfood_fail': "I need to drop off a meal here.",
    'lightcandle_fail': "I need to find matches before I can light the candle."
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
        'tcost': 9999,
        'tlabel': 'task_c1_donothing',
        'type': 'none',
        'attributes': [0,0,0],
        'tags': [Task.OPTIONAL]
    },
    'fetchquest': {
        'type': 'none',
        'title': "Guest Request",
        'attributes': [0,0,0],
        'tags': [Task.SPECIAL]
    },
    'fetchquest_end': {
        'type': 'medium',
        'title': "Guest Request",
        'attributes': [1,3,1],
        'tags': [Task.SPECIAL]
    },
    'grabdishes': {
        'tcost': 5,
        'type': 'none',
        'desc': 'Clear the table',
        'tlabel': 'task_c1_grabdishes',
        'fail_id': 'handsfull_fail',
        'item_req': ['air', 'dish_dirty'],
        'attributes': [0,0,0],
        'next': 'dropdishes',
        'parent': 'dishes_chain',
        'idle': 'grabdishes_idle'
    },
    'dropdishes': {
        'tcost': 5,
        'type': 'medium',
        'desc': 'Drop off dirty dishes',
        'tlabel': 'task_c1_dropdishes',
        'fail_id': 'dropdishes_fail',
        'item_req': ['dish_dirty'],
        'attributes': [3,3,1],
        'next': 'grabdishes',
        'parent': 'dishes_chain',
        'idle': 'dropdishes_idle'
    },
    'dishes_chain': { # contains all the parts of the "quest chain"
        'type': 'medium',
        'title': "Clean up dirty dishes",
        'sequence': ['grabdishes', 'dropdishes'],
        'desc': 'Clear the ballroom tables, drop off dirty dishes in the kitchen',
        'attributes': [3,3,1]
    },
    'waterpour': {
        'tcost': 20,
        'type': 'large',
        'title': "Help at the bar",
        'desc': "Pour drinks at the ballroom's bar",
        'tlabel': 'task_c1_waterpour',
        'attributes': [2,2,6],
        'idle': 'waterpour_idle',
        'cd': 10
    },
    'sortlaundry': {
        'tcost': 20,
        'type': 'large',
        'title': "Do the laundry",
        'tlabel': 'task_c1_sortlaundry',
        'desc': 'Sort the laundry into the washing machines',
        'attributes': [6,2,2],
        'idle': 'sortlaundry_idle',
        'cd': 10
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
        'next': 'dropfood',
        'parent': 'food_chain'
    },
    'dropfood': {
        'tcost': 5,
        'type': 'medium',
        'tlabel': 'task_c1_dropfood',
        'desc': 'Drop off finished dishes',
        'tags': [Task.NO_FADE],
        'fail_id': 'dropfood_fail',
        'item_req': ['food'],
        'attributes': [1,3,3],
        'next': 'grabfood',
        'parent': 'food_chain'
    },
    'food_chain': {
        'type': 'medium',
        'sequence': ['grabfood', 'dropfood'],
        'title': "Serve the food",
        'desc': 'Pick up finished dishes in the kitchen, drop off dishes in ballroom',
        'tags': [Task.NO_FADE],
        'attributes': [1,3,3]
    },
    'lightcandle': {
        'tcost': 1,
        'type': 'small',
        'tlabel': 'task_c1_lightcandle',
        'title': "Light candles",
        'desc': 'Bonus task: Light the candles in the upstairs guestrooms',
        'item_req': ['matches'],
        'fail_id': 'lightcandle_fail',
        'tags': [Task.NO_FADE, Task.BONUS],
        'attributes': [0,1,0],
        'max_cd': 20
    }
}

default tasks = {
    1: {
        'optional': { # for easter egg quests
            'donothing': {
                't0': 1020,
                'btn': '4_1',
                'tasktype': 'donothing'
            },
        },
        'single': { # for quests that only show up once
            'scene3_end': {
                'tcost': 17,
                'desc': 'Provide room service to guests',
                'btn': 'gr_22',
                'tlabel': 'c1_scene3',
                't0': 1031,
                'tasktype': 'fetchquest_end'
            },
            'fetch1': {
                'tcost': 5,
                'desc': 'Talk to noble',
                'btn': '4_5',
                'tlabel': 'c1_fetch1',
                't0': 1100,
                'next': 'fetch1_end',
                'tasktype': 'fetchquest'
            },
            'fetch1_end': {
                'tcost': 5,
                'desc': 'Bring wine to noble',
                'btn': '4_5',
                'tlabel': 'c1_fetch1_end',
                'tasktype': 'fetchquest_end'
            },
            'fetch2': {
                'tcost': 5,
                'desc': 'Talk to noble',
                'btn': '6_5',
                'tlabel': 'c1_fetch2',
                't0': 1125,
                'next': 'fetch2_end',
                'tasktype': 'fetchquest'
            },
            'fetch2_end': {
                'tcost': 5,
                'desc': 'Bring jacket to noble',
                'btn': '6_5',
                'tlabel': 'c1_fetch2_end',
                'tasktype': 'fetchquest_end'
            },
            'fetch3': {
                'tcost': 5,
                'desc': 'Talk to noble',
                'btn': '6_3',
                'tlabel': 'c1_fetch3',
                't0': 1150,
                'next': 'fetch3_end',
                'tasktype': 'fetchquest'
            },
            'fetch3_end': {
                'tcost': 5,
                'desc': 'Ask the chefs for desserts',
                'btn': 'kitchen_idk',
                'tlabel': 'c1_fetch3_end',
                'tasktype': 'fetchquest_end'
            },
            'fetch4_end': {
                'tcost': 5,
                'desc': 'Talk to noble',
                'btn': 'long1',
                'tlabel': 'c1_fetch4',
                't0': 1170,
                'tasktype': 'fetchquest_end'
            }
        },
        'infinite': { # tasks that are infinitely generated
            'dishes_chain': {
                'btns': {
                    'grabdishes': ['4_2', '4_3', '4_4', '4_5', '4_6', 'long2', '6_1', '6_2', '6_4', '6_6', '6_7', '6_9', '6_10'],
                    'dropdishes': ['sink']
                }
            },
            'waterpour': {
                'btns': ['bar']
            },
            'sortlaundry': {
                'btns': ['laundry_1']
            },
            'food_chain': {
                'btns': {
                    'grabfood': ['pickuptable'],
                    'dropfood': ['4_2', '4_3', '4_4', '4_5', '4_6', 'long2', '6_1', '6_2', '6_4', '6_6', '6_7', '6_9', '6_10']
                }
            },
            'lightcandle': {
                'btns': ['gr_l_candle1', 'gr_l_candle2', 'gr_l_candle3', 'gr_r_candle1', 'gr_r_candle2']
            }
        }
    }
}

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
        'name': 'red jacket with gold trim',
        'desc': 'A red jacket with golden trim.',
        'im': 'shirt',
        'stackable': False
    },
    'jacket_darkblue': {
        'name': 'dark blue jacket with silver trim',
        'desc': 'A dark blue jacket with silver trim.',
        'im': 'shirt',
        'stackable': False
    },
    'jacket_black': {
        'name': 'black jacket with light gold trim',
        'desc': 'A black jacket with light gold trim.',
        'im': 'shirt',
        'stackable': False
    },
    'jacket_darkgreen': {
        'name': 'dark green jacket with three pockets',
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
                'id': 'matches',
                'stack': 2
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
        'jacketred': {
            'item': {
                'id': 'jacket_red'
            },
            'p': (793,263),
            'room': 'guestroom r'
        },
        'jacketblue': {
            'item': {
                'id': 'jacket_darkblue'
            },
            'p': (1314,264),
            'room': 'guestroom l'
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
                'stack': 3
            },
            'p': (795, 275),
            'room': 'guestroom l'
        }
    }
}

default tutorialText = [
    {
        'text': "A good maid must fulfill the expectations of her clients.",
        'btn': 'none',
        'mask': (0,0,0,0),
        'pos': (719, 396) # CENTER OF SCREEN
    },
    {
        'text': "By the end of the day, I {b}MUST{/b} reach the {b}three attribute goals{/b} listed here.",
        'btn': 'none',
        'mask': (1510,16,1891,192),
        'pos': (961, 37)
    },
    {
        'text': "These attributes all begin at 0. If I do not fill up the bar and reach these goals by the deadline, I will {b}INSTANTLY FAIL{/b}.",
        'btn': 'none',
        'mask': (1510,16,1891,192),
        'pos': (961, 37)
    },
    {
        'text': "First, check the notebook.",
        'btn': 'notes_btn',
        'mask': (75,344,197,465),
        'pos': (246, 286)
    },
    {
        'text': "Doing the tasks listed in the notebook can help me reach the goals.",
        'btn': 'none',
        'mask': (0,0,1920,1080),
        'pos': (719, 396)
    },
    {
        'text': "Each task gives a different amount of points toward the 3 attributes, so I must choose a selection of different tasks to achieve the 3 goals.",
        'btn': 'none',
        'mask': (0,0,1920,1080),
        'pos': (719, 396)
    },
    {
        'text': "For example, the laundry task gives a lot of cleanliness and coverage points...",
        'btn': 'none',
        'mask': (1345,561,1475,612),
        'pos': (468, 555)
    },
    {
        'text': "...while the bar task gives a lot of service points.",
        'btn': 'none',
        'mask': (1468,402,1538,450),
        'pos': (468, 394)
    },
    {
        'text': "I’ll start by gathering the dirty dishes. This task is located in the ballroom and takes 5 minutes to complete.",
        'btn': 'none',
        'mask': (998,205,1553,395),
        'pos': (468, 175)
    },
    {
        'btn': 'popup_button_close',
        'mask': (1636,65,1709,138),
        'pos': (1138, 86)
    },
    {
        'text': "I can use the map to navigate the building.",
        'btn': 'map_btn',
        'mask': (75,489,197,603),
        'pos': (273, 398)
    },
    {
        'text': "This map will show the general location of rooms and tasks.",
        'btn': 'none',
        'mask': (0,0,1920,1080),
        'pos': (719, 30) # CENTER TOP
    },
    {
        'text': "Use these buttons to navigate to other floors of the building.",
        'btn': 'floor_up_btn',
        'mask': (245,464,292,509),
        'pos': (312, 277)
    },
    {
        'text': "To continue doing tasks, exit the map.",
        'btn': 'leave_btn',
        'mask': (75,957,197,1060),
        'pos': (260, 771)
    },
    {
        'text': "Click on the name of a room to enter it. We are going to the ballroom.",
        'btn': 'ballroom',
        'mask': (778,244,1165,418),
        'pos': (719, 402)
    },
    {
        'text': "Start a task by clicking on a highlighted piece of furniture.",
        'btn': 'none',
        'mask': (1054,273,1306,833),
        'pos': (719, 30)
    },
    {
        'text': "To see more of a room, drag or scroll to move it left and right.",
        'btn': 'none',
        'mask': (0,0,0,0),
        'pos': (719, 30)
    },
    {
        'text': "Hovering over certain buttons will show a brief description.",
        'btn': 'none',
        'mask': (1335,740,1859,1040),
        'pos': (1350, 438)
    },
    {
        'text': "Now find a table that needs to be cleared.",
        'btn': '6_1',
        'mask': (0,0,1920,1080),
        'pos': (719, 30),
        'draggable': True
    },
    {
        'text': "Instructions on how to complete a task can be found here. Be sure to check the instructions whenever you see an unfamiliar task.",
        'btn': 'help_btn',
        'mask': (75,788,197,898),
        'pos': (257, 681)
    },
    {
        'text': "After reading the rules, exit the help menu to continue doing the task.",
        'btn': 'popup_button_close',
        'mask': (1346,207,1402,275),
        'pos': (828, 20)
    },
    {
        'btn': 'gameplay'
    },
    {
        'text': "Hover over the clock to see the current time.",
        'btn': 'none',
        'mask': (0,0,1920,1080),
        'pos': (275, 58)
    },
    {
        'text': "Doing tasks will take up time. I must manage my time wisely to reach clients’ expectations.",
        'btn': 'none',
        'mask': (0,0,1920,1080),
        'pos': (275, 58)
    },
    {
        'text': "Now open the notebook again.",
        'btn': 'notes_btn',
        'mask': (75,344,197,465),
        'pos': (246, 286)
    },
    {
        'text': "After collecting all the dirty dishes, I must now bring them to the kitchen.",
        'btn': 'none',
        'mask': (998,205,1553,395),
        'pos': (468, 175)
    },
    {
        'btn': 'popup_button_close',
        'mask': (1636,65,1709,138),
        'pos': (1138, 86)
    },
    {
        'text': "First, we must go to the kitchen.",
        'btn': 'to_kitchen_btn',
        'mask': (1042,912,1261,1036),
        'pos': (886, 620)
    },
    {
        'text': "Make sure to always keep an eye on the clock. Even walking to a different room takes time.",
        'btn': 'none',
        'mask': (0,0,1920,1080),
        'pos': (275, 58)
    },
    {
        'text': "Now drop off the dirty dishes from the ballroom in the sink.",
        'btn': 'sink',
        'mask': (0,0,1920,1080),
        'pos': (719, 30),
        'draggable': True
    },
    {
        'btn': 'gameplay'
    },
    {
        'text': "After completing the task, I have made progress towards my target attributes. Remember that all of these goals {b}MUST{/b} be achieved before the end of the day.",
        'btn': 'none',
        'mask': (1510,16,1891,192),
        'pos': (961, 37)
    },
    {
        'text': "Sometimes, a task will require me to use certain items, such as this bottle of wine on the counter.",
        'btn': 'none',
        'mask': (1315,214,1392,319),
        'pos': (787, 143)
    },
    {
        'text': "Hovering over an item will explain what it is. Try picking up the bottle of wine.",
        'btn': 'kitchen2',
        'mask': (0,0,1920,1080),
        'pos': (787, 143)
    },
    {
        'text': "Click here to check what I’m holding.",
        'btn': 'onhand_btn',
        'mask': (75,625,197,764),
        'pos': (245, 556)
    },
    {
        'text': "I’m holding the bottle of wine that I just picked up.",
        'btn': 'none',
        'mask': (0,0,1920,1080),
        'pos': (873, 217)
    },
    {
        'btn': 'popup_button_close',
        'mask': (1238,354,1308,427),
        'pos': (1315, 230)
    },
    {
        'text': "Select an empty spot to place down items.",
        'btn': 'kitchen2',
        'mask': (1315,214,1392,319),
        'pos': (787, 143)
    },
    {
        'text': "Let's pick up the wine again.",
        'btn': 'kitchen2',
        'mask': (1315,214,1392,319),
        'pos': (787, 143)
    },
    {
        'text': "And the matches.",
        'btn': 'kitchen1',
        'mask': (355,229,431,300),
        'pos': (468, 300)
    },
    {
        'text': "Try placing down one item in this empty spot.",
        'btn': 'kitchen2',
        'mask': (1315,214,1392,319),
        'pos': (787, 143)
    },
    {
        'text': "If I’m holding items on both hands, I’ll have to choose which item I want to place down.",
        'btn': 'none',
        'mask': (0,0,1920,1080),
        'pos': (719, 30)
    },
    {
        'text': "Choose either item to place down.",
        'btn': 'idk',
        'mask': (0,0,1920,1080),
        'pos': (719, 30)
    },
    {
        'text': "I should complete more tasks now, but it looks like there's nothing to do.",
        'btn': 'none',
        'mask': (0,0,1920,1080),
        'pos': (719, 30)
    },
    {
        'text': "I can check the notebook to find other tasks.",
        'btn': 'notes_btn',
        'mask': (75,344,197,465),
        'pos': (246, 286)
    },
    {
        'text': "Occasionally, clients will have specific requests which take priority over other tasks.",
        'btn': 'none',
        'mask': (290,542,913,818),
        'pos': (232, 249)
    },
    {
        'text': "I cannot start other tasks until I assist the guests. This time, I am providing room service in the guestrooms.",
        'btn': 'none',
        'mask': (290,542,913,818),
        'pos': (232, 249)
    },
    {
        'btn': 'popup_button_close',
        'mask': (1636,65,1709,138),
        'pos': (1138, 86)
    },
    {
        'text': "We should go upstairs to the guestrooms.",
        'btn': 'floor_up_btn',
        'mask': (245,464,292,509),
        'pos': (312, 277)
    },
    {
        'text': "This task is in the right guestrooms.",
        'btn': 'guestroom r',
        'mask': (0,0,1920,1080),
        'pos': (719, 30)
    },
    {
        'text': "The room we’re looking for is highlighted.",
        'btn': 'gr_22',
        'mask': (0,0,1920,1080),
        'pos': (719, 30),
        'draggable': True
    },
    {
        'text': "There are still many tasks to do before eight o’clock.",
        'btn': 'none',
        'mask': (0,0,0,0),
        'pos': (719, 396)
    },
    {
        'text': "I should manage my time wisely to meet the goals assigned by Mother.",
        'btn': 'none',
        'mask': (0,0,0,0),
        'pos': (719, 396)
    },
    {
        'text': "The notebook lists the attribute points that different tasks give so it is wise to constantly check it.",
        'btn': 'none',
        'mask': (0,0,0,0),
        'pos': (719, 396)
    },
    {
        'text': "Remember, if I DO NOT reach the 3 attribute goals before the end of the day, it will be considered {b}INSTANT FAILURE{/b}.",
        'btn': 'none',
        'mask': (0,0,0,0),
        'pos': (719, 396)
    }
]

default helpText = {
    'main': ['''{size=30}{b}BASIC GAMEPLAY{/b}{/size}
Manage your time wisely and complete tasks before time runs out!
{b}Click{/b} on the name of a room to go to it, or the {b}up/down arrows{/b} on the left to go up/down stairs.
{b}Highlighted{/b} furniture means there's a {b}task{/b} you need to complete.
{b}Click{/b} on an item to pick it up, or a {b}hand icon{/b} to place one down. Only {b}one{/b} item can be carried in {b}each{/b} hand, so you may need to {b}drop{/b} an item before picking up another.
{b}Hovering{/b} over a task or item will show {b}information{/b} about it.

{size=30}{b}LEFT SIDEBAR{/b}{/size}
{b}Clock{/b}: shows the {b}current time{/b} and how long you have left.
{b}Notebook{/b}: shows your current {b}tasks{/b}.''',
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
'''
{size=30}{b}COMPLETION{/b}{/size}
{b}Completing{/b} a task grants a certain amount of {b}points{/b} for each of the {b}three attributes{/b}.
The {b}top right corner{/b} shows your {b}progress{/b} towards the attribute goals. Not reaching these goals results in {b}instant failure{/b}.'''
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
    'sortlaundry': ['''Drag {b}each{/b} article of clothing into the {b}correct{/b} washing machine.
Click the {b}start{/b} button to {b}set the time{/b} for each machine.
{b}Light{/b} clothing (undergarment, gloves, tie) needs to be washed for the {b}least{/b} amount of time.
{b}Heavy{/b} clothing (coat, suit, gown) needs to be washed for the {b}most{/b} amount of time.
{b}Medium{/b} clothing (shirt, blouse, pants) {b}cannot{/b} be washed for {b}too long{/b} or {b}too short{/b}.''']
}

default infoText = {
    'notes': ['''Notebook shows all current tasks.''',
'''{b}Completing{/b} a task grants a certain amount of {b}points{/b} for each of the {b}three attributes{/b}.''',
'''The {b}top right corner{/b} shows your {b}progress{/b} towards the attribute goals. Not reaching these goals results in {b}instant failure{/b}.'''],
    'onhand': ['''{b}Pick up items{/b} by finding them around the map or by completing certain tasks.

You can only hold {b}two items{/b} at a time, so use {b}hand icon{/b} around the map to keep track of all your items!

{b}Stackable items{/b}, like empty plates, will only count as 1 item once stacked.
'''],
    'trade': ['''Normally, grabbing or dropping an item will be done automatically when clicking on an item.
    
However, if both of your hands are full, you will be prompted to choose which item you want to remove from your inventory.
''']
}
