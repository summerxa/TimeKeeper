 
label c1_scene1:
    
    "Scene 1 (Memory)"
    
    $ mother_name = "???"

    show snowback
    m "You will be perfect, won’t you?"
    
    show mc 3b
    s "Yes."

    m "My perfect little doll."

    show mc 1b
    s "Yes, Mother."
    
    $ char_unlock("mc") 
    $ char_unlock("mother")

    return

#animations:
    #align, xalign, and yalign set position and anchor (relative to top left) to this value, so xalign 0.0 and yalign 0.0 set current postion and anchor as 0.0,0.0
    #linear, ease, easein, easeout all move the sprites: first # affects speed (larger # = slower), second # affects position
        #linear moves sprite at level speed all thorughout
        #ease starts slow, speeds up, then ends slow
        #easein starts fast, ends slow
        #easeout starts slow, ends fast
        #linear 1.0 xalign 1.0: speed divided by 1, move to right (if start at <1.0)
    #pause (for x time), rotate (for x degrees), and repeat are self-explanatory
    #zoom, xzoom, yzoom all zoom in; xzoom and yzoom only affect horizontal/vertical
        #negative values will flip the sprite horizontally/vertically
        #set zoom to 1.0 to reset
    #linear + circles

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

    show snowmenu opac

    s "oooh, {i}fancy{i} snow"
    #end of testing
    
    return
  
