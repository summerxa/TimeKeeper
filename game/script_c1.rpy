 
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
    #highlight: $ focus_on(['bella'], {'bella': 2})

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
    # sound design is pain -snail
    # ;-; -jade

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
    "She eventually walks into Room 422, where Amelia is leaning against the wall. She seems to be in some discomfort." 

    # i think we're gonna transition into this cutscene from the tutorial minigame
    # so we may not need the intro section? -snail
    #ahh, true true -jade
    # (insert gremlin emoji here) -snail

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

    play ambience ballroom_ambience_1
    # TODO are we using ambience 1 or 2? -snail
    #idk... both are not great ;-; -jade
    # :i_cri_evry_tiem: -snail
    #sadge -jade

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
    # it looks good :D -snail

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

    show npc3_1 at r1_5
    show mc 1b at l1_5
    #TODO: replace maid w/ chef, and insert luna part in actual game

    n3_1 "I’ll make the food for you."

    n3_1 "Can you wash the dishes while you wait? Mother won’t be happy if she finds out that the dishes aren’t done."

    s "Yes, I can wash them."

    "some time later..."

    s "Is the food finished?"

    n3_1 "Oh, I gave it to Bella."

    s 4b "...Bella?"

    n3_1 "Yeah, she said that she would take the food for you."

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
            pause 0.6
            show mc at mc_gets_bonked
            play sound chain_clink
            # TODO fix the sound effects -snail

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
            pause 0.4
            show mc at mc_gets_bonked
            play sound chain_clink
            # TODO fix the sound effects -snail

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

    # TODO after adding minigame, include these 2 lines:
    # hide screen mgame_overlay
    # with cfade
    
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

    m "Anastasia, please inform the rest of the maids to go to Room 422 for the inspection."

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
    
    $ focus_on(['bella','amelia'], {'bella': 2, 'amelia': 2})
    show bella 5a at left
    show amelia 1a at l1_3
    pause.5
    show mc 1b at einf(1.2,.9,.9)
    "Anastasia eventually comes across Amelia and Bella in Room 405, talking to each other in low voices."

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

    s "Mother wants the maids to gather at Room 422 for inspection."

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

    "Anastasia searches for any other maids in the remaining rooms, then goes to Room 422, where Mother and the other maids are waiting." 

    scene bg guestroom with cfade

    show amelia 6a at xal(.265)
    show bella 5a at xal(-.045)
    show mother 1a at r1_4
    show mc 1b at einf(1.4,.8,1.0902)

    m "Anastasia."
    # TODO calculate player’s completion here
    # made a placeholder menu to test the dialogue lol -snail
    menu:
        "this is a placeholder lmao, anyway choose a completion score"

        "player completion/progress good":

            m 2a "Your work today was excellent."

            m "Everyone should follow Anastasia’s example."

            m "This is what a good maid should be."

        "player completion/progress mid":

            m "Your work today was… a little {i}inadequate{/i}, but I hope that you will do better next time."

        "player completion/progress bad":

            m 6a "Your work today was… quite frankly, {i}dreadful{/i}." 

            m 1a "I am rather stunned that you managed to stoop this {i}low{/i}, considering the fact that you were always the highest performing maid."

            m "Please improve next time, dear. You’re not making the best example for the other maids."

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

                    $ c1_blame_bella_dialogue = True

                    call c1_bella_ending from _call_c1_bella_ending
                "Anastasia":

                    $ mc_takes_blame = True

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
    # just kinda my opinion but i feel like we shud save amelia 8a for later in the inspection
    # (and use a less extreme shooketh expression here)
    # so 8a has more dramatic effect once its finally used -snail
    #gotcha -jade

    show amelia 7a zorder .001
    a "!!!"
    
    show bella 9a zorder .002
    b "!!!"

    m 1a "Ah."

    $ focus_on(['mother'])
    "Mother looks at Amelia."

    m 5a "Amelia…"

    show amelia 8a zorder .003
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
    # maybe eyes closed expression for sympathetic? like 5a or smth -snail
    m 5a "I love this family. I {i}really{/i} do. But if this keeps happening, this family won’t be able to stay together anymore, and some people will have to {i}leave{/i}."

    #nor this one -jade
    # looks fine to me lol -snail
    #mkay -jade
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
    
    $ focus_on(['bella'], {'bella': 2})
    # added a highlight to bella as she leaves the room... not sure if it looks better this way -snail
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
    show snowfront zorder 10

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

    show black zorder 11 with dissolve

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

    # 'zorder [insert big number here]' makes sure the snow is always on top -snail
    # ah true true -jade
    show snowfront zorder 10

    play ambience wind_howling_ambience fadein .6

    $ npc3_name = "MAID 1"
    $ npc3_1_name = "MAID 2"

    n3 "It’s s-so cold out here..."

    n3_1 "Can’t do much about it. The nobles are going to leave soon and if we don’t clear out the snow in the path, the cars won’t be able to leave."

    n3 "I guess."

    # btw u dont have to show a character's sprite in order to make them talk :D -snail
    #ohh, i didnt know that :0 -jade 
    $ npc4_name = "MAID 3"

    show bg hellway at vshake
    show npc3 at vshake
    show npc3_1 at vshake
    #show bg hellway with hpunch
    n4 "AHHHHHHHHH!!!"

    n3_1 "W-what’s going on?"

    n3 "Oh my god!"

    show mc 5a
    show npc3_1 at ein(.5,.05)
    show npc3 at ein(.5,.95)
    s "Step aside."

    $ npc4_name = "NOBLE" # resetting npc's name here before we forget lol -snail

    stop ambience fadeout 2.0
    scene black with dissolve

    # btw 2.0- using the "scene" statement automatically hides all the sprites hehe -snail
    #ahh, gotcha -jade

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

            s "That would be Bella."

            show amelia 8a

            b 9a "WHAT!?"

            s "Bella was taking my tasks earlier."

            s "She interrupted me while I was assisting some nobles, and she hastily dropped her pocket watch when I confronted her about it."

        else:
            
            s "That would be Bella."

            show amelia 8a

            b 9a "WHAT!?"

    $ node_unlock('c1_bella_blame')

    m 5a "Ah. I see."

    b "Mother, that wasn’t what I was doing, I—"

    m 6a "Oh, Bella. Please quiet down, dear."

    m "You made a mistake right as I was informing the lord of our services, and now this?"

    m 7a "It seems that you haven’t learned enough from your last punishment."

    b 6a "No— Mother, I’ll do better, I swear! Just—"

    show bella 5a
    m "No, you’ve already proven that you need more discipline."

    m 8a "Everyone else, excellent work today! I {i}encourage{/i} you all to finish your other tasks, thank you."

    $ focus_on(['amelia'])
    show amelia 6a at eout(1.8,1.4)
    "Amelia anxiously leaves the room with the other maids."

    m 1a "Anastasia? Please close the door on your way out. And make sure the rest of the maids don’t misbehave while I deal with Bella."

    s "Yes, Mother."

    $ focus_on(["mc"])
    "Anastasia leaves the room."
    #is this line really needed? -jade

    scene bg hallway with cfade
    #TODO: insert cg here

    "Anastasia cleans the tables in the ballroom. She sees a few maids huddled together conspiratorially."

    $ npc3_name = "MAID 1"
    $ npc3_1_name = "MAID 2"

    n3 "Did you know what happened to Bella?"

    n3_1 "Shh! I heard that after Mother left, someone looked into the room and saw Bella’s body!"

    $ char_kill("bella")

    n3 "Oh my gosh! Does that mean…?"

    n3_1 "Poor Amelia…"

    "Anastasia finishes cleaning the tables and walks through a hallway when she suddenly catches a glimpse of Amelia."

    #cg: [amelia has puffy eyes and dried tear marks]

    "Amelia is clutching her pocket watch when she sees Anastasia. She looks away."

    s "..."

    "Anastasia walks by her and doesn’t look back."

    scene black with dissolve

    $ node_unlock('c1_bella_end')
    return

