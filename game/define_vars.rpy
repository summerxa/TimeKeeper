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

default notes_tab = 'tasks'
default notes_text = ''
default notes_text_s = ''

default hinttext = 'Welcome.'

# --- MINIGAME INSIDE THE MINIGAME STUFF ---

default showhint = False

default mgame_try = None
default mgame_goal = None
