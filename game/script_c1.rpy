 
label c1_scene1:
    
    "Scene 1 (Memory)"
    
    $ mother_name = "???"

    m "You will be perfect, won’t you?"
    
    $ focus_on('[mc]') 
    show mc 3b with Dissolve(.5,alpha=True) 
    #i think normal dissolve is ..5 automatically?
    
    s "Yes."

    m "My perfect little doll."

    s 1b "Yes, Mother."
    
    $ char_unlock("mc") 
    $ char_unlock("mother")

    $ node_unlock('c1_scene1')

    return

#animations:
    #align, xalign, and yalign set position and anchor (relative to top left) to this value, so xalign 0.0 and yalign 0.0 set current postion and anchor as 0.0,0.0
    #linear, ease, easein, easeout all move the sprites: first # affects time (larger # = slower), second # affects position
        #linear moves sprite at level speed all thorughout
        #ease starts slow, speeds up, then ends slow
        #easein starts fast, ends slow
        #easeout starts slow, ends fast
        #linear 1.0 xalign 1.0
    #use lin(), ein(), eout() instead!
    #and linf(), einf(), eoutf() to set position first in not already on screen
    #pause (for x time), rotate (for x degrees), and repeat are self-explanatory
    #zoom, xzoom, yzoom all zoom in; xzoom and yzoom only affect horizontal/vertical
        #negative values will flip the sprite horizontally/vertically
        #set zoom to 1.0 to reset
    #linear + circles
    #zorder (number) makes image above others with smaller number
    #use behind to... make iamges behind each other
    #idk if it's better to increase/decrease zorder for diff images, or set zorder to value, set back to 0, then use behind #shrug
        #prolly easiest is to just keep increasing zorder
    # use $ focus_on(['xyz']) to focus on someone
    #scene black with dissolve
    #to center 2 chars, use l1_5 and r1_5, or xal .2 and .8
    #use -.8 to out offscreen left, 1.5 for offscreem right
    #to display snow: show black with dissolve, scene bg xyz, show snowback, show black, pause x time, hide black with dissolve, show sprite, show snowfront

label c1_scene1_5: 
   
    scene bg joyce why with cfade
    "test scene"
    #testing out animations bc AHHHH
    
    show mc 2b
    s "what sprite is this?"
    s 1a "ohhh"

    "let's see how these positions look"

    show mc 3b at flip
    s 4a "hmmm"

    show mc 5a at l1_5
    show mc 6a at r1_5

    s 2a "well..."
    show mc 5a:

        xalign 0.0 yalign 0.0

        linear 2.0 xalign 1.0

    s "it looks ok ig"

    show bella 1a at offscreenleft
    b "what are you doing?"

    s "testing, {i}duh{i}"

    show amelia 3a at left
    a "it's... pretty obvious, bella"

    show mc 2b:

        xalign 0.0 yalign 0.0

        linear 1.0 xalign 0.5

    s "Yeah, listen to your gf, {i}bella{i}"

    show bella 6a:

        xalign 0.0 yalign 0.0

        linear 0.5 xalign 0.3

    b "she's not my gf!!"
    b 8a "y-yet..."

    show amelia 1a at left
    a "i'm... not??"

    show bella 6a:

        xalign 0.0 yalign 0.0

        linear 2.0 xalign 1.0
        xzoom -1.0
        easein 2.0 xalign 0.0
        xzoom 1.0
        repeat

    b "u-um..."

    show amelia 3a at left
    a "it's ok, bella"
    a 4a "that just means that we havent become gfs yet!"

    show bella 7a at flip, l1_3
    b 'y-yeah...'

    show amelia 3a:
        xalign 0.0 yalign 0.1
        zoom 3.0

    s "yeet"

    show mc 6a:
        easein 3.0 xalign 0.5
        easeout 3.0 xalign 0.0
        pause 1.0
        repeat
    s "not really sure if easein/out makes a major difference"

    show amelia 1a:
        xzoom 2.0
    a "horizontal zoommm"

    show bella 3a:
        xalign 0.001
        yzoom 2.0
    b "vertical zoom"

    show amelia 1a:
        xalign 0.15 yalign 0.0
        zoom 1
        xzoom 1

    show mc 5a:
        anchor (0,0)
        linear 2.0 clockwise circles 3
        #for some reason, the anchor will depend on where mc is at before player clicks, so circles either will be big or small depending on how close mc is to top side

    s "weee"

    show mc 6a:
        xalign 1.0 yalign 0.0
        anchor (0.5,0)
        linear 4.5 clockwise circles 4

    s "getting kinda dizzy ngl"
    
    show mc 6a:
        xalign 1.0 yalign 0.0

    s "hmmm"

    show mc 5a:
        rotate 30
    
    s "im rotated"
    
    show mc 6a:
        rotate -30

    s "interesting"

    show mc 6a:
        rotate 0
    
    s "did anything happen?"

    show mc 5a:
        xpan 40

    s "did this work?"

    show mc 6a:
        xpan 0

    s "oh woe, a dismembered hand!"

    hide amelia 1a

    s "oh, there goes amelia lmao"
    
    show snowfront
    show snowback

    s "oh, snow!"

    show snowmenu

    s "oooh, {i}fancy{i} snow"
    #end of testing
    
    return
  
