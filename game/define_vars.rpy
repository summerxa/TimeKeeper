init python:
    # --- CHAR MENU
    def char_unlock(c):
        persistent.chars_unlocked[c] = True

    def char_kill(c):
        store.chars_current[c]['alive'] = False
        store.chars_current[c]['small'] = 'small_rip'
        store.chars_current[c]['big'] = 'big_rip'
        store.chars_current[c]['desc'] = 'desc_rip'

default save_version = None

# --- SPRITE HIGHLIGHTING/CONDITION SWITCH ---
default current_speaker = None
default talks_next = None

# --- CONST VALUES FOR UI ---
define popup_zorder = 150
define room_arrow_yoffset = 0.12
define fadetime = 0.5
# ^ 0.0 to skip animation, 0.5 for normal fade in/out

# --- CUSTOM SETTINGS ---
define persistent.showspecial = True # highlights recommended quests if True
define persistent.namesaves = True # prompts user to name save files if True
define persistent.showleavewarning = True # if True, confirm whether you'd like to leave a minigame

# --- MINIGAME STUFF ---
init python:
    from enum import Enum
    class Task(Enum):
        SPECIAL = 0     # task is recommended
        NO_REDO = 1     # can't retry task if failed

default tolabel = ''

default curlevel = 500
default curtime = 0
default tstart = 0
default tlimit = 9999
default completion = 0

default curroom = 'main'
default prevroom = None
default curfloor = 0
default mapfloor = 0

default curtask = None
default curgame = None
default taskq = []
default taskrq = []

default curholder = None
default curhand = -1
default invitems = ['air', 'air']
default invstacks = [1, 1]
default ichoice = None

default notes_text = ''
default notes_text_s = ''

# (not using screen variable b/c will have to redeclare for every screen that uses a button)
default cur_hov = None

default hinttext = 'Welcome.'
default task_failed_return = False

# --- MINIGAME TASK STUFF ---

# default showhint = False

default mgame_try = None
default mgame_goal = None

# --- CHAR MENU ---

default chars_current = {}

define persistent.chars_unlocked = {
    'mc': False,
    'mother': False,
    'amelia': False,
    'bella': False
}
