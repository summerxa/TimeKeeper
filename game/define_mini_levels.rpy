default baseButtons = [
    {
        'y': 0.15,
        'act': Show('popup_notes'),
        'im': 'mini/ui/icon_notebook_%s.png'
    },
    {
        'y': 0.35,
        'act': Show('popup_map'),
        'im': 'mini/ui/icon_map_%s.png'
    },
    {
        'y': 0.55,
        'act': Show('popup_onhand'),
        'im': 'mini/ui/icon_onhand_%s.png'
    }
]

default levelInfo = {
    1: {
        't0': 1020,
        'tf': 1200,
        'info': '''Info about the time needed for each task.\n\n\n\n\n\n\n\n\n\n\n\n\nAlso did you know this textbox has a scroll bar? :D''',
        'tstairs': 2,
        'nfloors': 2,
        'alldishes': 8
    }
}

default levelHints = {
    1: {
        'start': "Welcome.",
        'grabdishes_fail': "imagine having your hands full and not being able to pick up dishes smh",
        'dropdishes_fail': "you're not even holding dishes in your inventory?? what???",
        'default_idle': "No task available right now.",
        'test_idle': "A custom idle message."
    }
}

default roomButtons = {
    1: {
        'ballroom': {
            'name': 'BALLROOM',
            'floor': 0,
            'num': 0,
            'xp': 0.5,
            'yp': 0.2,
        },
        'kitchen': {
            'name': 'KITCHEN',
            'floor': 0,
            'num': 1,
            'xp': 0.6,
            'yp': 0.7
        },
        'laundry': {
            'name': 'LAUNDRY',
            'floor': 0,
            'num': 2,
            'xp': 0.35,
            'yp': 0.7
        },
        'room 4': {
            'name': 'ROOM 4',
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
        'r11': {
            'xp': 0.5,
            'yp': 0.5,
            'room': 'ballroom',
            'hidden': True,
            'imtask': 'normal'
        },
        'r21': {
            'xp': 0.5,
            'yp': 0.5,
            'room': 'kitchen',
            'imtask': 't2'
        },
        'r31': {
            'xp': 0.5,
            'yp': 0.5,
            'room': 'laundry',
            'imtask': 'normal'
        },
        'r41': {
            'xp': 0.3,
            'yp': 0.7,
            'room': 'kitchen',
            'imtask': 'normal',
            'taskless': 'test_idle'
        }
    }
}

default taskRoots = {
    1: ['t1', 't2']
}

default tasks = {
    1: {
        't1': {
            'name': 't1',
            'desc': 'Clear the table',
            'btn': 'r11',
            'tlabel': 'c1_grabdishes',
            'tcost': 10,
            't0': 1020,
            'tf': 1030,
            'tags': []
        },
        't2': {
            'name': 't2',
            'desc': 'Drop off dirty dishes',
            'btn': 'r21',
            'tlabel': 'c1_dropdishes',
            'tcost': 10,
            't0': -1,
            'tf': 9999,
            'tags': []
        },
        # 't1': {
        #     'name': 't1',
        #     'desc': 'task 1',
        #     'btn': 'r11',
        #     'tlabel': 'c1_t1',
        #     'tcost': 30,
        #     't0': 1020,
        #     'tf': 1025,
        #     'nxt': ['t3'],
        #     'tags': [Task.SPECIAL, Task.NO_REDO]
        # },
        # 't2': {
        #     'name': 't2',
        #     'desc': 'task 2',
        #     'btn': 'r21',
        #     'tlabel': 'c1_t2',
        #     'tcost': 10,
        #     't0': 1050,
        #     'tf': 1060,
        #     'tags': [Task.SPECIAL]
        # },
        # 't3': {
        #     'name': 't3',
        #     'desc': 'task 3',
        #     'btn': 'r31',
        #     'tlabel': 'c1_t3',
        #     'tcost': 5,
        #     't0': -2,
        #     'tf': 1190,
        #     'tags': [Task.NO_REDO]
        # },
        # 't4': {
        #     'name': 't4',
        #     'desc': 'task 4',
        #     'btn': 'r41',
        #     'tlabel': 'c1_t4',
        #     'tcost': 30,
        #     't0': -3,
        #     'dur': 50,
        #     'prq': ['t2', 't3'],
        #     'tags': [Task.SPECIAL]
        # }
    }
}

# normally "air" would be a transparent image but it's visible for testing purposes lol
default itemsAll = {
    'air': {
        'name': 'empty',
        'im': 'mini/btn_item/test_item0_%s.jpg',
        'stackable': False
    },
    'test_3': {
        'name': 'test item 3',
        'im': 'mini/btn_item/test_item3_%s.jpg',
        'stackable': False
    },
    'dirtydishes': {
        'name': 'dirty dishes',
        'im': 'mini/btn_item/test_item1_%s.jpg',
        'stackable': True
    }
}

default itemHolders = {
    1: {
        'r11': {
            'item': {
                'id': 'dirtydishes',
                'stack': 1
            },
            'xp': 0.2,
            'yp': 0.1,
            'room': 'ballroom'
        },
        'r12': {
            'item': {
                'id': 'dirtydishes',
                'stack': 2
            },
            'xp': 0.6,
            'yp': 0.5,
            'room': 'ballroom'
        },
        'r21': {
            'item': {
                'id': 'test_3'
            },
            'xp': 0.6,
            'yp': 0.1,
            'room': 'ballroom'
        },
        'r31': {
            'item': {
                'id': 'test_3'       
            },
            'xp': 0.2,
            'yp': 0.5,
            'room': 'ballroom'
        }
    }
}

default taskGames = {
    1: {
        't1': {
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
        },
        't2': {
            'type': 'dropdishes',
            'xp': 0.8,
            'im': 'mini/icon_map_mc_idle.png',
            'drop': [
                {
                    'n': 'goal','xp': 0.2, 'yp': 0.6, 'im': 'mini/btn_item/test_item0_idle.jpg'
                }
            ],
            'hint': [2, 'this is another hint']
        },
        # 't2': {
        #     'goal': ['left', 'right'],
        #     'drag': [
        #         {
        #             'n': '0', 'xp': 0.2, 'yp': 0.3, 'im': 'mini/button_temp_idle.jpg'
        #         },
        #         {
        #             'n': '1', 'xp': 0.5, 'yp': 0.3, 'im': 'mini/button_temp_idle.jpg'
        #         }
        #     ],
        #     'drop': [
        #         {
        #             'n': 'left', 'xp': 0.2, 'yp': 0.6, 'im': 'mini/test_item0_idle.jpg'
        #         },
        #         {
        #             'n': 'right', 'xp': 0.5, 'yp': 0.6, 'im': 'mini/test_item0_idle.jpg'
        #         }
        #     ],
        #     'hint': [2, 'Drag one of the buttons to the square and drop it']
        # },
        # 't4': {
        #     'type': 'toggle',
        #     'goal': [True, False, True],
        #     'xp': [0.3, 0.5, 0.7],
        #     'yp': [0.5, 0.5, 0.5],
        #     'off': ['mini/button_temp_%s.jpg', 'mini/test_item1_%s.jpg', 'mini/button_temp_%s.jpg'],
        #     'on': ['mini/test_item0_%s.jpg', 'mini/test_item0_%s.jpg', 'mini/test_item0_%s.jpg'],
        #     'hint': [1, 'Click on the items to pick them up/put them down']
        # }
    }
}
