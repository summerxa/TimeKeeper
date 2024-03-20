label chap1_test_start:
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

label chap1_test_part2:
    show mc 1b

    $ current_speaker = 'mc'

    s "minigame over, continuing regular dialogue"

    return

label c1_t1:
    call give_item_prompt

    if ichoice == 'test_1':
        'good job, you chose the right item'
        call update_inv(myitem='test_1', mystack=1, useholder=False, ret=True)
        $ dotask(curtask)
    elif ichoice == 'test_3':
        'no???? wrong?????'
        $ dotask(curtask, False)
    
    'oh yeah also could you bring item 1 and item 3 into room 3? thanks'

    jump mini_main

label c1_t2:
    "drag left button to left square, right button to right square"

    # python:
    #     mgame_goal = taskGames[curlevel][curtask['name']]['goal']
    #     if not 'try' in taskGames[curlevel][curtask['name']]:
    #         taskGames[curlevel][curtask['name']]['try'] = []
    #         for i in range(len(mgame_goal)):
    #             taskGames[curlevel][curtask['name']]['try'].append('')
    #     mgame_try = taskGames[curlevel][curtask['name']]['try']
    $ fill_try(taskGames[curlevel][curtask['name']], '')

    call screen mgame_dragdrop(taskGames[curlevel][curtask['name']], curtask['tcost'])

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

    # python:
    #     mgame_goal = taskGames[curlevel][curtask['name']]['goal']
    #     if not 'try' in taskGames[curlevel][curtask['name']]:
    #         taskGames[curlevel][curtask['name']]['try'] = []
    #         for i in range(len(mgame_goal)):
    #             taskGames[curlevel][curtask['name']]['try'].append(False)
    #     mgame_try = taskGames[curlevel][curtask['name']]['try']
    $ fill_try(taskGames[curlevel][curtask['name']], False)

    call screen mgame_toggle(taskGames[curlevel][curtask['name']], curtask['tcost'])
    
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
        tgame = taskGames[curlevel][curtask['name']]
        if not 'try' in tgame:
            mgame_goal = len(tgame['drag'])
            tgame['try'] = [0] * mgame_goal
            for i in range(mgame_goal):
                tgame['drag'][i]['n'] = str(i)
                tgame['drag'][i]['im'] = 'mini/icon_map_mc_idle.png'
        mgame_try = tgame['try']

    $ game_ret = 'refresh'
    while game_ret == 'refresh':
        call screen mgame_dragdrop_dishes(tgame, curtask['tcost'])
        $ game_ret = _return

    if not 0 in mgame_try:
        'yay u did task'
    else:
        'no u didnt do task'
    
    $ dotask(curtask, not 0 in mgame_try)
    $ tgame['try'] = [2 if x == 1 else x for x in tgame['try']]

    $ show_hint = False
    jump mini_main

label c1_dropdishes:
    if not 'dirtydishes' in invitems:
        $ hinttext = levelHints[curlevel]['dropdishes_fail']
        jump mini_main

    python:
        tgame = taskGames[curlevel][curtask['name']]
        tgame['try'] = [] # reset dishes every time, in case player gained or lost some
        tgame['drag'] = []
        for i in range(invCountNum('dirtydishes')):
            tgame['try'].append(0)
            tgame['drag'].append({
                'n': str(i),
                'xp': tgame['xp'],
                'yp': (0.8 - (i * 0.1)),
                'im': tgame['im']
            })
        mgame_try = tgame['try']

    $ game_ret = 'refresh'
    while game_ret == 'refresh':
        call screen mgame_dragdrop_dishes(tgame, curtask['tcost'])
        $ game_ret = _return

    $ levelInfo[curlevel]['alldishes'] -= mgame_try.count(1)
    if not levelInfo[curlevel]['alldishes']:
        'all dishes collected'
        $ dotask(curtask, True)
    else:
        'there are still more dishes left'
        $ dotask(curtask, False)

    jump mini_main