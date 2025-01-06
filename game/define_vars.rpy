init python:
    # --- CHAR MENU
    def char_unlock(c):
        persistent.chars_unlocked.add(c)
    
    def node_unlock(n_):
        persistent.nodes_unlocked.add(n_)
        nodes_current.add(n_)
    
    def cg_unlock(c_):
        persistent.cgs_unlocked.add(c_)

    def char_kill(c):
        store.chars_current[c]['alive'] = False
    
    def char_addpoints(c, n):
        store.chars_current[c]['points'] += n
        if n < 0:
            renpy.notify(f"{c.title()} is sad :(")
        elif n > 0:
            renpy.notify(f"{c.title()} is happy :D")
    
    def char_getpoints(c):
        return store.chars_current[c]['points']

    def char_relation(c):
        pts = char_getpoints(c)
        return "good" if pts > 0 else ("bad" if pts < 0 else "neutral")

default save_version = None

# --- SPRITE HIGHLIGHTING/CONDITION SWITCH ---
default current_speaker = None
default focus_dict = {}

# --- CUSTOM SETTINGS ---
default persistent.namesaves = True # prompts user to name save files if True
default persistent.showleavewarning = True # if True, confirm whether you'd like to leave a minigame
default persistent.showresetwarning = True # same as above but for resetting minigame progress
default persistent.showversionwarning = True # if True, warns user when they load a diff version save file

# --- STORY STUFF ---

default c1_ending = None
default c1_saw_bella_watch = False
default c1_has_bella_watch = False
default c1_late = False
default c1_amelia_help = False
default c1_amelia_mean = False


# --- MINIGAME STUFF ---
init python:
    from enum import Enum
    class Task(Enum):
        SPECIAL = 0     # task is recommended
        OPTIONAL = 1    # for easter egg tasks
        NO_FADE = 2     # no fadein/fadeout animation
        BONUS = 3       # bonus tasks that add fixed productivity
    
    class Game(Enum):
        DONE = 0        # minigame final goal was achieved
        REFRESH = 1     # game state was updated, need to relaunch window

default tolabel = ''

default curlevel = 1
default curtime = 0

default productivity = 100.0
# cleanliness, coverage, service
default player_attrs = [0, 0, 0]

default curroom = 'main'
default prevroom = None
default curfloor = 0

default curtask = None
default curtask_btn = None
default curgame = None

# if true, the minigame is in tutorial mode and player must click on indicated buttons
default isTutorial = False
default tutStep = 0

# stores fetch quests as a string containing the quest ID
default fetchq = []

# stores infinite tasks as a dictionary entry formatted as:
# 'task ID': {'btn': furniture ID, 'part': part ID (for multi-part tasks only), 't0': start time (for tasks w/ cooldown)}
#   can also contain more data depending on the task (like grab/drop dishes contains the
#       total number of dishes the player must grab/drop off)
default taskq = {}

default curholder = None
default curhand = -1
default invitems = ['air', 'air']
default invstacks = [1, 1]
default ichoice = None

# (not using screen variable b/c will have to redeclare for every screen that uses a button)
default cur_hov = None

default hinttext = 'Welcome.'

# --- MINIGAME TASK STUFF ---

default mgame_try = None
default mgame_goal = None

# --- CHAR MENU ---

default chars_current = {}
default nodes_current = set()

default persistent.chars_unlocked = set()
default persistent.nodes_unlocked = set()
default persistent.cgs_unlocked = set()