label c1_scene2:
    
    scene bg joyce why with cfade
    #TODO: replace with ballroom bg later
    
    play ambience ballroom_ambience_1
    #idk anymore... -jade

    "Scene 2 (Intro + tasks)"

    $ mother_name = "MOTHER"
    $ bella_name = "???"
    $ amelia_name = "???"

    show npc2 at center
    
    n2 "These are the most proficient of your maids, madam?"

    show mother 2a at l1_5
    #flip
        
    m "Yes, Lord Layton."
    
    $ focus_on(['mc', 'mother'])

    show mother 2a at ein(0.8, 0.15)
    #flip,

    show npc2 at ein(.8, .95) 
    #magic number .95

    show mc 1b at center
    #flip,

    m "This is Anastasia, my best maid. She’ll do anything you say and won’t tell a soul."

    
    n2 "I see."

    n2 "I suppose I might hire one of your maids in the near future."

    show mc 1b zorder 2.0
    m 3a "I am thoroughly pleased to hear that, sir. I ensure you that my maids are—"

    play sound glass_break_sfx volume 0.15
    #you can change whichever glass sound to be, just reference the video times from https://www.youtube.com/watch?v=0aaPMzWYL2A
    #MAKE SURE TO MAKE VOLUME VERY QUIET BECAUSE IT'S LOUD AS HELL

    show mother 5a
    
    show bella 8a at offscreenleft
    b "Ah!"
    
    show mother 6a at lin(0.8, 0.4)
    #unflip

    show mc 4b at lin(0.8, 0.7)
    #unflip

    show npc2 at lin(0.8, 1.1)

    pause 0.7
    show bella 8a at ein(0.7, 0.0)
    #flip

    pause 2.5
    m 7a "...Ah."

    show mother 8a #at flip
    m "My deepest apologies, Lord Layton. I’ll have this sorted out immediately."

    play sound metal_pipe volume .23
    hide npc2 with Dissolve(.4,alpha=True)
   
    
    show mother 6a #at unflip

    show bella 6a #at unflip
    b "Mother, I—"

    $ focus_on(['mother', 'bella'])

    show mother 7a at ein(0.6, 0.31)

    show bella 8a
    "Mother grips the maid’s shoulder with one hand and grips her chin with the other to force the maid to look at her."
    
    hide npc2 # hiding sprites saves a teeny bit of processing power #really? i didn't know that -jade
    # well, that's what renpy wiki told me lol -snail

    show amelia 6a at eaf(1.2, 0.8, 1.0)
    a "!!!"

    $ focus_on(['amelia'])

    "Another maid looks on in horror and covers her mouth with her hand."

    m "It seems I need to {i}reeducate{/i} you, Bella."

    $ bella_name = "BELLA"
   
    b 6a "No! I-"

    m 7a "Now, now. You wouldn’t want to cause a ruckus for the guests, {i}would you?{/i}"

    show mother 1a #at flip
    m "Could you clean this up, my dears?"

    $ focus_on(['mother', 'bella'])

    show mother 7a at ea(1.2, -1.0)
    #flip

    pause 0.5
    show bella 8a at ea(1.0, -1.0)
    #flip
    
    "Mother grips Bella’s arm tightly and drags her out of the ballroom."

    hide mother
    hide bella

    $ focus_on(['amelia'])

    #TODO: figure out what to do here LMAO; amelia's expression does NOT match 
    pause 1.0
    show amelia 1a
    "Anastasia and the other maids pull themselves together and clean up the mess."

    # turns out renpy has a built in black bg hooray -snail
    scene black with dissolve

    "One hour later…"

    scene bg joyce why with dissolve
    #TODO: replace with ballroom bg later

    $ focus_on(['mother', 'mc'])

    #TODO: animate them better
    show mc 3b at r1_4
    #flip

    show mother 1a at ein(1.0, 0.25)
    #flip

    pause .65
    show mc 1b #at unflip

    "Mother returns to the ballroom alone and walks to Anastasia."

    m "Anastasia, dear."

    m "There are some tasks that I would like you to complete tonight."

    m "Firstly, the candles and fireplaces in the guest rooms must be lit up, and make sure to tidy any cluttered rooms that you come across."

    m "On the off chance that a few of the nobles might wish to rest or converse in private, it is best that we prepare the rooms ahead of time."

    m "Then, you must go to the kitchens and bring the trays of food to the ballroom. Our guests will surely still be hungry, so that would hopefully keep them satisfied." 

    m "Lastly, empty trays must be taken to the kitchen and washed lest the ball room appears disorganized."

    m 5a "Please finish all these tasks by eight o’clock."

    s 3b "Yes, Mother."

    m 1a "If any of the guests require your service, you must assist them before completing your tasks."

    s "Yes, Mother."

    m 6a "And remember to report any disobedient maids."

    s 1b "I will."

    $ focus_on(['mother'])

    pause 1.0
    show mother 2a
    pause .5
    m "Don’t disappoint me, Anastasia."

    $ node_unlock('c1_scene2_tasks')

    scene hallway with cfade
    #TODO: replace with ballroom bg later

    $ focus_on(['bella'])

    show bella 8a at r1_4
    b "Ugh... Where is it? The cloth was here just a second ago!"

    show amelia 2a at einf(-0.2, 1.0 ,0.25)
    #flip
    a "Here, take this."

    $ focus_on(['bella'])

    show bella 1a #at flip

    $ amelia_name = "AMELIA"

    pause 0.5
    b "Oh. Thanks, Amelia…"

    a 3a "No problem, Bella."

    $ focus_on(['bella'])

    show bella 8a
    "Bella holds her hand to her face."

    b "Tch."

    a 6a "Are you okay, Bella?"

    $ focus_on(['bella'])

    show bella 5a
    pause .5
    show bella 8a
    pause 1.0
    b "I…"
    pause 1.0
    show bella 7a
    pause 1.0
    show bella 1a
    #you can adjust times and order if it feels weird bc i give up bro ;-;

    b "I just feel tired. That’s all. I’ll probably be fine after a while."

    a 1a "If you say so…" 

    $ focus_on(['amelia'], {'amelia': 2})

    show amelia 1a at eout(1.0, 0.2)
    #unflip
    "Amelia starts to walk away, but—"

    # i made an animation maybe...? -snail
    # TODO add a falling sound

    show amelia 8a
    # amelia falls immediately (more jarring/shocking effect)
    # if text plays too fast, waits until 0.5 secs have passed until making amelia fall
    $ wtime = 0.5 if (not preferences.text_cps or preferences.text_cps < 6) else 0.5 - (3 / preferences.text_cps)
    "!!!{w=[wtime]}{nw}"

    # falling animation
    hide amelia with easeoutbottom

    play sound metal_pipe volume .23
    #hehe :3

    # screen shake (might be a bit too intense?) -snail
    hide amelia with vpunch

    #not sure if this expression quite matches up... but oh well
    #might need a pause here bc otherwise might feel too fast
    # is this too long...? -snail
    #it should be fine :) -jade
    # hooray :D -snail
    pause 0.6
    b 9a "Amelia, are you alright?!"

    show amelia 1a at l1_5
    #flip
    a "I-I’m okay..."

    b 5a "Are you sure? Maybe you should take a break."

    a 5a "No— I’m okay! It’s probably nothing."

    b "I can finish your tasks if you need me to…"

    a 6a "N-no, I can do them!"

    a 1a "I-I mean, you were already punished...the cuts are still there. Should I get more medicine? I can always make some more if you need me to…"

    $ focus_on(['bella'])

    show bella 1a
    pause 0.5
    show bella 7a
    pause 0.5

    b "Nah, it's..."
    
    show bella 2a
    pause 1.5
    show bella 7a
    pause 0.5
    show bella 1a
    #again, you can adjust these times and the order stuff is in if it feels wack :P

    b "...It’s fine. Won’t open up unless I get punished again or something, though I’ll be doing everything I can to avoid that."

    b 5a "But Amelia, you've been worried about me... all this time."
    
    b "If you feel tired... {i}please{/i}, tell me."
    
    #this line... doesn't flow quite smoothly...
    # maybe remove the first "I know"- feels kinda redundant(?) idk how to word it... -snail
    # or break into two lines "...all this time" -> "But if you..." for a thoughtful pause effect :D

    a 5a "Don’t worry Bella, I’ll be alright."

    #WHY IS THERE NO CONCERNED/WORRIED EXPRESSION FOR BELLA AHHHH
    # maybe try 7a? it makes her look in amelia's general direction :D -snail
    #hopefully luna will provide us with a scared/worried expression soon T_T
    b 8a "If you say so..."

    $ char_unlock("amelia")
    $ char_unlock("bella")

    return

