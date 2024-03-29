define cfade = Fade(fadetime, 0.0, fadetime)

# --- UI STUFF ---

# keep an image rotated to angle "a"
transform rot(a):
    rotate a

style fancy_font:
    color '#906548'
    font 'Bodoni-16-Medium.otf'

# transform highlight_hov(hov, myname):
#     matrixcolor BrightnessMatrix(0.1 if (hov == myname) else 0.0)

# transform highlight_hov:
#     matrixcolor BrightnessMatrix(0.0)

# --- SPRITE STUFF ---

# used to shade sprites that aren't talking
transform darken_sprite:
    # matrixcolor ContrastMatrix(0.9) * BrightnessMatrix(-0.2)
    matrixcolor TintMatrix('#aaaaaa')

init python:
    import functools
    def set_cur_speaker(event, interact=True, ch=None, **kwargs):
        global current_speaker
        global talks_next

        if not interact:
            return

        if event == 'show':
            current_speaker = ch
            talks_next = None
    
    def Comp_(charname, imwidth, headheight, face, pose):
        im_face = f"sprites/{charname}/{face}.png"
        im_pose = f"sprites/{charname}/{pose}.png"
        return Composite((imwidth, 1080), (0, 0), im_face, (0, headheight), im_pose)

    def CS_(charname, imname, has_talk=False):
        silent = f"{charname} {imname} s"
        talking = f"{charname} {imname} {'t' if has_talk else 's'}"
        return ConditionSwitch(
            f"current_speaker == '{charname}'", talking,
            f"talks_next == '{charname}'", silent,
            "True", At(silent, darken_sprite)
        )

image bg minigame = 'mini/ui_backrgons.jpg'
image bg seal room = 'bgs/seal room.png'
image bg hallway = 'bgs/hallway.png'
image bg joyce why = 'bgs/joyce why.png'


image mc 1a s = Comp_('mc', 641, 386, '01', '0a')
image mc 1a t = Comp_('mc', 641, 386, '01t', '0a')
image mc 1a = CS_('mc', '1a', True)
image mc 2a s = Comp_('mc', 641, 386, '02', '0a')
image mc 2a = CS_('mc', '2a')
image mc 3a s = Comp_('mc', 641, 386, '03', '0a')
image mc 3a t = Comp_('mc', 641, 386, '03t', '0a')
image mc 3a = CS_('mc', '3a', True)
image mc 4a s = Comp_('mc', 641, 386, '04', '0a')
image mc 4a = CS_('mc', '4a')
image mc 5a s = Comp_('mc', 641, 386, '05', '0a')
image mc 5a t = Comp_('mc', 641, 386, '05t', '0a')
image mc 5a = CS_('mc', '5a', True)
image mc 6a s = Comp_('mc', 641, 386, '06', '0a')
image mc 6a t = Comp_('mc', 641, 386, '06t', '0a')
image mc 6a = CS_('mc', '6a', True)

image mc 1b s = Comp_('mc', 641, 386, '01', '0b')
image mc 1b t = Comp_('mc', 641, 386, '01t', '0b')
image mc 1b = CS_('mc', '1b', True)
image mc 2b s = Comp_('mc', 641, 386, '02', '0b')
image mc 2b = CS_('mc', '2b')
image mc 3b s = Comp_('mc', 641, 386, '03', '0b')
image mc 3b t = Comp_('mc', 641, 386, '03t', '0b')
image mc 3b = CS_('mc', '3b', True)
image mc 4b s = Comp_('mc', 641, 386, '04', '0b')
image mc 4b = CS_('mc', '4b')
image mc 5b s = Comp_('mc', 641, 386, '05', '0b')
image mc 5b t = Comp_('mc', 641, 386, '05t', '0b')
image mc 5b = CS_('mc', '5b', True)
image mc 6b s = Comp_('mc', 641, 386, '06', '0b')
image mc 6b t = Comp_('mc', 641, 386, '06t', '0b')
image mc 6b = CS_('mc', '6b', True)


image mother 1a s = Comp_('mother', 467, 239, '1_1', '1_a')
image mother 1a t = Comp_('mother', 467, 239, '1_1t', '1_a')
image mother 1a = CS_('mother', '1a', True)
image mother 2a s = Comp_('mother', 467, 239, '1_2', '1_a')
image mother 2a = CS_('mother', '2a')
image mother 3a s = Comp_('mother', 467, 239, '1_3', '1_a')
image mother 3a = CS_('mother', '3a')
image mother 4a s = Comp_('mother', 467, 239, '1_4', '1_a')
image mother 4a = CS_('mother', '4a')
image mother 5a s = Comp_('mother', 467, 239, '1_5', '1_a')
image mother 5a = CS_('mother', '5a')
image mother 6a s = Comp_('mother', 467, 239, '1_6', '1_a')
image mother 6a t = Comp_('mother', 467, 239, '1_6t', '1_a')
image mother 6a = CS_('mother', '6a', True)
image mother 7a s = Comp_('mother', 467, 239, '1_7', '1_a')
image mother 7a = CS_('mother', '7a')


image npc1 s = 'sprites/npc/n1.png'
image npc1 = CS_('npc1', '')
image npc2 s = 'sprites/npc/n2.png'
image npc2 = CS_('npc2', '')

# --- CHARACTER STUFF ---
# technically these aren't visuals...
# but let's keep this a little secret between you and me, okay?

define narrator = Character(callback=functools.partial(set_cur_speaker))
define s = Character('MC', image='mc', callback=functools.partial(set_cur_speaker, ch='mc'))
define m = Character('Mother', image='mother', callback=functools.partial(set_cur_speaker, ch='mother'))

# young noble m npc
define n1 = Character('NPC 1', image='npc1', callback=functools.partial(set_cur_speaker, ch='npc1'))
# old noble m npc
define n2 = Character('NPC 2', image='npc2', callback=functools.partial(set_cur_speaker, ch='npc2'))

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
