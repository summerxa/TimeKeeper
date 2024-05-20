# --- SPECIAL EFFECTS ---

# Snow particles base code credit to Renpy wiki
# Tweaked it a little to have a max/min depth (lower = closer to the viewer, higher = farther)
init python:
    import random
    
    random.seed()

    def Snow(image, max_particles=50, speed=150, wind=100, xborder=(0,100), yborder=(50,400), **kwargs):
        """
        This creates the snow effect. You should use this function instead of instancing
        the SnowFactory directly (we'll, doesn't matter actually, but it saves typing if you're
        using the default values =D)
        
        @parm {image} image:
            The image used as the snowflakes. This should always be a image file or an im object,
            since we'll apply im transformations in it.
        
        @parm {int} max_particles:
            The maximum number of particles at once in the screen.
            
        @parm {float} speed:
            The base vertical speed of the particles. The higher the value, the faster particles will fall.
            Values below 1 will be changed to 1
            
        @parm {float} wind:
            The max wind force that'll be applyed to the particles.
            
        @parm {Tuple ({int} min, {int} max)} xborder:
            The horizontal border range. A random value between those two will be applyed when creating particles.
            
        @parm {Tuple ({int} min, {int} max)} yborder:
            The vertical border range. A random value between those two will be applyed when creating particles.
            The higher the values, the fartest from the screen they will be created.
        """
        return Particles(SnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))
    
    class SnowFactory(object):
        """
        The factory that creates the particles we use in the snow effect.
        """
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):
            """
            Initialize the factory. Parameters are the same as the Snow function.
            """            
            # the maximum number of particles we can have on screen at once
            self.max_particles = max_particles
            
            # the particle's speed
            self.speed = speed
            
            # the wind's speed
            self.wind = wind
            
            # the horizontal/vertical range to create particles
            self.xborder = xborder
            self.yborder = yborder
            
            # the maximum depth of the screen. Higher values lead to more varying particles size,
            # but it also uses more memory. Default value is 10 and it should be okay for most
            # games, since particles sizes are calculated as percentage of this value.
            self.depthmin = kwargs.get("depthmin", 1)

            self.depthmax = kwargs.get("depthmax", 10)
            
            # initialize the images
            self.image = self.image_init(image)
            

        def create(self, particles, st):
            """
            This is internally called every frame by the Particles object to create new particles.
            We'll just create new particles if the number of particles on the screen is
            lower than the max number of particles we can have.
            """
            # if we can create a new particle...
            if particles is None or len(particles) < self.max_particles:
                
                # generate a random depth for the particle
                depth = random.randint(self.depthmin, self.depthmax)
                
                # We expect that particles falling far from the screen will move slowly than those
                # that are falling near the screen. So we change the speed of particles based on
                # its depth =D
                depth_speed = 1.5-depth/(self.depthmax+0.0)
                
                return [ SnowParticle(self.image[depth-self.depthmin-1],      # the image used by the particle 
                                    random.uniform(-self.wind, self.wind)*depth_speed,  # wind's force
                                    self.speed*depth_speed,  # the vertical speed of the particle
                                    random.randint(self.xborder[0], self.xborder[1]), # horizontal border
                                    random.randint(self.yborder[0], self.yborder[1]), # vertical border
                                    ) ]
        
        
        def image_init(self, image):
            """
            This is called internally to initialize the images.
            will create a list of images with different sizes, so we
            can predict them all and use the cached versions to make it more memory efficient.            
            """
            rv = [ ]
            
            # generate the array of images for each possible depth value.
            for depth in range(self.depthmax - self.depthmin + 1):
                # Resize and adjust the alpha value based on the depth of the image
                p = 1.1 - depth/(self.depthmax+0.0)
                if p > 1:
                    p = 1.0
                
                rv.append( At( At(image, opac(p)), zm(p) ) )

            return rv
        
        
        def predict(self):
            """
            This is called internally by the Particles object to predict the images the particles
            are using. It's expected to return a list of images to predict.
            """ 
            return self.image

    class SnowParticle(object):
        """
        Represents every particle in the screen.
        """
        def __init__(self, image, wind, speed, xborder, yborder):
            """
            Initializes the snow particle. This is called automatically when the object is created.
            """
            
            # The image used by this particle
            self.image = image
            
            # For safety (and since we don't have snow going from the floor to the sky o.o)
            # if the vertical speed of the particle is lower than 1, we use 1.
            # This prevents the particles of being stuck in the screen forever and not falling at all.
            if speed <= 0:
                speed = 1
                
            # wind's speed
            self.wind = wind
            
            # particle's speed
            self.speed = speed

            # The last time when this particle was updated (used to calculate the unexpected delay
            # between updates, aka lag)
            self.oldst = None
            
            # the horizontal/vertical positions of this particle            
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder
            
            
        def update(self, st):
            """
            Called internally in every frame to update the particle.
            """
            
            # calculate lag
            if self.oldst is None:
                self.oldst = st
            
            lag = st - self.oldst
            self.oldst = st
            
            # update the position
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
               
            # verify if the particle went out of the screen so we can destroy it.
            if self.ypos > renpy.config.screen_height or\
                (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                ##  print "Dead"
                return None
                
            # returns the particle as a Tuple (xpos, ypos, time, image)
            # since it expects horizontal and vertical positions to be integers, we have to convert
            # it (internal positions use float for smooth movements =D)
            return int(self.xpos), int(self.ypos), st, self.image

transform zm(a):
    zoom a

transform opac(a):
    matrixcolor OpacityMatrix(a)


image snowfront = Snow('particles/particle_snow_1.png', max_particles=25, depthmax=3)
image snowback = Snow('particles/particle_snow_1.png', max_particles=25, depthin=9)

image snowmenu = Snow(At('particles/particle_gold.png', opac(0.25)))


default cfade = Fade(0.5, 0.0, 0.5)
# ^ 0.5 for normal fade, 0.0 to skip fade animation

# --- SOUND STUFF ---

init:
    $ renpy.music.register_channel("ambience", "ambience", loop=True)

# story sfx
define audio.glass_break_sfx = "<from 31.4 to 32.8>a lot of glass breaking.mp3"
define audio.metal_pipe = "jixaw-metal-pipe-falling-sound.mp3"
define audio.clothes_rustle = "<from 0.5 to 3>fabric-rustling-and-sliding-25971.mp3"
define audio.chain_clink = "<from 0 to 1>Small Size Chain Sound Effect.mp3"
define audio.door_creak = "door-creak-02-79920.mp3"

# minigame sfx
define audio.button_click_sfx = "btn_click_light_2.mp3"
define audio.waterpour_click_sfx = "btn_click_waterpour.mp3"

# AMBIENCE
define audio.ballroom_ambience_1 = "<from 3.1 to 6.44>bustling-cafe-ambience.mp3"
define audio.ballroom_ambience_2 = "<from 3.5 to 7.0>busy-restaurant-dining-room-ambience-128466.mp3"
define audio.wind_howling_ambience = "<from .551 to 27.2>wind-blowing-sfx-12809.mp3"


# --- UI STUFF ---

# keep an image rotated to angle "a"
transform rot(a):
    rotate a

style fancy_font:
    color '#906548'
    font 'Maitree-Regular.ttf'
    textalign 0.5

style plaque1_font:
    color '#000000'
    font 'Maitree-Regular.ttf'
    textalign 0.5

transform highlight_hov(hov, myname, col='#aaaaaa'):
    matrixcolor InvertMatrix(1.0 if (hov == myname) else 0.0) * TintMatrix(col if (hov == myname) else '#ffffff') * InvertMatrix(1.0 if (hov == myname) else 0.0)

transform zoom_hov(hov, myname, sz=1.05):
    zoom (sz if hov == myname else 1.0)

transform tint(c):
    matrixcolor TintMatrix(c)

# used for endings menu zoom in/out
init python:
    def zoomfact_torange(zf_):
        lbound = 0.52
        return lbound + (1.0 - lbound) * zf_

    def zf(n_, zf_):
        return int(n_*zf_)

    def get_nodech_anchor(nsize):
        return ((310/2)/nsize[0], (1.0 - ((165/2)/nsize[1])))

# --- SPRITE STUFF ---

# used to shade sprites that aren't talking
transform darken_sprite:
    tint('#aaa')

init python:
    import functools
    def set_cur_speaker(event, interact=True, ch=None, **kwargs):
        global current_speaker
        global focus_dict

        if not interact:
            return

        if event == 'begin':
            current_speaker = ch
            # remove highlighted characters after one line of dialogue is shown
            chk = list(focus_dict.keys())
            for ch in chk:
                if not focus_dict[ch]:
                    del focus_dict[ch]
            for ch in focus_dict:
                focus_dict[ch] -= 1
    
    def focus_on(chs, cht={}):
        store.current_speaker = None
        for ch in chs:
            focus_dict[ch] = cht[ch] if ch in cht else 1
    
    def Comp_(charname, imwidth, headheight, face, pose):
        im_face = f"sprites/{charname}/{face}.png"
        im_pose = f"sprites/{charname}/{pose}.png"
        return Composite((imwidth, 1080), (0, 0), im_face, (0, headheight), im_pose)

    def CS_(charname, spr_im):
        return ConditionSwitch(
            f"current_speaker == '{charname}' or '{charname}' in focus_dict", spr_im,
            "True", At(spr_im, darken_sprite)
        )
    
    def CCS_(charname, imwidth, headheight, face, pose):
        return CS_(charname, Comp_(charname, imwidth, headheight, face, pose))


image bg mgame_main = 'mini/ui_backrgons.jpg'
image bg mgame_waterpour = 'mini/tgame/waterpour/waterpour_bg.jpg'
image bg mgame_dropdishes = 'mini/tgame/grab_dropdishes/dropdishes_bg.jpg'

image bg guestroom = 'bgs/guestroom.jpg'
image bg hallway = 'bgs/hallway.jpg'
image bg kitchen = 'bgs/kitchen.jpg'

image bg seal room = 'bgs/seal room.png'
image bg joyce why = 'bgs/joyce why.png'
image bg hellway = 'bgs/hellway.png'

image cg amelia tired v1 = 'cgs/Amelia_Cutscene look away.jpg'
image cg amelia tired v2 = 'cgs/Amelia_Cutscene look at you.jpg' 


image mc minigame = Comp_('mc', 641, 386, '01', '0b')

image mc default = Comp_('mc', 641, 386, '01', '0a')
image mc 1a = CCS_('mc', 641, 386, '01', '0a')
image mc 2a = CCS_('mc', 641, 386, '02', '0a')
image mc 3a = CCS_('mc', 641, 386, '03', '0a')
image mc 4a = CCS_('mc', 641, 386, '04', '0a')
image mc 5a = CCS_('mc', 641, 386, '05', '0a')
image mc 6a = CCS_('mc', 641, 386, '06', '0a')

image mc 1b = CCS_('mc', 641, 386, '01', '0b')
image mc 2b = CCS_('mc', 641, 386, '02', '0b')
image mc 3b = CCS_('mc', 641, 386, '03', '0b')
image mc 4b = CCS_('mc', 641, 386, '04', '0b')
image mc 5b = CCS_('mc', 641, 386, '05', '0b')
image mc 6b = CCS_('mc', 641, 386, '06', '0b')


image mother default = Comp_('mother', 467, 281, '1_1', '1_a')
image mother 1a = CCS_('mother', 467, 281, '1_1', '1_a')
image mother 2a = CCS_('mother', 467, 281, '1_2', '1_a')
image mother 3a = CCS_('mother', 467, 281, '1_3', '1_a')
image mother 4a = CCS_('mother', 467, 281, '1_4', '1_a')
image mother 5a = CCS_('mother', 467, 281, '1_5', '1_a')
image mother 6a = CCS_('mother', 467, 281, '1_6', '1_a')
image mother 7a = CCS_('mother', 467, 281, '1_7', '1_a')
image mother 8a = CCS_('mother', 467, 281, '1_8', '1_a')


image amelia default = Comp_('amelia', 450, 412, '2_1', '2_a')
image amelia 1a = CCS_('amelia', 450, 412, '2_1', '2_a')
image amelia 2a = CCS_('amelia', 450, 412, '2_2', '2_a')
image amelia 3a = CCS_('amelia', 450, 412, '2_3', '2_a')
image amelia 4a = CCS_('amelia', 450, 412, '2_4', '2_a')
image amelia 5a = CCS_('amelia', 450, 412, '2_5', '2_a')
image amelia 6a = CCS_('amelia', 450, 412, '2_6', '2_a')
image amelia 7a = CCS_('amelia', 450, 412, '2_7', '2_a')
image amelia 8a = CCS_('amelia', 450, 412, '2_8', '2_a')


image bella default = Comp_('bella', 536, 318, '3_1', '3_a')
image bella 1a = CCS_('bella', 536, 318, '3_1', '3_a')
image bella 2a = CCS_('bella', 536, 318, '3_2', '3_a')
image bella 3a = CCS_('bella', 536, 318, '3_3', '3_a')
image bella 4a = CCS_('bella', 536, 318, '3_4', '3_a')
image bella 5a = CCS_('bella', 536, 318, '3_5', '3_a')
image bella 6a = CCS_('bella', 536, 318, '3_6', '3_a')
image bella 7a = CCS_('bella', 536, 318, '3_7', '3_a')
image bella 8a = CCS_('bella', 536, 318, '3_8', '3_a')
image bella 9a = CCS_('bella', 536, 318, '3_9', '3_a')
image bella 10a = CCS_('bella', 536, 318, '3_10', '3_a')


image npc1 = CS_('npc1', 'sprites/npc/n1.png')
image npc2 = CS_('npc2', 'sprites/npc/n2.png')
image npc3 = CS_('npc3', 'sprites/npc/n3.png')
image npc3_1 = CS_('npc3_1','sprites/npc/n3_1.png')
image npc4 = CS_('npc4', 'sprites/npc/n4.png')
image npc5 = CS_('npc5', 'sprites/npc/n5.png')

# --- CHARACTER STUFF ---
# technically these aren't visuals...
# but let's keep this a little secret between you and me, okay?
# ok, lol

define narrator = Character(callback=functools.partial(set_cur_speaker, ch=None))
define s = Character('ANASTASIA', image='mc', callback=functools.partial(set_cur_speaker, ch='mc'))
define m = Character('mother_name', image='mother', callback=functools.partial(set_cur_speaker, ch='mother'), dynamic=True)
define a = Character('amelia_name', image='amelia', callback=functools.partial(set_cur_speaker, ch='amelia'), dynamic=True)
define b = Character('bella_name', image='bella', callback=functools.partial(set_cur_speaker, ch='bella'), dynamic=True)

default mother_name = '???'
default amelia_name = '???'
default bella_name = '???'

# young noble m
define n1 = Character('npc1_name', image='npc1', callback=functools.partial(set_cur_speaker, ch='npc1'), dynamic=True)
# old noble m
define n2 = Character('npc2_name', image='npc2', callback=functools.partial(set_cur_speaker, ch='npc2'), dynamic=True)
# maid
define n3 = Character('npc3_name', image='npc3', callback=functools.partial(set_cur_speaker, ch='npc3'), dynamic=True)
# alt maid
define n3_1 = Character('npc3_1_name', image='npc3_1', callback=functools.partial(set_cur_speaker, ch='npc3_1'), dynamic=True)
# young noble f
define n4 = Character('npc4_name', image='npc4', callback=functools.partial(set_cur_speaker, ch='npc4'), dynamic=True)
# old noble f
define n5 = Character('npc5_name', image='npc5', callback=functools.partial(set_cur_speaker, ch='npc5'), dynamic=True)

default npc1_name = 'NOBLE'
default npc2_name = 'NOBLE'
default npc3_name = 'MAID'
default npc3_1_name = 'MAID'
default npc4_name = 'NOBLE'
default npc5_name = 'NOBLE'

# --- POSITION STUFF ---

transform flip:
    xzoom -1
transform unflip:
    xzoom 1

transform xal(x):
    xalign x

transform lin(t, x):
    linear t xalign x
transform ea(t, x):
    ease t xalign x
transform ein(t, x):
    easein t xalign x
transform eout(t, x):
    easeout t xalign x

transform linf(x0, t, x):
    xalign x0
    linear t xalign x
transform eaf(x0, t, x):
    xalign x0
    ease t xalign x
transform einf(x0, t, x):
    xalign x0
    easein t xalign x
transform eoutf(x0, t, x):
    xalign x0
    easeout t xalign x

transform l1_5:
    xal(0.2)
transform l1_4:
    xal(0.25)
transform l1_3:
    xal(0.333)
transform l2_5:
    xal(0.4)
transform r2_5:
    xal(0.6)
transform r1_3:
    xal(0.667)
transform r1_4:
    xal(0.75)
transform r1_5:
    xal(0.8)

transform vshake:
    linear 0.01 yoffset -20
    linear 0.01 yoffset 0
    repeat 10

transform mc_gets_bonked:
    easein 0.1 xoffset 20
    linear 0.1 xoffset 0

# animation test >:3
transform boogie:
    flip
    pause 0.1
    unflip
    pause 0.1
    repeat