label c1_scene3:
    scene black with dissolve

    stop ambience

    "Scene 3 (amelia sick scene)"

    #shrug -jade
    "Anatasia walks to the guestrooms, lighting the candles one by one."

    scene cg amelia tired v1 with cfade
    "She eventually walks into Room 7, where Amelia is leaning against the wall. She seems to be in some discomfort." 

    # i think we're gonna transition into this cutscene from the tutorial minigame
    # so we may not need the intro section? -snail
    #ahh, true true -jade

    "Anatasia lights up the candles and the fireplace in the room before approaching the bed."

    s "What are you doing?"
    
    show cg amelia tired v2
    a "!!!"

    "Amelia steps towards Anatasia."

    a "Wait! I- D-Don’t tell Mother!"

    s "... "

    a "Please... "

    a "I- You… you know what she does to those who break the rules! P-please... I don’t want to be punished..."

    a "I’m not trying to slack off! I really am trying to live up to Mother’s expectations! I—"

    "Amelia pauses for a moment and breathes heavily; Her face briefly scrunching up in pain."

    a "It’s just that I keep getting these headaches and I can’t think straight."
    #bc she aint straight LMAO -jade
    # ayooooo -snail
    #( ͡° ͜ʖ ͡°) -jade

    a "B-but, I’ll be fine! J-just give me a few minutes and I’ll be doing perfect work."

    a "You would remember, right? I-I have never messed up before this! And it won’t ever happen again! I promise!"

    a "Please… don’t tell her."

    s "..."

    "Amelia struggles to stand up and return to work."

    scene black with dissolve
    #shrug -jade
    # i think this transition should be fine- check with luna tho lol -snail
    #ok -jade
    play sound clothes_rustle volume 2.0
    "Anatasia walks out of the room and finishes lighting the candles and fireplaces in all of the rooms."

    $ node_unlock('c1_scene3')

    return

label c1_fetch1:
    
    scene bg hallway with cfade
    #TODO: change this later maybe LMAO

    "Fetch quest 1"

    play ambience ballroom_ambience

    show npc2 at l1_5
    show mc 1b at r1_5

    n2 "Hey! You there. Bring me a bottle of red wine. The finest quality only!"

    # TODO mark 1st part as done
    
    "placeholder: fetch quest gameplay, in kitchen"

    jump c1_fetch1_end # TODO jump mini_main

label c1_fetch1_end:
    scene bg hallway with cfade
    #TODO: change this later maybe LMAO

    # TODO uncomment following line in actual minigame
    # play ambience ballroom_ambience

    show npc2 at l1_5
    show mc 1b at r1_5
    
    #after item is obtained, interacting with nobleman again triggers this

    # TODO call c1_give_item_prompt(n2, "wine_bottle")

    s 1b "Your wine, sir."

    n2 "Ah, perfect. Just the type I was looking for."

    # TODO mark 2nd part as done, remove wine from inventory
    
    $ node_unlock('c1_fetch1')

    return # TODO jump mini_main

label c1_fetch2:
    
    scene bg guestroom with cfade
    #TODO: replace bg with ballroom maybe
    
    "Fetch quest 2"

    show npc1 at l1_5
    show mc 1b at r1_5

    n1 "Are you the head maid?"

    s "Yes, I am."

    n1 "Excellent. I need you to go to the laundry room and bring my jacket to me." 

    n1 "It is the red one with the golden trim."

    s "Affirmative, sir."

    # TODO mark 1st part complete

    #[mc goes to the laundry room.] 

    #[mc sees a dark blue jacket, a black jacket, a red jacket, and a dark green jacket.]

    "fetch quest stuff"

    jump c1_fetch2_end # TODO jump mini_main

label c1_fetch2_end:
    scene bg guestroom with cfade
    #TODO: replace bg with ballroom maybe

    show npc1 at l1_5
    show mc 1b at r1_5

    # TODO call c1_give_item_prompt(n1, "jacket_red")
    
    $ focus_on(["mc"])
    "Anastasia returns to the ballroom with the jacket and hands it to the noble."

    n1 "Hmph. It appears that these maids are somewhat competent." 

    # TODO mark 2nd part complete, remove jacket from inventory

    scene bg hallway with cfade
    #TODO: replace bg w/ something else

    show bella 8a at center
    b "Shit… So goddamn tired, but I still need to help these stupid nobles. Damn it…"

    show bella 8a at ein(.6,.2)
    show mother 1a at offscreenright
    show mother at ein(.8,.8)
    m "Bella?"

    show bella 9a
    b "Y-yes, Mother?"

    $ focus_on(['mother'])
    show mother 5a
    pause .8
    show mother 6a
    m "I was hoping you were going to improve your performance today, especially after your little incident, but it seems that I expected too much from you."

    m 1a "Perhaps you should learn from Anastasia's example. After all, Anastasia has done an excellent job today."

    b 8a "..."

    m 6a "Make sure you finish the rest of your tasks." 

    b 5a "...Yes, Mother."
    #is this the right expression? -jade

    return # TODO jump mini_main

label c1_fetch3:
    
    scene bg hallway with cfade
    #TODO: change bg

    "Fetch quest 3"

    show npc2 at l1_5
    show npc3 at r1_5

    n3 "Sir, did you need something?"

    n2 "Are you the head maid? I only want service from the best around here."

    n3 "No, sir."

    n2 "Then what are you standing there for? Hurry up and find them!"

    show mc 1b at r1_5
    hide npc3
    with dissolve

    s "That would be me."

    n2 "Is that so? Go get me some desserts. Only the ones of finest quality."

    #TODO mark 1st part complete

    jump c1_fetch3_end # TODO jump mini_main

label c1_fetch3_end:

    scene bg kitchen with cfade
    #only for placeholder; not in actual game

    #TODO: replace ballroom ambience w/ kitchen sounds

    show mc 1b at center
    "fetch quest gameplay in kitchen; ask the chefs around the place to compile a list of the best desserts; After the tray is completed, scene triggers"

    show mc 1b at ea(.8,.2)
    show bella 4a at eaf(1.2,.8,.8)
    b "So, these are the desserts? I’ll be taking it."

    show bella 4a at eout(.8,1.4)
    s 4a "???"
    hide bella

    # TODO remove finished tray from inventory

    #when mc returns to ballroom, next scene triggers"

    scene bg hallway with cfade
    #TODO: replace with ballroom times a billion

    show bella 1a at r1_5
    show npc2 at center

    show bella 1a zorder 1.0
    b "Here’s your cake, sir."

    show npc2 zorder 2.0
    n2 "Perfect."

    show bella zorder 3.0
    show bella at eout(.8,1.4)
    b "Call me if you have any other requests, sir."

    n2 "Yeah, yeah."
    
    hide bella

    n2 "Wait, did the maid always look like that?"

    # TODO mark last part complete, set current room to ballroom

    return # TODO jump mini_main

