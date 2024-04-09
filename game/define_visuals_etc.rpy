init python:
    
    #################################################################
    # Here we use random module for some random stuffs (since we don't
    # want Ren'Py saving the random number's we'll generate.
    import random
    
    # initialize random numbers
    random.seed()
    
    #################################################################
    # Snow particles
    # ----------------
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
    
    # ---------------------------------------------------------------
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
            self.depth = kwargs.get("depth", 10)
            
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
                depth = random.randint(1, self.depth)
                
                # We expect that particles falling far from the screen will move slowly than those
                # that are falling near the screen. So we change the speed of particles based on
                # its depth =D
                depth_speed = 1.5-depth/(self.depth+0.0)
                
                return [ SnowParticle(self.image[depth-1],      # the image used by the particle 
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
            for depth in range(self.depth):
                # Resize and adjust the alpha value based on the depth of the image
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0
                
                rv.append( At( At(image, opac(p)), siz(p) ) )

            return rv
        
        
        def predict(self):
            """
            This is called internally by the Particles object to predict the images the particles
            are using. It's expected to return a list of images to predict.
            """ 
            return self.image
            
    # ---------------------------------------------------------------
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

transform siz(a):
    zoom a

transform opac(a):
    matrixcolor OpacityMatrix(a)


image snow1 = Snow('particles/particle_snow_1.png')
image snow2 = Snow('particles/particle_snow_2.png')

image snowmenu base = Snow('particles/particle_gold.png')
image snowmenu opac = Snow(At('particles/particle_gold.png', opac(0.5)))
image snowmenu tinted = Snow(At('particles/particle_gold.png', darken_sprite))

default cfade = Fade(fadetime, 0.0, fadetime)

# --- UI STUFF ---

# keep an image rotated to angle "a"
transform rot(a):
    rotate a

style fancy_font:
    color '#906548'
    font 'Bodoni-16-Bold.otf'
    textalign 0.5

transform highlight_hov(hov, myname):
    # matrixcolor BrightnessMatrix(0.2 if (hov == myname) else 0.0) * ContrastMatrix(1.0 if (hov == myname) else 1.0)
    matrixcolor InvertMatrix(1.0 if (hov == myname) else 0.0) * TintMatrix('#aaaaaa' if (hov == myname) else '#ffffff') * InvertMatrix(1.0 if (hov == myname) else 0.0)

transform tint(c):
    matrixcolor TintMatrix(c)

# --- SPRITE STUFF ---

# used to shade sprites that aren't talking
transform darken_sprite:
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

    def CS_(charname, spr_im):
        return ConditionSwitch(
            f"current_speaker == '{charname}' or talks_next == '{charname}'", spr_im,
            "True", At(spr_im, darken_sprite)
        )
    
    def Comp_CS_(charname, imwidth, headheight, face, pose):
        return CS_(charname, Comp_(charname, imwidth, headheight, face, pose))


image bg minigame = 'mini/ui_backrgons.jpg'

image bg guestroom 1 = 'bgs/guestroom 1.jpg'
image bg guestroom 2 = 'bgs/guestroom 2.jpg'

image bg seal room = 'bgs/seal room.png'
image bg hallway = 'bgs/hallway.png'
image bg joyce why = 'bgs/joyce why.png'


image mc minigame = Comp_('mc', 641, 386, '01', '0a')

image mc 1a = Comp_CS_('mc', 641, 386, '01', '0a')
image mc 2a = Comp_CS_('mc', 641, 386, '02', '0a')
image mc 3a = Comp_CS_('mc', 641, 386, '03', '0a')
image mc 4a = Comp_CS_('mc', 641, 386, '04', '0a')
image mc 5a = Comp_CS_('mc', 641, 386, '05', '0a')
image mc 6a = Comp_CS_('mc', 641, 386, '06', '0a')

image mc 1b = Comp_CS_('mc', 641, 386, '01', '0b')
image mc 2b = Comp_CS_('mc', 641, 386, '02', '0b')
image mc 3b = Comp_CS_('mc', 641, 386, '03', '0b')
image mc 4b = Comp_CS_('mc', 641, 386, '04', '0b')
image mc 5b = Comp_CS_('mc', 641, 386, '05', '0b')
image mc 6b = Comp_CS_('mc', 641, 386, '06', '0b')


image mother 1a = Comp_CS_('mother', 467, 281, '1_1', '1_a')
image mother 2a = Comp_CS_('mother', 467, 281, '1_2', '1_a')
image mother 3a = Comp_CS_('mother', 467, 281, '1_3', '1_a')
image mother 4a = Comp_CS_('mother', 467, 281, '1_4', '1_a')
image mother 5a = Comp_CS_('mother', 467, 281, '1_5', '1_a')
image mother 6a = Comp_CS_('mother', 467, 281, '1_6', '1_a')
image mother 7a = Comp_CS_('mother', 467, 281, '1_7', '1_a')
image mother 8a = Comp_CS_('mother', 467, 281, '1_8', '1_a')


image amelia 1a = Comp_CS_('amelia', 450, 412, '2_1', '2_a')
image amelia 2a = Comp_CS_('amelia', 450, 412, '2_2', '2_a')
image amelia 3a = Comp_CS_('amelia', 450, 412, '2_3', '2_a')
image amelia 4a = Comp_CS_('amelia', 450, 412, '2_4', '2_a')
image amelia 5a = Comp_CS_('amelia', 450, 412, '2_5', '2_a')
image amelia 6a = Comp_CS_('amelia', 450, 412, '2_6', '2_a')
image amelia 7a = Comp_CS_('amelia', 450, 412, '2_7', '2_a')
image amelia 8a = Comp_CS_('amelia', 450, 412, '2_8', '2_a')


image bella 1a = Comp_CS_('bella', 536, 318, '3_1', '3_a')
image bella 2a = Comp_CS_('bella', 536, 318, '3_2', '3_a')
image bella 3a = Comp_CS_('bella', 536, 318, '3_3', '3_a')
image bella 4a = Comp_CS_('bella', 536, 318, '3_4', '3_a')
image bella 5a = Comp_CS_('bella', 536, 318, '3_5', '3_a')
image bella 6a = Comp_CS_('bella', 536, 318, '3_6', '3_a')
image bella 7a = Comp_CS_('bella', 536, 318, '3_7', '3_a')
image bella 8a = Comp_CS_('bella', 536, 318, '3_8', '3_a')


image npc1 = CS_('npc1', 'sprites/npc/n1.png')
image npc2 = CS_('npc2', 'sprites/npc/n2.png')
image npc3 = CS_('npc3', 'sprites/npc/n3.png')
image npc4 = CS_('npc4', 'sprites/npc/n4.png')
image npc5 = CS_('npc5', 'sprites/npc/n5.png')

# --- CHARACTER STUFF ---
# technically these aren't visuals...
# but let's keep this a little secret between you and me, okay?

define narrator = Character(callback=functools.partial(set_cur_speaker))
define s = Character('MC', image='mc', callback=functools.partial(set_cur_speaker, ch='mc'))
default mother_name = '???'
define m = Character('mother_name', image='mother', callback=functools.partial(set_cur_speaker, ch='mother'), dynamic=True)
default amelia_name = '???'
define a = Character('amelia_name', image='amelia', callback=functools.partial(set_cur_speaker, ch='amelia'), dynamic=True)
default bella_name = '???'
define b = Character('bella_name', image='bella', callback=functools.partial(set_cur_speaker, ch='bella'), dynamic=True)
default maria_name = '???'
define l = Character('maria_name', image='maria', callback=functools.partial(set_cur_speaker, ch='maria'), dynamic=True)

# young noble m
define n1 = Character('NOBLE', image='npc1', callback=functools.partial(set_cur_speaker, ch='npc1'))
# old noble m
define n2 = Character('NOBLE', image='npc2', callback=functools.partial(set_cur_speaker, ch='npc2'))
# maid
define n3 = Character('MAID', image='npc3', callback=functools.partial(set_cur_speaker, ch='npc3'))
# young noble f
define n4 = Character('NOBLE', image='npc4', callback=functools.partial(set_cur_speaker, ch='npc4'))
# old noble f
define n5 = Character('NOBLE', image='npc5', callback=functools.partial(set_cur_speaker, ch='npc5'))

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
