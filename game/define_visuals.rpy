# --- UI STUFF ---

# keep an image rotated to angle "a"
transform rot(a):
    rotate a

style fancy_font:
    color '#000'
    font 'Bodoni-16-Medium.otf'

# --- SPRITE STUFF ---

# used to shade sprites that aren't talking
transform darken_sprite:
    # matrixcolor ContrastMatrix(0.9) * BrightnessMatrix(-0.2)
    matrixcolor TintMatrix('#aaaaaa')

init python:
    import functools
    def set_cur_speaker(event, interact=True, ch=None, **kwargs):
        global current_speaker

        if not interact:
            return

        if event == 'show':
            current_speaker = ch
    
    def make_comp(charname, imwidth, headheight, face, pose):
        imface = f"spr_{charname}/{face}.png"
        impose = f"spr_{charname}/{pose}.png"
        return Composite((imwidth, 1080), (0, 0), imface, (0, headheight), impose)

    def make_cs(charname, imname, has_talk=False):
        silent = f"{charname} {imname} s"
        talking = f"{charname} {imname} {'t' if has_talk else 's'}"
        return ConditionSwitch(f"current_speaker == '{charname}'", talking, "True", At(silent, darken_sprite))

image mc 1a s = make_comp('mc', 641, 386, '01', '0a')
image mc 1a t = make_comp('mc', 641, 386, '01t', '0a')
image mc 1a = make_cs('mc', '1a', True)
image mc 2a s = make_comp('mc', 641, 386, '02', '0a')
image mc 2a = make_cs('mc', '2a')
image mc 3a s = make_comp('mc', 641, 386, '03', '0a')
image mc 3a t = make_comp('mc', 641, 386, '03t', '0a')
image mc 3a = make_cs('mc', '3a', True)
image mc 4a s = make_comp('mc', 641, 386, '04', '0a')
image mc 4a = make_cs('mc', '4a')
image mc 5a s = make_comp('mc', 641, 386, '05', '0a')
image mc 5a t = make_comp('mc', 641, 386, '05t', '0a')
image mc 5a = make_cs('mc', '5a', True)
image mc 6a s = make_comp('mc', 641, 386, '06', '0a')
image mc 6a t = make_comp('mc', 641, 386, '06t', '0a')
image mc 6a = make_cs('mc', '6a', True)

image mc 1b s = make_comp('mc', 641, 386, '01', '0b')
image mc 1b t = make_comp('mc', 641, 386, '01t', '0b')
image mc 1b = make_cs('mc', '1b', True)
image mc 2b s = make_comp('mc', 641, 386, '02', '0b')
image mc 2b = make_cs('mc', '2b')
image mc 3b s = make_comp('mc', 641, 386, '03', '0b')
image mc 3b t = make_comp('mc', 641, 386, '03t', '0b')
image mc 3b = make_cs('mc', '3b', True)
image mc 4b s = make_comp('mc', 641, 386, '04', '0b')
image mc 4b = make_cs('mc', '4b')
image mc 5b s = make_comp('mc', 641, 386, '05', '0b')
image mc 5b t = make_comp('mc', 641, 386, '05t', '0b')
image mc 5b = make_cs('mc', '5b', True)
image mc 6b s = make_comp('mc', 641, 386, '06', '0b')
image mc 6b t = make_comp('mc', 641, 386, '06t', '0b')
image mc 6b = make_cs('mc', '6b', True)


image mother 1a s = make_comp('mother', 467, 239, '1_1', '1_a')
image mother 1a t = make_comp('mother', 467, 239, '1_1t', '1_a')
image mother 1a = make_cs('mother', '1a', True)
image mother 2a s = make_comp('mother', 467, 239, '1_2', '1_a')
image mother 2a = make_cs('mother', '2a')
image mother 3a s = make_comp('mother', 467, 239, '1_3', '1_a')
image mother 3a = make_cs('mother', '3a')
image mother 4a s = make_comp('mother', 467, 239, '1_4', '1_a')
image mother 4a = make_cs('mother', '4a')
image mother 5a s = make_comp('mother', 467, 239, '1_5', '1_a')
image mother 5a = make_cs('mother', '5a')
image mother 6a s = make_comp('mother', 467, 239, '1_6', '1_a')
image mother 6a t = make_comp('mother', 467, 239, '1_6t', '1_a')
image mother 6a = make_cs('mother', '6a', True)
image mother 7a s = make_comp('mother', 467, 239, '1_7', '1_a')
image mother 7a = make_cs('mother', '7a')


image npc1 s = 'spr_npc/n1.png'
image npc1 = make_cs('npc1', '')
image npc2 s = 'spr_npc/n2.png'
image npc2 = make_cs('npc2', '')

# --- CHARACTER STUFF ---
# technically these aren't visuals...
# but let's keep this a little secret between you and me, okay?

define narrator = Character(callback=functools.partial(set_cur_speaker, ch=None))
define s = Character('MC', image='mc', callback=functools.partial(set_cur_speaker, ch='mc'))
define m = Character('Mother', image='mother', callback=functools.partial(set_cur_speaker, ch='mother'))

define n1 = Character('NPC 1', image='npc1', callback=functools.partial(set_cur_speaker, ch='npc1'))
define n2 = Character('NPC 1', image='npc2', callback=functools.partial(set_cur_speaker, ch='npc2'))

# --- POSITION STUFF ---

transform l1_5:
    xalign 0.2
transform l1_4:
    xalign 0.25
transform l1_3:
    xalign 0.33

transform r1_5:
    xalign 0.8
transform r1_4:
    xalign 0.75
transform r1_3:
    xalign 0.67