label c1_fetch4:
    
    scene bg guestroom with cfade
    #TODO: replace with ballroom bg

    "Fetch quest 4"

    show npc4 at l1_5
    show mc 1b at r1_5

    n4 "The food here is rather lacking. I prefer the cuisine from Bertrose much more."

    s "I’ll request for an order of cuisine from Bertrose right away, ma’am."

    # TODO either mark 1st part complete or set room to kitchen (automatic transition to next scene)
    
    scene bg kitchen with cfade
    #placeholder: not in actual game

    show npc3 at r1_5
    show mc 1b at l1_5
    #TODO: replace maid w/ chef, and insert luna part in actual game

    n3 "I’ll make the food for you."

    n3 "Can you wash the dishes while you wait? Mother won’t be happy if she finds out that the dishes aren’t done."

    s "Yes, I can wash them."

    "some time later..."

    s "Is the food finished?"

    n3 "Oh, I gave it to Bella."

    s 4b "...Bella?"

    n3 "Yeah, she said that she would take the food for you."

    s "I see. Thank you for telling me."
    
    scene bg guestroom with cfade

    show npc4 at l1_5
    show bella 1a at r1_5

    n4 "So there is the possibility of good food. Tell your master to add Bertrose food on the menu next time, or else I’m not attending."

    show npc4 at eout(.8,-1.0)

    b "Of course, ma’am."

    hide npc4
    show bella 1a at ein(1.2,.2)
    show mc 1b at einf(1.2,.9,.8)

    pause 1.2

    $ node_unlock('c1_fetch4')

    menu:

        b 5a "...Hmmm?"

        # TODO mark part as complete/set room to ballroom

        "Do nothing":

            b 10a "What are you staring at? Don’t you have work to do as the head maid?"

            show bella 10a at eout(1.2,1.4)
            #TODO: make mc sprite shake when bella walks by + sound

            $ focus_on(['bella'])

            "Bella leaves to complete more tasks."

            $ node_unlock('c1_fetch4_n')

            hide bella

        "Confront Bella":

            s 1b "Why have you been taking my tasks?"

            b 1a "Oh, it’s you." 

            b 5a "You already have enough errands to do as a head maid, why shouldn’t {i}I{/i} be able to take up a few of them?"

            b 6a "You must be proud, huh?"

            b "Finding every little nitpick to report others on just because you’re the head maid. Why don’t you go do that while I do the real tasks?"

            b "You don’t even understand what it means to be punished."

            show bella 5a at eout(.8,1.4)
            #TODO: make mc sprite shake when bella walks by + sound

            $ focus_on(['bella'])

            $ c1_saw_bella_watch = True

            "Bella strides off to complete more tasks and accidentally leaves behind her pocket watch." 
            
            $ node_unlock('c1_fetch4_c')

            hide bella

            menu:

                "Leave it behind":

                    "skill issue lmao"

                    $ node_unlock('c1_fetch4_c_leave')

                    pass # This ends the scene
                "Pick it up":

                    "you got Bella's pocket watch! yippee!"
                    
                    $ node_unlock('c1_fetch4_c_pickup')

                    $ c1_has_bella_watch = True
    return # TODO jump mini_main

label c1_scene5:
    
    scene bg guestroom with cfade
    #TODO: replace w/ ballroom bg
    
    "Scene 5"

    show mc 1a at center
    $ focus_on(['mc'], {'mc': 3})
    "Anastasia goes to the ballroom and looks out a window. There’s an intense blizzard outside."

    show mc 1b
    "She looks at the pocket watch. It’s time."

    scene bg hallway with cfade

    show mc 1b at offscreenleft
    show mc 1b at ein(1.3,.2)
    show mother 1a at r1_5

    "She walks away and goes to look for Mother, who waves her over."

    m "Anastasia, please inform the rest of the maids to go to Room 7 for the inspection."

    s "Yes, Mother."

    $ node_unlock('c1_scene5')

    return

label c1_scene6:
    
    scene bg guestroom with cfade

    $ node_unlock('c1_scene6')

    stop ambience

    "Mother inspection"

    "Anastasia walks through the hallways and tells any maids that she finds to go to the room that Mother is in."
        
    scene bg guestroom with cfade
    
    $ focus_on(['bella','amelia'])
    show bella 5a at left
    show amelia 1a at l1_3
    pause.5
    show mc 1b at einf(1.2,.9,.9)
    "Anastasia eventually comes across Amelia and Bella in Room 2, talking to each other in low voices."

    $ focus_on(['bella','amelia'])
    "Amelia looks better than when Anastasia last saw her, although Bella seems upset with her."

    b 6a "Why didn’t you tell me you were sick?!"

    a "Mother or the other maids might’ve overheard, and I didn’t want you to worry..."

    b "Of course I would worry!"

    show bella 5a
    a "Bella, I… I also didn’t want you to have to make up my tasks, especially since you were already so tired from doing so many…"

    a "I—"

    show amelia 6a

    $ focus_on(['amelia','mc'])
    "Amelia suddenly spots Anastasia at the entrance of the room." 
    
    show bella 10a

    $ focus_on(['bella'])
    "Bella quickly turns around and also sees her."

    b "Why are you here?"

    s "Mother wants the maids to gather at Room 7 for inspection."

    b 5a "Fine."

    b 10a "Wait... Did you hear what we were talking about?"

    s "..."

    b "Did you, or did you not—"

    show amelia 1a
    a "Let’s just go, Bella."

    show amelia at eout(.8,-.8)
    show bella 5a at eout(.8,-.8)

    scene black with dissolve
    play sound clothes_rustle volume 2.0

    "Anastasia searches for any other maids in the remaining rooms, then goes to Room 7, where Mother and the other maids are waiting." 

    scene bg guestroom with cfade

    show amelia 6a at xal(.265)
    show bella 5a at xal(-.045)
    show mother 1a at r1_4
    show mc 1b at einf(1.4,.8,1.0902)

    m "Anastasia."
    # TODO calculate player’s completion here
        
        #{[player completion/progress good]

            #m 2a "Your work today was excellent."

            #m "Everyone should follow Anastasia’s example."

            #m "This is what a good maid should be."}

        #{[player completion/progress mid]

            #m "Your work today was… a little inadequate, but I hope that you will do better next time."}

        #{[player completion/progress bad]

            #m 6a "Your work today was… quite frankly, dreadful." 

            #m 1a "I am rather stunned that you managed to stoop this low, considering the fact that you were always the highest performing maid."

            #m "Please improve next time, dear. You’re not making the best example for the other maids."}

    m 1a "Now, my dears, I’ve been inspecting the rooms and hallways, and almost everything seems to be in place."

    m 5a "However, one of the guestrooms has not been properly cleaned."

    m 6a "In fact, it was this room that was not cleaned."

    menu:

        m "Anastasia, did you see any maids disobeying my orders?"

        "Yes":

            s "Yes, I did see a disobedient maid."

            m "Who was it?"

            menu:

                #$ focus_on(['mother'])

                m "Who was it?"

                "Amelia":

                    $ c1_justify_blame = True

                    call c1_amelia_ending from _call_c1_amelia_ending

                "Bella" if c1_has_bella_watch:

                    #$ c1_blame_bella dialogue = True

                    call c1_bella_ending from _call_c1_bella_ending
                "Anastasia":

                    #$ mc_takes_blame = True

                    call c1_mc_ending from _call_c1_mc_ending
        "No":

            $ focus_on(['mc'])

            "Anastasia shakes her head." 

            m "Are you sure you did not?"

            menu:
                "Are you sure you did not?"

                "Not sure":
                    menu:
                        "Who was it?"
                        "Amelia":
                            call c1_amelia_ending from _call_c1_amelia_ending_1
                        "Bella" if c1_has_bella_watch:
                            call c1_bella_ending from _call_c1_bella_ending_1
                "Yes":
                    menu:
                        "Were there any idle maids?"
                        "Yes":
                            menu:
                                "Amelia":
                                    call c1_amelia_ending from _call_c1_amelia_ending_2
                                "Bella" if c1_has_bella_watch:
                                    call c1_bella_ending from _call_c1_bella_ending_2
                                "Anastasia":
                                    call c1_mc_ending from _call_c1_mc_ending_1
                        "No":
                            menu:
                                "Did you see anything unusual?"
                                "Yes":
                                    menu:
                                        "What was that?"
                                        "Amelia":
                                            call c1_amelia_ending from _call_c1_amelia_ending_3
                                        "Bella" if c1_has_bella_watch:
                                            call c1_bella_ending from _call_c1_bella_ending_3
                                "No":
                                    menu:
                                        "Who would you suspect?"
                                        "Amelia":
                                            call c1_amelia_ending(c1_justify_blame=False) from _call_c1_amelia_ending_4
                                        "Bella" if c1_has_bella_watch:
                                            call c1_bella_ending(c1_justify_blame=False) from _call_c1_bella_ending_4
                                        "Anastasia":
                                            call c1_mc_ending from _call_c1_mc_ending_2
        "Say nothing":

            m "Anastasia? Who was it?"

            menu:
                "Who was it?"
                "Amelia":
                    call c1_amelia_ending from _call_c1_amelia_ending_5
                "Bella" if c1_has_bella_watch:
                    call c1_bella_ending from _call_c1_bella_ending_5
                "Anastasia":
                    call c1_mc_ending from _call_c1_mc_ending_3
                "Say nothing":
                    menu:
                        "bella accuses, mother asks 'is this true?'"
                        "Bella" if c1_has_bella_watch:
                            call c1_bella_ending(c1_blame_bella_dialogue=False) from _call_c1_bella_ending_6
                        "Say nothing":
                            call c1_mc_ending("gets_accused") from _call_c1_mc_ending_4
    return