label c1_scene2:
    
    scene bg joyce why with cfade
    #TODO: replace with ballroom bg later
    
    "Scene 2 (Intro + tasks)"

    $ mother_name = "MOTHER"
    $ bella_name = "???"
    $ amelia_name = "???"

    show npc2 at r1_5
    
    n2 "These are the most proficient of your maids, madam?"

    show mother 2a at flip, l2_5
        
    m "Yes, Lord Layton."

    $ npc2_name = 'LORD LAYTON'
    
    $ focus_on(['mc', 'mother'])

    show mother 2a at flip, ein(0.8, 0.2)

    show mc 1b at flip, center

    m "This is Anastasia, my best maid. She’ll do anything you say and won’t tell a soul."

    n2 "I see."

    n2 "I suppose I might hire one of your maids in the near future."

    show mother 3a
    m "I am thoroughly pleased to hear that, sir. I ensure you that my maids are—"

    show bella 8a at offscreenleft
    b "Ah!"

    play sound "<from 30.5 to 32>a lot of glass breaking.mp3" volume 0.1
    #you can change whichever glass sound to be, just reference the video times from https://www.youtube.com/watch?v=0aaPMzWYL2A
    #MAKE SURE TO MAKE VOLUME VERY QUIET BECAUSE IT'S LOUD AS HELL

    show mother 8a at unflip, lin(0.8, 0.4)

    show mc 1b at unflip, lin(0.8, 0.7)

    show npc2 at lin(0.8, 1.1)

    pause 0.7
    show bella 8a at flip, ein(0.7, 0.0)

    pause 2.5 
    show mother 5a
    m "...Ah."

    show mother 8a at flip
    m "My deepest apologies, Lord Layton. I’ll have this sorted out immediately."

    show npc2 at eout(2.0, 2.0)
    
    show mother 6a at unflip

    show bella 6a at unflip
    b "Mother, I—"

    $ focus_on(['mother', 'bella'])

    show mother 7a at ein(0.6, 0.31)

    show bella 8a
    "Mother grips the maid’s shoulder with one hand and grips her chin with the other to force the maid to look at her."
    
    hide npc2 # hiding sprites saves a teeny bit of processing power
    $ npc2_name = 'NOBLE' # reset npc name for the next time we use this character

    # uh... for some reason it shows amelia at the far left if these are merged into one line :Troy:
    show amelia 8a at eaf(1.2, 0.8, 1.0)
    a "!!!"

    $ focus_on(['amelia'])

    "Another maid looks on in horror and covers her mouth with her hand."

    m "It seems I need to {i}reeducate{/i} you, Bella."

    $ bella_name = "BELLA"
   
    show bella 6a
    b "No! I-"

    show mother 7a
    m "Now, now. You wouldn’t want to cause a ruckus for the guests, {i}would you?{/i}"

    show mother 1a at flip
    m "Could you clean this up, my dears?"

    $ focus_on(['mother', 'bella'])

    show mother 7a at flip, ea(1.2, -1.0)

    pause 0.5
    show bella 8a at flip, ea(1.0, -1.0)
    
    "Mother grips Bella’s arm tightly and drags her out of the ballroom."

    $ focus_on(['amelia'])

    #TODO: figure out what to do here LMAO; amelia's expression does NOT match 
    pause 1.0
    show amelia 7a
    "Anastasia and the other maids pull themselves together and clean up the mess."

    # turns out renpy has a built in black bg hooray -snail
    scene black with dissolve

    "One hour later…"

    scene bg joyce why with dissolve
    #TODO: replace with ballroom bg later

    $ focus_on(['mother', 'mc'])

    #TODO: animate them better
    show mc 3b at flip, r1_4

    show mother 1a at flip, ein(1.0, 0.25)

    pause .65
    show mc 1b at unflip

    "Mother returns to the ballroom alone and walks to Anastasia."

    show mother 1a
    m "Anastasia, dear."

    m "There are some tasks that I would like you to complete tonight."

    m "Firstly, the candles and fireplaces in the guest rooms must be lit up, and make sure to tidy any cluttered rooms that you come across."

    m "On the off chance that a few of the nobles might wish to rest or converse in private, it is best that we prepare the rooms ahead of time."

    m "Then, you must go to the kitchens and bring the trays of food to the ballroom. Our guests will surely still be hungry, so that would hopefully keep them satisfied." 

    m "Lastly, empty trays must be taken to the kitchen and washed lest the ball room appears disorganized."

    show mother 5a
    m "Please finish all these tasks by eight o’clock."

    show mc 3b
    s "Yes, Mother."

    show mother 1a
    m "If any of the guests require your service, you must assist them before completing your tasks."

    s "Yes, Mother."

    show mother 6a
    m "And remember to report any disobedient maids."

    show mc 4b
    s "I will."

    $ focus_on(['mother'])

    pause 1.0
    show mother 2a
    pause .5
    m "Don’t disappoint me, Anastasia."

    scene bg guestroom with cfade
    #TODO: replace with ballroom bg later

    $ focus_on(['bella'])

    show bella 8a at r1_4
    b "Ugh... Where is it? The cloth was here just a second ago!"

    show amelia 2a at flip, einf(-0.2, 1.0 ,0.25)
    a "Here, take this."

    $ focus_on(['bella'])

    show bella 1a at flip

    $ amelia_name = "AMELIA"

    pause 0.5
    b "Oh. Thanks, Amelia…"

    show amelia 3a
    a "No problem, Bella."

    $ focus_on(['bella'])

    show bella 8a
    "Bella holds her hand to her face."

    b "Tch."

    show amelia 6a
    a "Are you okay, Bella?"

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

    show amelia 1a
    a "If you say so…" 

    $ focus_on(['amelia'])

    show amelia 1a at unflip, eout(1.0, 0.2)
    "Amelia starts to walk away, but—"

    # i made an animation maybe...? -snail
    # TODO add a falling sound

    # i made the manual highlight clear after one line cuz that works *most* of the time,
    # but now you have to call focus_on after every line of narration for this section :Troy: -snail
    $ focus_on(['amelia'])

    show amelia 8a
    "!!!{w=1}{nw}" # amelia automatically falls after 1 second (has a more jarring/shocking effect?)
    # screen shake feels a lil too intense for someone falling over
    # LMK if u want a less intense shake- i can make a custom one for this scene :3 -snail
    hide amelia with vpunch

    show bella 6a #not sure if this expression quite matches up... but oh well
    b "Amelia, are you alright?!"

    show amelia 1a at flip
    a "I-I’m okay..."

    show bella 5a
    b "Are you sure? Maybe you should take a break."

    show amelia 5a #expression not quite right...
    a "No— I’m okay! It’s probably nothing."

    b "I can finish your tasks if you need me to…"

    show amelia 7a
    a "N-no, I can do them!"

    show amelia 6a
    a "I-I mean, you were already punished...the cuts are still there. Should I get more medicine? I can always make some more if you need me to…"

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

    show bella 5a
    b "Amelia, I know you've been worried about me all this time, but if you feel tired, {i}please{/i}, tell me."
    #this line... doesn't flow quite smoothly...
    # maybe remove the first "I know"- feels kinda redundant(?) idk how to word it... -snail
    # or break into two lines "...all this time" -> "But if you..." for a thoughtful pause effect :D

    show amelia 5a
    a "Don’t worry Bella, I’ll be alright."

    #WHY IS THERE NO CONCERNED/WORRIED EXPRESSION FOR BELLA AHHHH
    # maybe try 7a? it makes her look in amelia's general direction :D -snail
    b "If you say so..."

    $ char_unlock("amelia")
    $ char_unlock("bella")

    return

