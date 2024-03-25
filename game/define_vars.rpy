init python:
    # --- CHAR MENU
    def char_unlock(c):
        store.chars_current[c]['unlocked'] = True
        persistent.chars_unlocked[c] = True

    def char_kill(c):
        store.chars_current[c]['alive'] = False
        store.chars_current[c]['small'] = 'small_rip'
        store.chars_current[c]['big'] = 'big_rip'
        store.chars_current[c]['desc'] = 'desc_rip'

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

default hinttext = 'Welcome.'

# --- MINIGAME TASK STUFF ---

default showhint = False

default mgame_try = None
default mgame_goal = None

# --- CHAR MENU ---

define persistent.charmenu_data = [
    {
        'id_name': 'mc',
        'disp_name': 'MC',
        'desc_default':
            '''Sophronia is Mother's finest maid: she listens to Mother's every command, completes every task, and makes no mistakes. Will she stay a perfect maid or will she choose another path? How her journey unfolds will be up to you.''',
        'small_default': 'charmenu/small/mc_default_%s.png',
        'big_default': 'charmenu/small/mc_default_idle.png'
    },
    {
        'id_name': 'mother',
        'disp_name': 'Mother',
        'desc_default':
            '''As the head of the Maid Academy, her philosophy is to be the “perfect” woman. In order to achieve her ideals, Mother does not go easy on her “lessons” to the maids, so it's best not to disappoint her. After all, Mother only wants the best for all… right?''',
        'small_default': 'charmenu/small/mother_default_%s.png',
        'big_default': 'charmenu/small/mother_default_idle.png'
    },
    {
        'id_name': 'amelia',
        'disp_name': 'Amelia',
        'desc_default':
            '''Abandoned by her family as a child, Amelia was left at the side of the street, cold and starving, until Mother took her into the Maid Academy. Amelia is incredibly thankful to Mother for giving her a place in the “family”, but it will only last as long as she is useful. 

As a kind and compassionate individual, Amelia is willing to believe in the best of others, but her greatest strength is hindered by her waning courage and fear of abandonment. Are you willing to trust in her kindness more, or are you more doubtful of her wavering resolve?''',
        'desc_rip': '''AMELIA NO!!!''',
        'small_default': 'charmenu/small/amelia_default_%s.png',
        'small_rip': 'charmenu/small/amelia_rip_%s.png',
        'big_default': 'charmenu/small/amelia_default_idle.png',
        'big_rip': 'charmenu/small/amelia_rip_idle.png'
    },
    {
        'id_name': 'bella',
        'disp_name': 'Bella',
        'desc_default':
            '''As an orphan growing up on the streets, Bella was used to having to fend for herself. Survival was her priority: if she had to steal or sacrifice for it, so be it. Her policies hadn't changed when taken into the Maid Academy; she was ready to take the top spot. But there ended up being an exception to her cutthroat nature when Amelia reached out and helped her integrate into the Academy. She was the first person to treat Bella with kindness. Bella's prickly heart softened, and they became fast friends. 

Bella's softer side comes out when it comes to Amelia, but her failing track record with Mother is leaving her desperate. If you aren't Amelia, then you are merely an obstacle to her. Will you choose to befriend her, or will you prefer an adversary to triumph over?''',
        'desc_rip': '''BELLA NO!!!''',
        'small_default': 'charmenu/small/bella_default_%s.png',
        'small_rip': 'charmenu/small/bella_rip_%s.png',
        'big_default': 'charmenu/small/bella_default_idle.png',
        'big_rip': 'charmenu/small/bella_rip_idle.png'
    }
]

default chars_current = {}

define persistent.chars_unlocked = {
    'mc': False,
    'mother': False,
    'amelia': False,
    'bella': False
}