label c1_amelia_ending(c1_justify_blame=True):
    $ c1_ending = "amelia"
    if c1_justify_blame:
        s "That would be Amelia. She had not been working on her tasks and was instead resting in this room."
    else:
        s "That would be Amelia."

    $ node_unlock('c1_amelia_blame')

    #might change sequence of shocked faces later... -jade

    show amelia 8a zorder .001
    a "!!!"
    
    show bella 9a zorder .002
    b "!!!"

    m 1a "Ah."

    $ focus_on(['mother'])
    "Mother looks at Amelia."

    m 5a "Amelia…"

    show amelia zorder .003
    a "N-no, Mother! I—"

    m 7a "There’s no need to panic, my dear Amelia. Just answer one question."

    m 1a "Is this true?" 

    a "M-Mother, I—"

    m 5a "Amelia, my dear… just calm down and answer the question."

    a 6a "I-I’m sorry, I just… I was tired. We were working the whole day, and I—"

    m 1a "Oh, Amelia…"

    m "I still remember the day we first met. You were all alone, in the snow, because your parents thought you weren’t good enough. ‘A {i}failure{/i}’, that’s what they thought."

    a 8a "!!!"

    a "Mo—"

    m 6a "But {i}I{/i} believed in you. {i}I{/i} took you in; {i}I{/i} gave you food; {i}I{/i} gave you an education; and {i}I{/i} gave you a place to call home."

    m 1a "In exchange for everything I’ve given you, I’m not asking for much in return. In fact, you just need to contribute to this family."

    #not sure abt this expression -jade
    m "I love this family. I {i}really{/i} do. But if this keeps happening, this family won’t be able to stay together anymore, and some people will have to {i}leave{/i}."

    #nor this one -jade
    m 7a "You wouldn't want that to happen, {i}would you{/i}?"

    a 7a "N-no, w-wait! Please, Mother— Just give me another chance! I— I’ll do better!"

    m 1a "I want to believe you; I really do. But looking at the current situation, I’m not sure if I should."

    a "P-please, Mother! I— I’ll do anything! J-just let me stay!"

    m "In that case, please do clean up this room."

    a 5a "Yes! I can do that."

    m "Oh, I almost forgot— The owner just told me that they needed an extra hand for the cleanup at the ballroom today."

    a 1a "I… I can do that too."

    m 3a "Why {i}thank you{/i}, Amelia. I was worried about who to assign it to."

    m 5a "Hmm… there was another task, was there not?" 
    
    m 1a "Joanne, do you recall what it was?"

    show npc3 with Dissolve(.6,alpha=True)
    show npc3 zorder .05

    n3 "I-it was shoveling the snow on the rooftop, Mother."

    show mother 1a zorder .1
    m "I see. Joanne, is there currently anyone available for the task?"

    show npc3 zorder .2
    n3  "Um…"

    show mother 2a zorder .3
    m "Joanne, you made a mistake at the last manor, but I can see that you’ve been working hard to make up for it. That’s excellent."

    show npc3 zorder .4
    n3  "Th-thank you, Mother. Everyone’s— everyone has been booked today."

    show mother 1a zorder .5
    m "Ah, that’s not good. As a family, we’ve all been working to complete our tasks diligently, but it seems that this isn’t quite enough."

    m "To belong in a family means that everyone must work together and contribute. Someone that doesn’t do their work properly is just a {i}burden{/i} to everyone else. Wouldn’t you agree, Joanne?"

    show npc3 zorder .6
    n3 "I-I agree, Mother."

    show amelia zorder .65
    a "I… I’ll do it."
    #might change expression later -jade

    show mother 1a zorder .7
    m "Hmm?"

    hide npc3 with dissolve

    a "I’ll also help shovel the snow."

    show bella 8a
    m 2a "Good girl. I can tell that you really are seeking to help out the family, Amelia."

    a "Yes, I— y-you won’t kick me out, r-right?"

    m "Of course not. If you are able to complete all of these tasks perfectly, it would lighten everyone’s burden greatly. We would all be thankful to you."

    m 3a "Everyone, thank you for coming, and I {i}encourage{/i} you all to keep up the excellent work. You are all dismissed."

    $ focus_on(['mc'])
    show mc 1b at eout(1.0,1.5)

    "Anastasia leaves the room with the other maids." 
    
    $ focus_on(['bella'])
    show bella 5a
    "At first, Bella doesn’t move and apprehensively looks at Amelia for a moment..."
    
    pause .9
    show bella 8a at eout(2.2,1.4)
    "But she quickly steels herself and leaves as well."

    scene black with dissolve

    scene bg hellway
    #TODO: replace w/ rooftop later
    show snowback
    show black

    "Some time later..."

    pause 1.2

    hide black with dissolve

    play ambience wind_howling_ambience fadein .57

    show amelia 7a
    show snowfront

    a "N-no! I— I can’t do it! I can’t shovel all the snow by myself! Wh-what am I going to do?!"

    a 8a "If Mother finds out, she’ll be disappointed in me— she’ll kick me out!"

    a 7a "Th-this is all my fault—"

    a "I’m— I’m pathetic! I’m a failure! No one will love me!"

    a "What am I going to do?!"

    a "I—"

    $ focus_on(['amelia'])
    "In the midst of her panic, Amelia looks out at the edge of the roof, where the snow falls off towards the ground below."

    a 6a "Maybe… that’s the only way…"

    stop ambience fadeout 2.0

    #[fade to black; end scene]

    #[snowy courtyard/whatever]

    show black with dissolve

    scene bg hellway
    #TODO: replace w/ rooftop later
    show snowback
    show black

    pause 1.5

    hide black with dissolve
    
    #TODO: replace w/ snowy bg later 

    #TODO: replace sprites later 

    show npc3_1 at l1_5
    show npc3 at r1_5

    show snowfront

    play ambience wind_howling_ambience fadein .6

    $ npc3_name = "MAID 1"
    $ npc3_1_name = "MAID 2"

    n3 "It’s s-so cold out here..."

    n3_1 "Can’t do much about it. The nobles are going to leave soon and if we don’t clear out the snow in the path, the cars won’t be able to leave."

    n3 "I guess."

    show npc4 at offscreenleft
    $ npc4_name = "MAID 3"

    show bg hellway with vpunch 
    #show bg hellway with hpunch
    n4 "AHHHHHHHHH!!!"

    n3_1 "W-what’s going on?"

    n3 "Oh my god!"

    hide snowfront
    show mc 5a
    show snowfront
    show npc3_1 at ein(.5,.05)
    show npc3 at ein(.5,.95)
    s "Step aside."

    stop ambience fadeout 2.0
    scene black with dissolve

    hide mc 5a
    hide npc3_1
    hide npc3
    hide npc4

    "At first glance, it seems that the normally pure white snow is only marred by a few drops of blood." 

    "But as Anastasia traces the trail of blood with her eyes, the drops gather and multiply, transforming the snow into small, dark clumps." 

    "Those clumps of snow accumulate into large, bloody piles, and those piles of snow lead to…"

    "!!!"

    "insert dead amelia cg here..."
    #TODO: add cg here later

    $ char_kill("amelia")
    $ node_unlock('c1_amelia_end')

    #call c1_scene7 from c1_amelia_ending

    return

