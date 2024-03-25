label chap1_test_sprites:
    scene bg room

    $ talks_next = 'mc'

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

    $ talks_next = 'npc1'

    show npc1 at left
    show npc2 at right
    with dissolve

    n1 'Hi im an npc'

    n2 'No way, me too!'

    s 5a s '...'

    s '(how did these random npcs spawn out of nowhere??)'

    show mc 5a

    m 'Hello random npcs'

    return

label chap1_test_charmenu:
    scene bg room

    menu:
        'Unlock all characters':
            $ char_unlock('mc')
            $ char_unlock('mother')
            $ char_unlock('amelia')
            $ char_unlock('bella')

            menu:
                'Commit violence?'

                'Yes >:)':
                    $ char_kill('amelia')
                    $ char_kill('bella')
                'NO!!!!':
                    pass
            
            return
        'Unlock through cutscene':
            pass

    "who's the main character?"

    "hmmm, never heard of her"

    "go to the character menu - she isn't unlocked yet"

    $ talks_next = 'mc'

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

label chap1_test_part2:
    scene bg hello person reading this

    show mc 1b

    $ talks_next = 'mc'

    s "minigame over, your score was [completion]"

    return

label c1_t1:
    'give me a test item 3 >:o'

    call give_item_prompt

    if ichoice == 'test_3':
        'good job, you chose the right item'
        $ update_inv(myitem='test_3', mystack=1)
        $ dotask(curtask)
    else:
        'no???? wrong?????'
        $ dotask(curtask, False)

    jump mini_main

label c1_t2:
    "drag left button to left square, right button to right square"

    python:
        mgame_goal = curgame['goal']
        if not 'try' in curgame:
            curgame['try'] = []
            for i in range(len(mgame_goal)):
                curgame['try'].append('')
        mgame_try = curgame['try']

    call screen mgame_dragdrop(curtask['tcost'])

    if is_win_listeq():
        "task 2 complete :D"
    else:
        "task 2 not complete :|"
    $ dotask(curtask, is_win_listeq())

    $ show_hint = False
    jump mini_main

label c1_default_idle:
    "this task isnt available right now"

    jump mini_main

label c500_default_idle:
    "this task isnt available right now"

    jump mini_main

label c1_t2_idle:
    "task 2 isnt available, go do something else"
    
    jump mini_main

label c1_t3:
    $ ichoice = False
    $ showlh = (invitems[0] != 'air')
    $ showrh = (invitems[1] != 'air' and invitems[1] != invitems[0])

    call give_item_prompt(vb='Place', both_hands=True)

    if type(ichoice) is list:
        if 'test_1' in ichoice and 'test_3' in ichoice:
            'task 3 complete'
            $ update_inv(myitem='test_1', useholder=False)
            $ update_inv(myitem='test_3', useholder=False)
            $ dotask(curtask)
        else:
            'wrong items smh'
            $ dotask(curtask, False)
    else:
        'why only one item smh'
        $ dotask(curtask, False)

    jump mini_main

label c1_t4:
    "oh no i dropped my buttons! please pick them up for me, but DONT grab anything else"

    python:
        mgame_goal = curgame['goal']
        if not 'try' in curgame:
            curgame['try'] = []
            for i in range(len(mgame_goal)):
                curgame['try'].append(False)
        mgame_try = curgame['try']

    call screen mgame_toggle(curtask['tcost'])
    
    if is_win_listeq():
        "task 4 complete (hooray!!!)"
    else:
        "task 4 not complete (not hooray!!!)"
    
    $ dotask(curtask, is_win_listeq())

    $ show_hint = False
    jump mini_main

label c1_grabdishes:
    if not 'air' in invitems and not 'dirtydishes' in invitems:
        $ hinttext = levelHints[curlevel]['grabdishes_fail']
        jump mini_main

    python:
        if not 'try' in curgame:
            mgame_goal = len(curgame['drag'])
            curgame['try'] = [0] * mgame_goal
            for i in range(mgame_goal):
                curgame['drag'][i]['n'] = str(i)
                curgame['drag'][i]['im'] = 'mini/icon_map_mc_idle.png'
        mgame_try = curgame['try']

    scene bg wassup im grabbing the dishes

    $ game_ret = 'refresh'
    while game_ret == 'refresh':
        call screen mgame_dragdrop_dishes(curtask['tcost'])
        $ game_ret = _return

    if not 0 in mgame_try:
        'yay u did task'
    else:
        'no u didnt do task'
    
    $ dotask(curtask, not 0 in mgame_try)
    $ curgame['try'] = [2 if x == 1 else x for x in curgame['try']]

    $ show_hint = False
    jump mini_main

label c1_dropdishes:
    if not 'dirtydishes' in invitems:
        $ hinttext = levelHints[curlevel]['dropdishes_fail']
        jump mini_main

    python:
        curgame['try'] = [] # reset dishes every time, in case player gained or lost some
        curgame['drag'] = []
        for i in range(invCountNum('dirtydishes')):
            curgame['try'].append(0)
            curgame['drag'].append({
                'n': str(i),
                'xp': curgame['xp'],
                'yp': (0.8 - (i * 0.1)),
                'im': curgame['im']
            })
        mgame_try = curgame['try']

    scene bg dropping the dishes off a ur moms house

    $ game_ret = 'refresh'
    while game_ret == 'refresh':
        call screen mgame_dragdrop_dishes(curtask['tcost'])
        $ game_ret = _return

    $ levelInfo[curlevel]['ndishes'] -= mgame_try.count(1)
    if not levelInfo[curlevel]['ndishes']:
        'all dishes collected'
        $ dotask(curtask, True)
    else:
        'there are still more dishes left'
        $ dotask(curtask, False, False)

    jump mini_main