label c1_scene3:
    "Scene 3 (amelia sick scene)"
    return

label c1_fetch1:
    "Fetch quest 1"
    return # TODO jump mini_main

label c1_fetch2:
    "Fetch quest 2"
    return # TODO jump mini_main

label c1_fetch3:
    "Fetch quest 3"
    return # TODO jump mini_main

label c1_fetch4:
    "Fetch quest 4"
    menu:
        "Bella confrontation"

        "Do nothing":
            "mc does nothing"
        "Confront Bella":
            "mc confronts"
            $ c1_saw_bella_watch = True
            menu:
                "Bella drops pocketwatch"

                "Leave it behind":
                    pass # This ends the scene
                "Pick it up":
                    $ c1_has_bella_watch = True
    return # TODO jump mini_main

label c1_scene5:
    "Scene 5"
    return

label c1_scene6:
    menu:
        "Mother inspection"
        "Yes":
            menu:
                "Who was it?"
                "Amelia":
                    call c1_amelia_ending
                "Bella" if c1_has_bella_watch:
                    call c1_bella_ending
                "Anastasia":
                    call c1_mc_ending
        "Say nothing":
            menu:
                "Who was it?"
                "Amelia":
                    call c1_amelia_ending
                "Bella" if c1_has_bella_watch:
                    call c1_bella_ending
                "Anastasia":
                    call c1_mc_ending
                "Say nothing":
                    menu:
                        "bella accuses, mother asks 'is this true?'"
                        "Bella" if c1_has_bella_watch:
                            call c1_bella_ending(c1_blame_bella_dialogue=False)
                        "Say nothing":
                            call c1_mc_ending("gets_accused")
        "No":
            menu:
                "Are you sure you did not?"
                "Not sure":
                    menu:
                        "Who was it?"
                        "Amelia":
                            call c1_amelia_ending
                        "Bella" if c1_has_bella_watch:
                            call c1_bella_ending
                "Yes":
                    menu:
                        "Were there any idle maids?"
                        "Yes":
                            menu:
                                "Amelia":
                                    call c1_amelia_ending
                                "Bella" if c1_has_bella_watch:
                                    call c1_bella_ending
                                "Anastasia":
                                    call c1_mc_ending
                        "No":
                            menu:
                                "Did you see anything unusual?"
                                "Yes":
                                    menu:
                                        "What was that?"
                                        "Amelia":
                                            call c1_amelia_ending
                                        "Bella" if c1_has_bella_watch:
                                            call c1_bella_ending
                                "No":
                                    menu:
                                        "Who would you suspect?"
                                        "Amelia":
                                            call c1_amelia_ending(c1_justify_blame=False)
                                        "Bella" if c1_has_bella_watch:
                                            call c1_bella_ending(c1_justify_blame=False)
                                        "Anastasia":
                                            call c1_mc_ending
    return

label c1_amelia_ending(c1_justify_blame=True):
    $ c1_ending = "amelia"
    if c1_justify_blame:
        "mc gives reason for blaming amelia"
    else:
        "Mc accuses amelia with no reason"
    "blame amelia"
    "amelia by herself"
    "amelia ded"
    return

label c1_bella_ending(c1_blame_bella_dialogue=True, c1_justify_blame=True):
    $ c1_ending = "bella"
    if c1_blame_bella_dialogue:
        if c1_justify_blame:
            "mc gives reason for blaming bella"
        else:
            "Mc accuses bella with no reason"
    "blame bella"
    "hear abt ded bella"
    return

label c1_mc_ending(c1_mc_type="takes_blame"):
    $ c1_ending = "mc " + c1_mc_type
    "mc takes/gets blame"
    "mother leaves; amelia and bella talk to mc"
    return

label c1_scene7:
    "Reached ending: [c1_ending]"
    "The end of the chapter"
    return