label c1_bella_ending(c1_blame_bella_dialogue=True, c1_justify_blame=True):
    $ c1_ending = "bella"
    if c1_blame_bella_dialogue:
        if c1_justify_blame:
            "mc gives reason for blaming bella"
        else:
            "Mc accuses bella with no reason"
    "blame bella"
    $ node_unlock('c1_bella_blame')
    "hear abt ded bella"
    $ node_unlock('c1_bella_end')
    return

label c1_mc_ending(c1_mc_type="takes_blame"):
    $ c1_ending = "mc " + c1_mc_type
    #if c1_mc_type == "takes_blame":
       # s "That would be me, Mother."

       # m "...You were the disobedient maid. I see."
    #else:

       # m "I see…"


    $ node_unlock('c1_mc_blame')

    "mother leaves; amelia and bella talk to mc"
    $ node_unlock('c1_mc_end')
    return

label c1_scene7:
    "Reached ending: [c1_ending]"



    "The end of the chapter"
    $ node_unlock('c1_scene7')
    return

label chap1_test_sprites:
    scene bg hallway

    $ focus_on(['mc'])

    show mc 1a with dissolve

    s 'This is one pose'

    'Woah nice pose!'

    s 1b 'This is another pose'

    s 3a 'i dont even remember what half these poses are send help'

    s 6b 'I REJECT MY HUMANITY JOJO!!!!'

    s 5b 'meow'

    'cat mc yay!!!'

    show mc 5b at left with move

    'hmm'

    show mc at l1_5

    'hmmm'

    show mc at l1_4

    'hmmmmmmm'

    show mc at l1_3

    'hmmMmmmmMMMMmmm'

    show mother 1a at r1_3 with dissolve

    s 'Oh hey mother'

    m 'Hello main character'

    'This dialogue is definitely not OOC... definitely :>'

    m 4a 'Check out this cool new facial expression'

    $ focus_on(['npc1'])

    show npc1 at left
    show npc2 at right
    with dissolve

    n1 'Hi im an npc'

    n2 'No way, me too!'

    s 5a '...'

    s '(how did these random npcs spawn out of nowhere??)'

    m 'Hello random npcs'

    return

label chap1_test_spritesall:

    show mc 1a
    s 'Pose a expression 1'
    s 6b 'Pose b expression 6'
    show mc 6b at flip
    s 'Get flipped >:D'
    hide mc

    show mother 1a
    m 'Pose a expression 1'
    show mother 7a
    m 'Ayo new expression???'
    show mother 8a
    m 'Pose a expression 8'
    hide mother

    show amelia 1a
    a 'What'
    a 8a 'SHOOKETH'
    hide amelia

    show bella 1a
    b 'Evil bella be like,'
    b 6a "\"I'm sorry I hurt your feelings\""
    b 8a 'Tsundere moment??????'
    hide bella

    show npc1
    n1 'testing'
    hide npc1

    show npc2
    n2 'testing'
    hide npc2

    show npc3
    n3 'testing'
    hide npc3

    show npc4
    n4 'testing'
    hide npc4

    show npc5
    n5 'testing'
    hide npc5

    return

label chap1_test_bgs:
    scene kitchen
    
    call chap1_test_spritesall from _call_chap1_test_spritesall

    jump bgprompt

label chap1_test_charmenu:
    scene bg joyce why

    menu:
        'Skip cutscene (unlock all chars)':
            $ char_unlock('mc')
            $ char_unlock('mother')
            $ char_unlock('amelia')
            $ char_unlock('bella')

            menu:
                'Commit violence? (kill chars)'

                'Yes >:)':
                    $ char_kill('amelia')
                    $ char_kill('bella')
                'NO!!!!':
                    pass
            
            return
        'Don\'t skip >:o':
            pass

    "who's the main character?"

    "hmmm, never heard of her"

    "go to the character menu - she isn't unlocked yet"

    $ focus_on(['mc'])

    show mc 1a at l1_4 with dissolve

    s "Hi I'm the main character"

    $ char_unlock('mc')

    s "Now you know who I am yay"

    show mother 1a at r1_4 with dissolve

    s "Oh hey mother"

    $ char_unlock('mother')
    
    m "Hello main character"

    "..."

    m "It's so sad that amelia died of ligma"

    s "Who's amelia?"

    m "... bro u know who amelia is"

    $ char_unlock('amelia')

    s "Oh right"

    m "Anyway,"

    m "She's dead, we had a tragic accident with the gun dlc"

    m "And the seal who is the mastermind behind everything killed her"
    
    $ char_kill('amelia')

    s "Nooooo :("

    "... also i should probably unlock Bella so u can actually see her in the menu LMAO"

    $ char_unlock('bella')

    "okay congrats now you've met bella :>"

    return