label c1_mc_ending(c1_mc_type="takes_blame"):
    $ c1_ending = "mc " + c1_mc_type
    if c1_mc_type == "takes_blame":
        s "That would be me, Mother."

        m "...You were the disobedient maid. I see."
    
    else:

        m "I see…"

    $ node_unlock('c1_mc_blame')

    $ focus_on(["mother"])

    "Mother steps towards the furniture that has not been dusted."

    m "Clean these."

    $ focus_on(["mc"])
    "Anastasia takes out her feather duster and dusts the tables, lamps, and bed." 

    m "Again."

    $ focus_on(["mc"])
    "Anastasia dusts the furniture again, faster this time."

    m "Clean the entire room." 

    #[might add moreee]

    m "The rest of you are dismissed."

    #[All the maids shuffle out of the room.]

    $ focus_on(["amelia","bella"])
    show bella 1a at eout(1.7,1.4)
    show amelia 1a at eout(1.6,1.4)
    #fix later
    "Amelia stops to glance at Anastasia worriedly, but Bella quickly ushers her out of the room."

    hide amelia
    hide bella

    #fix this later -jade

    $ focus_on(['mother',"mc"],{"mc":2})
    show mother 1a at ein(1.2,.2)
    show mc 1b at ein(.8,.8)
    "Mother watches the maids leave before closing the door behind them and snapping her attention back on Anastasia."

    "Anastasia finishes cleaning the entire room."

    m "Clean the room again."

    $ focus_on(["mother","mc"])
    "Mother coolly watches as Anastasia cleans the room, over and over again."

    m "Clean this area again."

    m "You missed a spot. Dust the entire floor again." 

    scene black with dissolve

    "One hour later…"

    scene bg guestroom with cfade

    show mother 1a at l1_5
    show mc 1b at r1_5

    m "This is all for your own good, Anastasia."

    m "You will follow orders next time, yes?"

    s "Yes, Mother."

    m "Once you are done cleaning yourself up, come find me in the ballroom."

    m "Do not disappoint me again."

    s "Understood, Mother."

    $ focus_on(["mother"])
    show mother 1a at eout(1.4,1.4)

    "Mother leaves the room."

    hide mother

    #TODO: [door creaks or maybe footsteps sound]
    ""

    s "...?"

    $ focus_on(["mc","amelia"])
    
    show mc 4b at ein(1.0,.2)
    show amelia 1a at einf(1.4,1.2,.8)

    "Anastasia looks up to see Amelia quietly walk in with a small container in her hands."

    a "Hi Anastasia... are you okay?"

    s "Amelia?"

    a "Here… I-I brought some medicine for your hands. I hope it helps with the pain."

    s "What are you doing?"
    
    if c1_mc_type == "takes_blame":

        a "You protected me and took the punishment in my place. You didn’t have to do that. In fact, I admire your courage. I’ve always been so scared to do, well, much of anything."

        a "Anyways, thank you. There’s no way I could leave you like this."

    else:

        a "Bella blamed you for my mistake, and you didn't say anything. You could’ve told Mother the truth, or you could’ve even lied and said that it was Bella who didn’t follow orders."

        a "Even though Bella forced you to take the punishment in my stead, you went along with her lie and protected me."

        a "So, thank you. There’s no way I could leave you like this."

    #TODO: [door opens noise]

    a 6a "!!!"

    show amelia 1a at ein(.8,.7)
    show bella 1a at einf(1.4,1.0,1.0)

    if c1_mc_type == "takes_blame":

        b "Hey Amelia, here’s the bandages you asked me to get."

    else:

        b "Hey Amelia… here’s the bandages you asked me to get."

    a 4a "Bella!"

    if c1_mc_type == "takes_blame":

        b "...So that’s what the bandages are for?"

        a "Um, yeah! Anastasia, could you hold out your hands, please? If-if that isn’t too much, of course!"

    else:

        b "I still can’t believe that you’re helping her…"

        a "After everything that happened?! Bella— why shouldn’t I?!"

        b "How do you know that she wasn’t going to tell Mother the truth?! Hell, she might’ve even blamed me! Either of us could’ve been punished because of her!"

        a "But Anastasia didn’t do any of that! You were the one who lied and shifted the blame onto someone else!"

        b "But—"

        a "Am I wrong?"

        b "...No."

        s "..."

        a "Um… a-anyways, Anastasia, could you hold out your hands, please? If-if that wouldn’t be too much, of course!"

    s "I still fail to understand why you would do this. I am merely facing the consequences of my incompetence."

    b "Jesus christ, are you a robot?"

    SOPHORNIA "I can assure you, I am not a robot. As you can see from the scratch on my arm here, I have blood circulating within me, not metal circuits."

    b "...I don’t even know whether to laugh or cry."

    "Amelia turns to Anastasia and unrolls the bandages, and then starts carefully wrapping them around Anastasia’s arm."

    if c1_mc_type == "takes_blame":

        a "Bella, try to be nice to Anastasia, okay? She did help me…"

    else:

        a "Bella, be nice to Anastasia, okay? She did help me, e-even though you did blame her for what I did."

    b "Ugh."

    if c1_mc_type == "takes_blame":

        a "Bella...you did something, didn’t you?"

        b "Uh, maybe."

        a "Oh—"

        a "I’m really sorry for everything Bella did."

    else:

        a "I’m really, {i}really{/i} sorry for everything Bella did!"

    s "..."

    a "Bella..."

    b "Ugh, I’m sorry for taking your tasks, but I don’t regret it. Wasn’t gonna get punished again."

    a "Bella!"

    b "Fine... I’m sorry that I was being rude, and I won’t do that again."

    b "And..." 

    if c1_mc_type == "takes_blame":

        b "Thank you for protecting Amelia."

    else:

        b "I’m sorry for blaming you for what Amelia did." 

        b "Thank you for protecting Amelia, despite the fact that you had every reason not to."

    b "A-anyways, do you have the time, Amelia?"

    a "Um… it’s half past nine. Why do you ask?"

    b "Nothing, it’s just that I lost my pocket watch earlier."

    a "What? When?"

    b "I think it might’ve been when I was helping out another noble, but I don’t really know."

    if not c1_has_bella_watch:

        if not c1_saw_bella_watch:

            a "Maybe you dropped it in the ballroom?"

            b "I guess so…"

        else:

            s "You dropped it after I confronted you about taking my tasks."

            b "That’s where it is? I can't believe I dropped it…"

        b "Hopefully I can still find it…"

        a "I’m sure you’ll be able to, Bella! I can help."

        b "I’ll take you up on your offer if I can’t find it after a while."

        b "Well, I guess I better go find it. See ya, Amelia. And… you too, I guess."

        a "Bella!"

        "Bella leaves the room."

        a "Well, that’s… one of the better apologies she’s given, honestly speaking. Could still work on the goodbye, though."

        a "Again— I’m really, really sorry for everything Bella’s done."

    if c1_has_bella_watch:

        $ c1_has_bella_watch = False

        "Anastasia pulls the pocket watch out of her pocket and presents it to Bella. In shock, she takes it from her."

        b "I— my pocket watch— where did you find it?"

        s "You dropped it after I found you serving food to the noble."

        b "What? I dropped it then?"

        b "I..."

        b "I still don’t like you, but..." 

        b "I-I guess you’re not as bad as I thought."
        #TODO: friendship meter increased! :3 -jade

        a "Hehehe...So you can be nice!"

        b "A-anyways, I have to finish my tasks."

        "Bella hurriedly leaves the room."

        #[amelia smiles]

        a "You know... that’s the best ‘thank you’ I ever heard Bella give."

    "Amelia finishes bandaging Anastasia’s hands."

    a "...And there we go!"

    a "Do your hands feel better now?"

    "Anastasia nods."

    a "That’s great. I know that the soap that we use can really hurt, especially when your hands have cuts, so it’s good that the medicine helps with the pain, even at least a little."

    a "Hmm...?"

    a "Oh my gosh, it’s ten o’clock! I need to go finish my tasks!"

    a "Please keep the medicine! I made it myself, so don’t worry about needing to return it! Just remember to apply it everyday right before you go to sleep!"

    "Amelia waves goodbye to Anastasia and leaves the room."

    #[fade to black]

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
    scene bg hallway
    hide screen mgame_overlay
    with cfade
    # need to hide screen for the cutscene that plays after minigame

    show mc 1b

    $ focus_on(['mc'])

    s "minigame over, your score was [completion] and you did [completion_f] fetch quest(s)"

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

    $ game_ret = 'refresh'
    while game_ret == 'refresh':
        call screen mgame_toggle
        $ game_ret = _return

    if game_ret == 'done':
        show screen mgame_toggle(shaded=False)
        show screen mgame_overlay
        hide screen mgame_toggle with dissolve
    
    if game_ret == 'done':
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
    python:
        if not 'original' in curgame:
            curgame['original'] = []
            for c in curgame['cups']:
                curgame['original'].append(c['colors'].copy())

    scene bg mgame_waterpour

    $ hinttext = levelHints['waterpour_idle']

    $ game_ret = 'refresh'
    while game_ret == 'refresh' or game_ret == 'reset':
        call screen mgame_waterpour
        $ game_ret = _return
        if game_ret == 'reset':
            $ waterpour_init()
            $ hinttext = levelHints['waterpour_idle']

    $ docurtask(game_ret == 'done')
    if game_ret == 'done':
        show screen mgame_waterpour(shaded=False)
        show screen mgame_overlay
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
                'p': ((1200 + (i * 50)), 390),
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
                0: min(times),
                2: max(times)
            }
            curgame['ind_to_type'] = {
                min(times): 0,
                max(times): 2
            }
            for i in times:
                if i != min(times) and i != max(times):
                    curgame['type_to_ind'][1] = i
                    curgame['ind_to_type'][i] = 1
                    break
            curgame['try_map'] = {0:-1, 1:-2, 2:-3}

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
                        'p': (renpy.random.randint(350, 1300), renpy.random.randint(540, 800)),
                        'type': i
                    })
                    curgame['goal'][tot_running] = [f"{-(i+1)}", i]
                    tot_running += 1
        mgame_try = curgame['try']
        mgame_goal = curgame['goal']

    $ hinttext = levelHints['laundry_idle']

    $ game_ret = 'refresh'
    while game_ret == 'refresh':
        call screen mgame_laundry
        $ game_ret = _return
    
    $ docurtask(game_ret == 'done')

    if game_ret == 'done':
        show screen mgame_laundry(shaded=False)
        show screen mgame_overlay
        hide screen mgame_laundry with dissolve

    jump mini_main
