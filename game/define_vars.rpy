# --- MODIFYING CHARACTER MENU ---
init python:
    def char_unlock(c):
        store.charmenu_current[c]['unlocked'] = True
        persistent.charmenu_saved[c]['unlocked'] = True

    def char_kill(c):
        store.charmenu_current[c]['alive'] = False
        store.charmenu_current[c]['small'] = 'small_rip'
        store.charmenu_current[c]['big'] = 'big_rip'
        store.charmenu_current[c]['desc'] = 'desc_rip'

        persistent.charmenu_saved[c]['alive'] = False
        persistent.charmenu_saved[c]['small'] = 'small_rip'
        persistent.charmenu_saved[c]['big'] = 'big_rip'
        persistent.charmenu_saved[c]['desc'] = 'desc_rip'

# --- SPRITE HIGHLIGHTING/CONDITION SWITCH ---
default current_speaker = None
default talks_next = None

# --- CONST VALUES FOR UI ---
define popup_zorder = 150
define room_arrow_yoffset = 0.12

# --- CUSTOM SETTINGS ---
define persistent.showspecial = False # highlights recommended quests if True
define persistent.namesaves = True # prompts user to name save files if True
define persistent.showleavewarning = True # if True, confirm whether you'd like to leave a minigame

# --- MINIGAME STUFF ---
init python:
    from enum import Enum
    class Task(Enum):
        SPECIAL = 0     # task is recommended
        NO_REDO = 1     # can't retry task if failed

default mini_fadeout = False
default tolabel = ''

default curlevel = 500
default curtime = 0
default tstart = 0
default tlimit = 9999

default curroom = 'main'
default prevroom = None
default curfloor = 0
default mapfloor = 0

default curtask = None
default taskq = []
default taskrq = []

default curholder = None
default curhand = -1
default invitems = ['air', 'air']
default invstacks = [1, 1]
default ichoice = None

default notes_text = ''
default notes_text_s = ''

default hinttext = 'Welcome.'

# --- MINIGAME INSIDE THE MINIGAME STUFF ---

default showhint = False

default mgame_try = None
default mgame_goal = None

# --- CHARACTERS ---

define persistent.charmenu_data = [
    {
        'id_name': 'mc',
        'disp_name': 'MC',
        'desc_default': '''Description for MC''',
        'small_default': 'charmenu/small/mc_default_%s.png',
        'big_default': 'charmenu/small/mc_default_idle.png'
    },
    {
        'id_name': 'mother',
        'disp_name': 'Mother',
        'desc_default': '''Mother :3''',
        'small_default': 'charmenu/small/mother_default_%s.png',
        'big_default': 'charmenu/small/mother_default_idle.png'
    },
    {
        'id_name': 'amelia',
        'disp_name': 'Amelia',
        'desc_default': '''i want to adopt her''',
        'desc_rip': '''AMELIA NO!!!''',
        'small_default': 'charmenu/small/amelia_default_%s.png',
        'small_rip': 'charmenu/small/amelia_rip_%s.png',
        'big_default': 'charmenu/small/amelia_default_idle.png',
        'big_rip': 'charmenu/small/amelia_rip_idle.png'
    },
    {
        'id_name': 'bella',
        'disp_name': 'Bella',
        'desc_default': '''hi bella!!!''',
        'desc_rip': '''BELLA NO!!!''',
        'small_default': 'charmenu/small/bella_default_%s.png',
        'small_rip': 'charmenu/small/bella_rip_%s.png',
        'big_default': 'charmenu/small/bella_default_idle.png',
        'big_rip': 'charmenu/small/bella_rip_idle.png'
    }
]

default charmenu_current = {}

define persistent.charmenu_saved = {
    'mc': {
        'desc': 'desc_default',
        'small': 'small_default',
        'big': 'big_default',
        'alive': True,
        'unlocked': False,
        'friend': False,
        'friendlvl': 0
    },
    'mother': {
        'desc': 'desc_default',
        'small': 'small_default',
        'big': 'big_default',
        'alive': True,
        'unlocked': False,
        'friend': False,
        'friendlvl': 0
    },
    'amelia': {
        'desc': 'desc_default',
        'small': 'small_default',
        'big': 'big_default',
        'alive': True,
        'unlocked': False,
        'friend': False,
        'friendlvl': 0
    },
    'bella': {
        'desc': 'desc_default',
        'small': 'small_default',
        'big': 'big_default',
        'alive': True,
        'unlocked': False,
        'friend': False,
        'friendlvl': 0
    }
}