label chap1_test_snow:
    show bg seal room

    show snowback
    show mc 1b
    show snowfront

    'snow 1'

    s '...'

    return

label chap1_test_longtext:
    m "Firstly, the candles and fireplaces in the guest rooms must be lit up, and make sure to tidy any cluttered rooms that you come across."
    
    m "On the off chance that a few of the nobles might wish to rest or converse in private, it is best that we prepare the rooms ahead of time."

    a "It’s just that I keep getting these headaches and I can’t think straight."
    
    a "B-but, I’ll be fine! J-just give me a few minutes and I’ll be doing perfect work."

    'Chef' "Ah. That’s a rather uncommon sight."
    
    'Chef' "Miss, perhaps you should not stay here too long. The oil could sully your clothes. We are almost done preparing the food, and you could find a seat with your parents."

    "Luna" "OH, and they said that I couldn’t study law, because ‘it was {i}unladylike{/i},’ and ‘no {i}good{/i} family would dare marry their son to a lady like that.’"
    
    "Luna" "But why should I not be allowed to do so? There’s nothing stopping women from being good at law, and doing so doesn’t suddenly make me less of a lady. Their argument has no real basis."

    b "You must be proud, huh?"
    
    b "Finding every little nitpick to report others on just because you’re the head maid. Why don’t you go do that while I do the real tasks?"
    
    b "You don’t even understand what it means to be punished."

    m "Ah, that’s not good. As a family, we’ve all been working to complete our tasks diligently, but it seems that this isn’t quite enough."
    
    m "To belong in a family means that everyone must work together and contribute. Right, Joanne?"

    "Anastasia shoves the maids to the side."
    
    "At first glance,  it seems that the normally pure white snow is only marred by a few drops of blood."
    
    "But as Anastasia traces the trail of blood with her eyes, the drops gather and multiply, transforming the snow into small, dark clumps."
    
    "Those clumps of snow accumulate into large, bloody piles, and those piles of snow lead to…"
    
    return

label chap1_test_namechange:
    scene bg joyce why

    b 'Hi there'

    $ bella_name = 'Bella'

    b 'My name is bella'

    $ focus_on(['mother'])

    show mother 1a

    m 'Hi bella'

    b 'Mother???????'

    $ amelia_name = 'Amelia'

    a 'Mother????????????'

    $ maria_name = 'Maria'

    "Luna" "Who's mother?????????????????"

    m "im mother"

    $ mother_name = 'Mother'

    "Luna" "Oh cool nice to meet you mother"

    m 'Nice to meet you too :)'

    return

label chap1_test_audio:
    play music boowomp

    $ focus_on(['mc'])

    show mc 1a at l1_3

    s 'Hmmm nice music'

    s '...'

    show bella 1a at r1_4, flip

    s '...?'

    play audio vineboom

    b 6a 'That music SUCKS'

    show bella 1a
    show mc at flip

    stop music fadeout 1.0

    s '...'

    show mc at unflip

    s 'Ok happy?'

    return

label chap1_test_animation:
    $ focus_on(['mc', 'mother', 'bella', 'amelia'])

    show mc 1a at boogie, left
    show mother 1a at boogie, l1_3
    show bella 1a at boogie, r1_3
    show amelia 1a at boogie, right
    pause

    $ focus_dict.clear()

    return

label chap1_test_part2:
    scene bg hallway with cfade

    show mc 1b

    $ focus_on(['mc'])

    s "minigame over, your score was [completion]"

    return

label c1_give_item_prompt(npc=None, goal_choice=''):
    $ ichoice = 'air'

    while True:
        call give_item_prompt from _call_give_item_prompt
        if not ichoice or ichoice == goal_choice:
            return
        if ichoice == 'dish_dirty':
            npc "What— What is this?! Why are you giving me your dirty dishes?!"

            s "I am extremely sorry; I’ll go get what you wanted."

            npc "These maids, honestly."
        elif item_is_of_type(ichoice, 'food'):
            npc "This… this is {i}not{/i} what I wanted."

            s "My apologies, I’ll go retrieve what you wanted."
        elif ichoice == 'candle' or ichoice == 'match':
            npc "What am I supposed to do with this?!"

            s "Perhaps it would help keep you warm at night?"

            npc "Keep— Keep me warm at night?! What are you insinuating?!"

            s "...?"

            npc "Oh lord."

            npc "I. Don’t. Need. It!"

            s "Understood."
        elif item_is_of_type(ichoice, 'jacket'):
            npc "This isn’t what I asked for, and it’s not even my jacket!"

            s "Are you quite sure you don’t want it?"

            npc "NO, I don’t want another person’s jacket! Just give me what I asked for!"

            s "Of course. My apologies."
        elif ichoice == 'wine_bottle':
            npc "I didn’t ask for any wine."

            s "Would you want a different drink?"

            npc "I would like to drink to forget this entire conversation…"

            s "I will immediately go and get another for you."

            npc "NO! I don’t need a drink! Just give me what I asked for."

            s "Understood."
        else:
            npc "This is NOT what I wanted!"

            s "Apologies, I’ll immediately go retrieve what you wanted."

            npc "...The best maid of the lot, huh?"

# TODO give item prompt but you can choose ANY item u want
label c1_give_item_prompt_HACKED(npc=None, goal_choice=''):
    $ ichoice = 'air'

    while True:
        menu:
            "Choose any item to try"
            "dirty dishes":
                $ ichoice = 'dish_dirty'
            "plates/trays of food":
                $ ichoice = 'food_blahblahblah'
            "candle/match":
                $ ichoice = 'candle'
            "jacket":
                $ ichoice = 'jacket_amogus'
            "bottle of wine":
                $ ichoice = 'wine_bottle'
            "other":
                $ ichoice = 'beesechurger'
            "(leave)":
                return
        if ichoice == 'dish_dirty':
            npc "What— What is this?! Why are you giving me your dirty dishes?!"

            s "I am extremely sorry; I’ll go get what you wanted."

            npc "These maids, honestly."
        elif item_is_of_type(ichoice, 'food'):
            npc "This… this is {i}not{/i} what I wanted."

            s "My apologies, I’ll go retrieve what you wanted."
        elif ichoice == 'candle' or ichoice == 'match':
            npc "What am I supposed to do with this?!"

            s "Perhaps it would help keep you warm at night?"

            npc "Keep— Keep me warm at night?! What are you insinuating?!"

            s "...?"

            npc "Oh lord."

            npc "I. Don’t. Need. It!"

            s "Understood."
        elif item_is_of_type(ichoice, 'jacket'):
            npc "This isn’t what I asked for, and it’s not even my jacket!"

            s "Are you quite sure you don’t want it?"

            npc "NO, I don’t want another person’s jacket! Just give me what I asked for!"

            s "Of course. My apologies."
        elif ichoice == 'wine_bottle':
            npc "I didn’t ask for any wine."

            s "Would you want a different drink?"

            npc "I would like to drink to forget this entire conversation…"

            s "I will immediately go and get another for you."

            npc "NO! I don’t need a drink! Just give me what I asked for."

            s "Understood."
        else:
            npc "This is NOT what I wanted!"

            s "Apologies, I’ll immediately go retrieve what you wanted."

            npc "...The best maid of the lot, huh?"