label chap1_test_sprites:
    scene bg room

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
    menu bgprompt:
        'bg 1':
            'sorry bg 1 got deleted :('
            jump bgprompt
        'bg 2':
            scene bg guestroom
        'leave for now':
            return
    
    call chap1_test_spritesall

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

    l "OH, and they said that I couldn’t study law, because ‘it was {i}unladylike{/i},’ and ‘no {i}good{/i} family would dare marry their son to a lady like that.’"
    
    l "But why should I not be allowed to do so? There’s nothing stopping women from being good at law, and doing so doesn’t suddenly make me less of a lady. Their argument has no real basis."

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

    l "Who's mother?????????????????"

    m "im mother"

    $ mother_name = 'Mother'

    l "Oh cool nice to meet you mother"

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
    scene bg hello person reading this with cfade

    show mc 1b

    $ focus_on(['mc'])

    s "minigame over, your score was [completion]"

    return

label c1_give_item_prompt(npc=None, goal_choice=''):
    $ ichoice = 'air'

    while True:
        call give_item_prompt
        if not ichoice or ichoice == goal_choice:
            return
        if ichoice == 'dirty_dishes':
            npc "...Are those dirty dishes??"
        else:
            npc "If you're seeing this dialogue, something's broken :("

label chap1_test_t1:
    scene bg seal room with cfade

    $ focus_on(['npc2'])

    show npc2

    n2 'welcome to the seal room, please deposit a test item 3'

    call c1_give_item_prompt(n2, 'test_3')

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

    $ show_hint = False
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

label chap1_test_t3:
    $ ichoice = False
    $ showlh = (invitems[0] != 'air')
    $ showrh = (invitems[1] != 'air' and invitems[1] != invitems[0])

    call give_item_prompt(vb='Place', both_hands=True)

    if type(ichoice) is list:
        if 'test_1' in ichoice and 'test_3' in ichoice:
            'task 3 complete'
            $ update_inv(myitem='test_1', useholder=False)
            $ update_inv(myitem='test_3', useholder=False)
            $ docurtask()
        else:
            'wrong items smh'
            $ docurtask(False)
    elif ichoice:
        'why only one item smh'
        $ docurtask(False)

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

    call screen mgame_toggle
    
    if is_win_listeq():
        "task 4 complete (hooray!!!)"
    else:
        "task 4 not complete (not hooray!!!)"
    
    $ docurtask(is_win_listeq())

    $ show_hint = False
    jump mini_main

label task_c1_waterpour:
    scene bg mgame_waterpour

    $ hinttext = levelHints['waterpour_idle']

    call screen mgame_waterpour

    python:
        all_colors = []
        failed = False
        for cup in curgame['cups']:
            cup_colors = cup['colors']
            if not len(cup_colors):
                continue
            curcolor = cup_colors[0]
            for c in cup_colors:
                if c in all_colors or c != curcolor:
                    failed = True
                    break
            if failed or curcolor in all_colors:
                failed = True
                break
            all_colors.append(curcolor)

    $ docurtask(not failed)

    jump mini_main

label task_c1_grabdishes:
    python:
        if not 'try' in curgame:
            mgame_goal = len(curgame['drag'])
            curgame['try'] = [0] * mgame_goal
            for i in range(mgame_goal):
                curgame['drag'][i]['n'] = str(i)
                curgame['drag'][i]['im'] = 'mini/icon_map_mc_idle.png'
        mgame_try = curgame['try']
    
    scene bg hallway

    $ hinttext = levelHints['grabdishes_idle']

    call screen mgame_dragdrop_dishes

    $ game_ret = _return

    while game_ret == 'refresh':
        call screen mgame_dragdrop_dishes
        $ game_ret = _return
    
    $ docurtask(not 0 in mgame_try)
    $ curgame['try'] = [2 if x == 1 else x for x in curgame['try']]

    $ show_hint = False
    jump mini_main

label task_c1_dropdishes:
    python:
        curgame['try'] = [] # reset dishes every time, in case player gained or lost some
        curgame['drag'] = []
        for i in range(invCountNum('dirty_dishes')):
            curgame['try'].append(0)
            curgame['drag'].append({
                'n': str(i),
                'xp': curgame['xp'],
                'yp': (0.8 - (i * 0.1)),
                'im': curgame['im']
            })
        mgame_try = curgame['try']
    
    scene bg hallway

    $ hinttext = levelHints['dropdishes_idle']

    call screen mgame_dragdrop_dishes

    $ game_ret = _return

    while game_ret == 'refresh':
        call screen mgame_dragdrop_dishes
        $ game_ret = _return

    $ levelInfo[curlevel]['ndishes'] -= mgame_try.count(1)
    if not levelInfo[curlevel]['ndishes']:
        $ docurtask(True)
    else:
        $ docurtask(False, False)

    jump mini_main