label chap1_test_t1:
    scene bg seal room with cfade

    # $ focus_on(['npc2'])

    show npc2 at l1_4

    show mc 1b at r1_4

    s 'hi random npc'

    n2 'welcome to the seal room, please deposit a test item 3'

    call c1_give_item_prompt(n2, 'test_3') from _call_c1_give_item_prompt

    if ichoice == 'test_3':
        n2 'good job, you chose the right item'
        $ update_inv(myitem='test_3')
        $ docurtask()

    jump mini_main

label chap1_test_t2:
    "drag left button to left square, right button to right square"

    python:
        mgame_goal = curgame['goal']
        if not 'try' in curgame:
            curgame['try'] = []
            for i in range(len(mgame_goal)):
                curgame['try'].append('')
        mgame_try = curgame['try']

    call screen mgame_dragdrop

    if is_win_listeq():
        "task 2 complete :D"
    else:
        "task 2 not complete :|"
    $ docurtask(is_win_listeq())

    jump mini_main

label c1_default_idle:
    "this task isnt available right now"

    jump mini_main

label c500_default_idle:
    "this task isnt available right now"

    jump mini_main

label chap1_test_t2_idle:
    "task 2 isnt available, go do something else"
    
    jump mini_main

label chap1_test_t6:
    scene bg guestroom with cfade

    show amelia 6a at l1_3

    a "(Man i miss bella...)"

    show bella 1a at r1_3

    a 3a "(Oh there she is)"

    a 4a "Hi bella :D"

    show amelia 3a

    b "Hi amelia"

    $ docurtask()

    jump mini_main

label task_c1_toggle:
    python:
        mgame_goal = curgame['goal']
        if not 'try' in curgame:
            curgame['try'] = []
            for i in range(len(mgame_goal)):
                curgame['try'].append(False)
        mgame_try = curgame['try']
    
    scene bg seal room

    $ hinttext = levelHints['toggle_idle']

    show screen mgame_overlay

    $ game_ret = 'refresh'
    while game_ret == 'refresh':
        call screen mgame_toggle
        $ game_ret = _return

    if game_ret == 'done':
        show screen mgame_toggle
        hide screen mgame_toggle with dissolve
    
    if game_ret == 'done':
        # kind of a cheesed method of fading out but oh well
        hide screen mgame_overlay
        scene bg joyce why
        with cfade
        "task 4 complete (hooray!!!)"
    else:
        hide screen mgame_overlay
        scene bg hellway
        with cfade
        "task 4 not complete (not hooray!!!)"
    
    $ docurtask(is_win_listeq())

    jump mini_main

label task_c1_waterpour:
    scene bg mgame_waterpour

    $ hinttext = levelHints['waterpour_idle']

    show screen mgame_overlay

    $ game_ret = 'refresh'
    while game_ret == 'refresh':
        call screen mgame_waterpour
        $ game_ret = _return

    $ docurtask(game_ret == 'done')
    if game_ret == 'done':
        show screen mgame_waterpour
        hide screen mgame_waterpour with dissolve

    jump mini_main

label task_c1_grabdishes:
    python:
        if not 'try' in curgame:
            mgame_goal = len(curgame['drag'])
            curgame['try'] = [0] * mgame_goal
            for i in range(mgame_goal):
                curgame['drag'][i]['n'] = str(i)
                curgame['drag'][i]['im'] = 'mini/tgame/grab_dropdishes/plate_dirty.png'
        mgame_try = curgame['try']
    
    scene bg hallway

    $ hinttext = levelHints['grabdishes_idle']

    $ game_ret = 'refresh'
    while game_ret == 'refresh':
        call screen mgame_dragdrop_dishes
        $ game_ret = _return
    
    $ docurtask(game_ret == 'done')
    $ curgame['try'] = [2 if x == 1 else x for x in curgame['try']]
    if game_ret == 'done':
        show screen mgame_dragdrop_dishes(shaded=False)
        show screen mgame_overlay
        hide screen mgame_dragdrop_dishes with dissolve

    jump mini_main

label task_c1_dropdishes:
    python:
        curgame['try'] = [] # reset dishes every time, in case player gained or lost some
        curgame['drag'] = []
        for i in range(invCountNum('dish_dirty')):
            curgame['try'].append(0)
            curgame['drag'].append({
                'n': str(i),
                'xp': (1200 + (i * 50)),
                'yp': 390,
                'im': curgame['im']
            })
        mgame_try = curgame['try']
    
    scene bg mgame_dropdishes

    $ hinttext = levelHints['dropdishes_idle']

    $ game_ret = 'refresh'
    while game_ret == 'refresh':
        call screen mgame_dragdrop_dishes
        $ game_ret = _return

    $ levelInfo[curlevel]['ndishes'] -= mgame_try.count(1)
    if not levelInfo[curlevel]['ndishes']:
        $ docurtask(True)
    else:
        $ docurtask(False, False)
    if game_ret == 'done':
        show screen mgame_dragdrop_dishes(shaded=False)
        show screen mgame_overlay
        hide screen mgame_dragdrop_dishes with dissolve

    jump mini_main

label task_c1_laundry:
    scene hellway

    python:
        if not 'try' in curgame:
            curgame['times'] = [0, 0, 0]
            times = curgame['times']
            for i in range(3):
                tim = renpy.random.randint(30, 60)
                while tim in times:
                    tim = renpy.random.randint(30, 60)
                times[i] = tim

            curgame['type_to_ind'] = {
                0: times.index(min(times)),
                2: times.index(max(times))
            }
            for i in range(3):
                if times[i] != min(times) and times[i] != max(times):
                    curgame['type_to_ind'][1] = i
                    break

            tot = renpy.random.randint(4, 8)
            curgame['try'] = [''] * tot
            curgame['goal'] = [''] * tot
            curgame['drag'] = []
            tot_running = 0
            for i in range(3):
                if tot - tot_running < 2 or i == 2:
                    num = tot - tot_running
                else:
                    num = renpy.random.randint(1, min(3, tot - tot_running))
                for j in range(num):
                    curgame['drag'].append({
                        'n': tot_running,
                        'xp': renpy.random.randint(350, 1300),
                        'yp': renpy.random.randint(540, 800),
                        'type': i
                    })
                    curgame['goal'][tot_running] = f"{curgame['type_to_ind'][i]}"
                    tot_running += 1
        mgame_try = curgame['try']
        mgame_goal = curgame['goal']

    $ hinttext = levelHints['laundry_idle']

    $ game_ret = 'refresh'
    while game_ret == 'refresh':
        call screen mgame_dragdrop_laundry
        $ game_ret = _return
    
    $ docurtask(game_ret == 'done')

    if game_ret == 'done':
        show screen mgame_dragdrop_laundry(shaded=False)
        show screen mgame_overlay
        hide screen mgame_dragdrop_laundry with dissolve

    jump mini_main
