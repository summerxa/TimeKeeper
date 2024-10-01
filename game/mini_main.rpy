screen btn_room(bt, b_id):
    default cords = roomRects[curlevel][bt['floor']][b_id]
    default xp = (cords[2] + cords[0]) // 2
    default yp = (cords[3] + cords[1]) // 2
    default tx = get_room_text(b_id)
    textbutton tx:
        xpos xp
        ypos yp
        xanchor 0.5 yanchor 0.5
        if isTutorial:
            if tutorialText[tutStep]['btn'] == b_id:
                action [Function(progressTutorial), SetVariable('curroom', b_id), Return('gotoroom_indirect')]
            else:
                action NullAction()
        else:
            action [SetVariable('curroom', b_id), Return('gotoroom_indirect')]
        text_style 'fancy_font'
        text_align 0.5
        text_size 50
        hovered SetVariable('cur_hov', f'{b_id}_room_btn')
        unhovered SetVariable('cur_hov', None)
        at highlight_hov(cur_hov, f'{b_id}_room_btn')
        activate_sound audio.button_click_sfx

screen btn_roomarrow(bt, hov_id):
    button:
        if bt['dir'] == 'up':
            ypos 0.07
        else:
            ypos 0.90
        xpos bt['xp']
        xanchor 0.5 yanchor 0.5
        if isTutorial:
            if tutorialText[tutStep]['btn'] == hov_id:
                action [Function(progressTutorial), SetVariable('prevroom', curroom), SetVariable('curroom', bt['toroom']), Function(addTime, mins=bt['tcost']), Return('gotoroom_direct')]
            else:
                action NullAction()
        else:
            action [SetVariable('prevroom', curroom), SetVariable('curroom', bt['toroom']), Function(addTime, mins=bt['tcost']), Return('gotoroom_direct')]
        hovered SetVariable('cur_hov', hov_id)
        unhovered SetVariable('cur_hov', None)
        activate_sound audio.button_click_sfx
        vbox:
            spacing -50
            if bt['dir'] == 'up':
                add 'mini/ui/btn_room_down_idle.png':
                    at highlight_hov(cur_hov, hov_id), rot(180), zm(0.5)
                    xalign 0.5
                text bt['btext']:
                    xalign 0.5 text_align 0.5
                    style 'fancy_font'
                    size 30
                    at highlight_hov(cur_hov, hov_id)
            else:
                text bt['btext']:
                    xalign 0.5 text_align 0.5
                    style 'fancy_font'
                    size 30
                    at highlight_hov(cur_hov, hov_id)
                add 'mini/ui/btn_room_down_idle.png':
                    at highlight_hov(cur_hov, hov_id), rot(0), zm(0.5)
                    xalign 0.5

screen btn_tsk(bt, hov_id=None):
    imagebutton:
        pos bt['p'] anchor (0.5, 0.5)
        if can_show_task(bt):
            # there is an active task, highlight this button
            auto bt['imtask_active']
            
            if isTutorial:
                if tutorialText[tutStep]['btn'] == hov_id:
                    action [Function(progressTutorial)] + bt['act']
                else:
                    action NullAction()
            else:
                if task_can_proceed(bt['curtask']):
                    action bt['act']
                else:
                    if 'sequence' in bt['curtask']:
                        action SetVariable('hinttext', levelHints[taskTemplates[taskq[bt['curtask']['tasktype']]['part']]['fail_id']])
                    else:
                        action SetVariable('hinttext', levelHints[bt['curtask']['fail_id']])

            # highlight and change mc textbox when hovered
            hovered [SetVariable('cur_hov', hov_id), SetVariable('hinttext', bt['htext'])]
            activate_sound audio.button_click_sfx
        else:
            # don't highlight button
            auto bt['imtask_idle']
            if fetchq:
                # noble has a request
                action SetVariable('hinttext', levelHints['quest_taskless'])
            else:
                # use the button's default "task unavailable" text
                action bt['act']

        unhovered [SetVariable('cur_hov', None), Function(setIdle)]
        # show highlights and rotation (if applicable)
        if can_show_task(bt):
            if 'rot' in bt:
                at highlight_hov(cur_hov, hov_id), rot(bt['rot'])
            else:
                at highlight_hov(cur_hov, hov_id)
        else:
            if 'rot' in bt:
                at rot(bt['rot'])
    # add text overlay on button
    if 'tx' in bt:
        text bt['tx']['text']:
            pos bt['p'] anchor (0.5, 0.5)
            if 'style' in bt['tx']:
                style bt['tx']['style']
            if can_show_task(bt):
                at highlight_hov(cur_hov, hov_id)

# item holder
screen btn_item(bt, hov_id):
    imagebutton:
        pos bt['p']
        anchor(0.5,0.5)
        auto f"mini/btn_item/item_{itemsAll[bt['item']['id']]['im']}_%s.png"
        if isTutorial:
            if tutorialText[tutStep]['btn'] == hov_id:
                action [Function(progressTutorial), SetVariable('curholder', bt), If(inventoryOk(bt['item']['id']), true=[Function(update_inv, useholder=True)], false=Show('popup_trade'))]
            else:
                action NullAction()
        else:
            action [SetVariable('curholder', bt), If(inventoryOk(bt['item']['id']), true=[Function(update_inv, useholder=True)], false=Show('popup_trade'))]
        hovered [SetVariable('cur_hov', hov_id), SetVariable('hinttext', fmtItemDesc(bt['item']['id'], bt['item']['stack']))]
        unhovered [SetVariable('cur_hov', None), Function(setIdle)]

        at highlight_hov(cur_hov, hov_id)
        activate_sound audio.button_click_sfx

# invisible button covering full screen
# only used to detect user "click to continue" during tutorial
screen btn_fullscreen(masksize=(0,0,1920,1080)):
    button: 
        add 'mini/mini_rect.png':
            anchor(0.,0.)
            pos(0,0)
            xysize(tutorialText[tutStep]['mask'][0], 1080)
            matrixcolor OpacityMatrix(0.)
        add 'mini/mini_rect.png':
            anchor(0.,0.)
            pos(tutorialText[tutStep]['mask'][0],0)
            xysize(tutorialText[tutStep]['mask'][2] - tutorialText[tutStep]['mask'][0], tutorialText[tutStep]['mask'][1])
            matrixcolor OpacityMatrix(0.)
        add 'mini/mini_rect.png':
            anchor(0.,0.)
            pos(tutorialText[tutStep]['mask'][0],tutorialText[tutStep]['mask'][3])
            xysize(tutorialText[tutStep]['mask'][2] - tutorialText[tutStep]['mask'][0], 1080)
            matrixcolor OpacityMatrix(0.)
        add 'mini/mini_rect.png':
            anchor(0.,0.)
            pos(tutorialText[tutStep]['mask'][2],0)
            xysize(1920, 1080)
            matrixcolor OpacityMatrix(0.)

        action If(isTutorial and tutorialText[tutStep]['btn'] == 'none', true=Function(progressTutorial), false=NullAction())

screen tut_lower():
    if isTutorial and tutorialText[tutStep]['btn'] == 'none':
        use btn_fullscreen(tutorialText[tutStep]['mask'])

screen tut_upper(isnotes=False):
    default opac_ = 0.75
    if isTutorial and not tutorialText[tutStep]['btn'] == 'gameplay':
        add "gui/overlay/confirm.png":
            at opac(opac_)
            anchor(0.,0.)
            pos(0,0)
            xysize(tutorialText[tutStep]['mask'][0], 1080)
        add "gui/overlay/confirm.png":
            at opac(opac_)
            anchor(0.,0.)
            pos(tutorialText[tutStep]['mask'][0],0)
            xysize(tutorialText[tutStep]['mask'][2] - tutorialText[tutStep]['mask'][0], tutorialText[tutStep]['mask'][1])
        add "gui/overlay/confirm.png":
            at opac(opac_)
            anchor(0.,0.)
            pos(tutorialText[tutStep]['mask'][0],tutorialText[tutStep]['mask'][3])
            xysize(tutorialText[tutStep]['mask'][2] - tutorialText[tutStep]['mask'][0], 1080)
        add "gui/overlay/confirm.png":
            at opac(opac_)
            anchor(0.,0.)
            pos(tutorialText[tutStep]['mask'][2],0)
            xysize(1920, 1080)
        
        if tutorialText[tutStep]['btn'] == 'none':
            
            if not isnotes:
                frame:
                    align (0.5,0.9)
                    xysize(600,100)
                    text "Click anywhere to continue":
                        align(0.5,0.5)
        use mc_hintbox(tutorialText[tutStep]['pos'], tutorialText[tutStep]['text'])

screen tut_overlay(isnotes=False):
    use tut_lower()
    use tut_upper(isnotes)

screen mini_sidebar(curstate='main', gametype=None, idle_txt=None):
    # any screen that uses the minigame sidebar cannot be hidden with middle click
    key "hide_windows" action []

    default baseButtons = [
        {
            'y': 0.15,
            'act': Show('popup_notes'),
            'im': 'mini/ui/icon_notebook_%s.png',
            'hov_id': 'notes_btn',
            'hov_txt': 'Shows the current tasks.'
        },
        {
            'y': 0.35,
            'act': Show('popup_map'),
            'im': 'mini/ui/icon_map_%s.png',
            'hov_id': 'map_btn',
            'hov_txt': 'Shows all the rooms.'
        },
        {
            'y': 0.55,
            'act': Show('popup_onhand'),
            'im': 'mini/ui/icon_onhand_%s.png',
            'hov_id': 'onhand_btn',
            'hov_txt': "Shows what items I'm holding."
        }
    ]
    default leave_hov = [SetVariable('cur_hov', 'leave_btn')]

    fixed:
        xalign 0.01
        yalign 0.
        maximum(240, 1080)
        frame:
            background "mini/ui/Billy bob joe.png"
            xalign 0.5
            yalign 1.
            maximum(189, 848)
            for bt in baseButtons:
                imagebutton:
                    xalign 0.5
                    yalign bt['y']
                    auto bt['im']
                    hovered [SetVariable('cur_hov', bt['hov_id']), SetVariable('hinttext', bt['hov_txt'])]
                    unhovered [SetVariable('cur_hov', None), Function(setIdle, idle_txt)]
                    at highlight_hov(cur_hov, bt['hov_id'])
                    if isTutorial:
                        if tutorialText[tutStep]['btn'] == bt['hov_id']:
                            action [Function(progressTutorial)] + [bt['act']]
                        else:
                            action NullAction()
                    else:
                        action [bt['act']]
                    activate_sound audio.button_click_sfx
            imagebutton:
                xalign 0.5
                yalign 0.75
                auto 'mini/ui/icon_help_%s.png'
                hovered [SetVariable('cur_hov', 'help_btn'), SetVariable('hinttext', 'Shows information on how to complete tasks.')]
                unhovered [SetVariable('cur_hov', None), Function(setIdle, idle_txt)]
                at highlight_hov(cur_hov, 'help_btn')
                if curstate == 'main' or curstate == 'inroom' or curstate == 'map':
                    if isTutorial:
                        if tutorialText[tutStep]['btn'] == 'help_btn':
                            action [Function(progressTutorial), Show('popup_help', curstate='main')]
                        else:
                            action NullAction()
                    else:
                        action Show('popup_help', curstate='main')
                elif curstate == 'mgame':
                    if isTutorial:
                        if tutorialText[tutStep]['btn'] == 'help_btn':
                            action [Function(progressTutorial), Show('popup_help', curstate=gametype)]
                        else:
                            action NullAction()
                    else:
                        action Show('popup_help', curstate=gametype)
                activate_sound audio.button_click_sfx
            imagebutton:
                xalign 0.5
                yalign 0.95
                auto 'mini/ui/icon_leave_%s.png'
                unhovered [SetVariable('cur_hov', None), Function(setIdle, idle_txt)]
                at highlight_hov(cur_hov, 'leave_btn')
                if curstate == 'main':
                    hovered leave_hov + [SetVariable('hinttext', 'Pauses the game.')]
                    if isTutorial:
                        if tutorialText[tutStep]['btn'] == 'leave_btn':
                            action [Function(progressTutorial), ShowMenu('save')]
                        else:
                            action NullAction()
                    else:
                        action ShowMenu('save')
                elif curstate == 'inroom':
                    hovered leave_hov + [SetVariable('hinttext', 'Exits the current room.')]
                    if isTutorial:
                        if tutorialText[tutStep]['btn'] == 'leave_btn':
                            action [Function(progressTutorial), SetVariable('prevroom', curroom), SetVariable('curroom', 'main')]
                        else:
                            action NullAction()
                    else:
                        action [SetVariable('prevroom', curroom), SetVariable('curroom', 'main')]
                elif curstate == 'mgame':
                    hovered leave_hov + [SetVariable('hinttext', 'Exits the current task. Note that quitting a task will still take up time.')]
                    if isTutorial:
                        if tutorialText[tutStep]['btn'] == 'leave_btn':
                            action [Function(progressTutorial), If(persistent.showleavewarning, true=[Show('popup_mgame_leave')], false=[Return(), With(cfade)])]
                        else:
                            action NullAction()
                    else:
                        action If(persistent.showleavewarning, true=[Show('popup_mgame_leave')], false=[Return(), With(cfade)])
                elif curstate == 'map':
                    hovered leave_hov + [SetVariable('hinttext', 'Exits the map.')]
                    if isTutorial:
                        if tutorialText[tutStep]['btn'] == 'leave_btn':
                            action [Function(progressTutorial), Hide('popup_map')]
                        else:
                            action NullAction()
                    else:
                        action Hide('popup_map')
                activate_sound audio.button_click_sfx
        fixed:
            maximum(240, 303) # resolution of clock background image
            imagebutton:
                xalign 0.5
                yalign 0.5
                auto 'mini/ui/clock_%s.png'
                action NullAction()
                hovered [SetVariable('cur_hov', 'clock_btn'), SetVariable('hinttext', fmtTimeHinttext())]
                unhovered SetVariable('cur_hov', None)
                at highlight_hov(cur_hov, 'clock_btn')
                activate_sound audio.button_click_sfx
            add 'mini/ui/clock_minute.png':
                xpos 0.505
                ypos 0.61
                xanchor 0.5
                yanchor 0.5
                rotate (curtime / 60) * 360
                at highlight_hov(cur_hov, 'clock_btn')
            add 'mini/ui/clock_hour.png':
                xpos 0.505
                ypos 0.61
                xanchor 0.5
                yanchor 0.5
                rotate (curtime / 720) * 360
                at highlight_hov(cur_hov, 'clock_btn')

screen floor_sidebar(curstate='game', mapfloor=0):
    default act1 = [SetVariable('prevroom', None), SetVariable('curroom', 'main')]
    default act2 = [Function(addTime, mins=levelInfo[curlevel]['tstairs']), Return('gotoroom_direct')]
    if curfloor < levelInfo[curlevel]['nfloors']-1 or curstate == 'map':
        imagebutton:
            auto 'mini/ui/btn_floor_up_%s.png'
            xpos 0.14
            ypos 0.45
            xanchor 0.5
            yanchor 0.5
            if curstate == 'map':
                if isTutorial:
                    if tutorialText[tutStep]['btn'] == 'floor_up_btn':
                        action [Function(progressTutorial), SetScreenVariable('mapfloor', (mapfloor + 1) % levelInfo[curlevel]['nfloors'])]
                    else:
                        action NullAction()
                else:
                    action SetScreenVariable('mapfloor', (mapfloor + 1) % levelInfo[curlevel]['nfloors'])
                hovered SetVariable('cur_hov', 'floor_up_btn')
            else:
                if isTutorial:
                    if tutorialText[tutStep]['btn'] == 'floor_up_btn':
                        action [Function(progressTutorial)] + act1 + [SetVariable('curfloor', curfloor+1)] + act2
                    else:
                        action NullAction()
                else:
                    action act1 + [SetVariable('curfloor', curfloor+1)] + act2
                hovered [SetVariable('cur_hov', 'floor_up_btn'), SetVariable('hinttext', f"Go upstairs ({levelInfo[curlevel]['tstairs']} min)")]
            unhovered [SetVariable('cur_hov', None), Function(setIdle)]
            at highlight_hov(cur_hov, 'floor_up_btn')
            activate_sound audio.button_click_sfx
    if curstate == 'game':
        text f'{curfloor+1}F':
            xpos 0.14
            ypos 0.5
            xanchor 0.5
            yanchor 0.5
            size 50
            style 'fancy_font'
    else:
        text f'{mapfloor+1}F':
            xpos 0.14
            ypos 0.5
            xanchor 0.5
            yanchor 0.5
            size 50
            style 'fancy_font'
    if curfloor > 0 or curstate == 'map':
        imagebutton:
            auto 'mini/ui/btn_floor_up_%s.png'
            xpos 0.14
            ypos 0.55
            xanchor 0.5
            yanchor 0.5
            if curstate == 'map':
                if isTutorial:
                    if tutorialText[tutStep]['btn'] == 'floor_down_btn':
                        action [Function(progressTutorial), SetScreenVariable('mapfloor', (mapfloor + levelInfo[curlevel]['nfloors'] - 1) % levelInfo[curlevel]['nfloors'])]
                    else:
                        action NullAction()
                else:
                    action SetScreenVariable('mapfloor', (mapfloor + levelInfo[curlevel]['nfloors'] - 1) % levelInfo[curlevel]['nfloors'])
                hovered SetVariable('cur_hov', 'floor_down_btn')
            else:
                if isTutorial:
                    if tutorialText[tutStep]['btn'] == 'floor_down_btn':
                        action [Function(progressTutorial)] + act1 + [SetVariable('curfloor', curfloor-1)] + act2
                    else:
                        action NullAction()
                else:
                    action act1 + [SetVariable('curfloor', curfloor-1)] + act2
                hovered [SetVariable('cur_hov', 'floor_down_btn'), SetVariable('hinttext', f"Go downstairs ({levelInfo[curlevel]['tstairs']} min)")]
            unhovered [SetVariable('cur_hov', None), Function(setIdle)]
            at highlight_hov(cur_hov, 'floor_down_btn'), rot(180)
            activate_sound audio.button_click_sfx

screen mc_hintbox(pos_, txt_):
    frame:
        anchor(0.,0.)
        pos pos_
        minimum (482, 288)
        style 'hintbox_frame'
        viewport:
            area (30, 30, 420, 228)

            mousewheel True
            draggable True
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"

            text txt_:
                xalign 0.5 yalign 0.5
                text_align 0.
                size 30
    zorder 10

screen mc_overlay(shaded=True):
    if shaded:
        add 'mc minigame':
            zoom 0.95
            anchor(1.,1.)
            pos(1.04,0.99)
            matrixcolor TintMatrix('#000000') * OpacityMatrix(0.5)
    add 'mc minigame':
        zoom 0.95
        anchor(1.,1.)
        pos(1.05,1.)
    
    use mc_hintbox((1350,750), hinttext)
    
    vbox:
        anchor(1.,0.)
        pos(1880, 20)
        spacing 10
        for idx, txt in [[0, 'cleanliness'], [1, 'coverage'], [2, 'service']]:
            hbox:
                xalign 1.
                spacing 10
                fixed:
                    xysize(50, 50)
                    align(0.5,0.5)
                    add 'mini/ui/[txt]Icon.png':
                        align(1.,1.)
                        matrixcolor TintMatrix('#000000') * OpacityMatrix(0.5)
                    add 'mini/ui/[txt]Icon.png':
                        align(0.5,0.5)
                fixed:
                    xysize(310, 48)
                    add 'gui/bar/right.png':
                        align(1.,1.)
                        # xysize(310, 40)
                        xysize(300,38)
                        matrixcolor TintMatrix('#000000') * OpacityMatrix(0.5)
                    bar value StaticValue(min(player_attrs[idx], levelInfo[curlevel]['level_threshold'][idx]), levelInfo[curlevel]['level_threshold'][idx]):
                        align(0.5,0.5)
                        style 'bar'
                        # left_bar Frame("gui/bar/left.png", Borders(10, 10, 10, 10), tile=gui.bar_tile)
                        # right_bar Frame("gui/bar/left.png", Borders(6, 6, 6, 6), tile=gui.bar_tile)
                        xmaximum 300
                        ymaximum 38

screen mini_overlay(curstate='main', gametype=None, shaded=True, has_mc=True, idle_txt=None):
    if curstate != 'map':
        use tut_lower()
    use mini_sidebar(curstate, gametype, idle_txt)
    if has_mc:
        use mc_overlay(shaded)

screen mini_mapbase(floor=curfloor):
    for rname, rm in roomRects[curlevel][floor].items():
        add 'mini/mini_rect.png':
            xpos rm[0] ypos rm[1]
            xanchor 0.0 yanchor 0.
            xysize (rm[2] - rm[0], rm[3] - rm[1])
            at tint('#692b22')

screen mini_screen():
    modal True

    if curroom == 'main':
        use mini_mapbase
        use mini_overlay
        for bn, bt in roomButtons[curlevel].items():
            if bt['floor'] == curfloor:
                use btn_room(bt, bn)
    else:
        viewport:
            area (0, 0, 1920, 1080)
            
            mousewheel "horizontal"
            xinitial 480
            draggable True
            fixed:
                minimum(2880, 1080)
                fixed:
                    xalign 0.5 yalign 0.5
                    xmaximum 1920
                    yminimum 1080
                    add f"mini/map/map_{curlevel}_{curroom}.png":
                        xalign 0.5 yalign 0.5
                    for bn, bt in taskButtons[curlevel].items():
                        if curroom == bt['room']:
                            use btn_tsk(bt, bn)
                    for hn, ht in itemHolders[curlevel].items():
                        if curroom == ht['room']:
                            use btn_item(ht, hn)
        if curroom in roomArrows[curlevel]:
            for ar in roomArrows[curlevel][curroom]:
                use btn_roomarrow(ar, f"to_{ar['toroom']}_btn")
        use mini_overlay('inroom')
    
    use floor_sidebar('game')

    use tut_upper()

label mini_main():

    # TODO stop skipping (if player is skipping fetch quests, it gets stuck when it returns to minigame)

    hide screen mgame_overlay

    # time is not up, still remaining tasks
    if curtime < levelInfo[curlevel]['tf']:
        # TODO maybe hide quickmenu if its too obtrusive

        stop music fadeout 1.0
        # TODO play soundtrack (if not playing already) - alt version based on how much time left
        # if we feeling fancy, make transition from normal to fast version smoother by calculating
        # where to start in the fast track based on position in the normal track

        stop ambience

        scene bg mgame_main

        if was_from_roomchange() or (curtask and Task.NO_FADE in curtask['tags']):
            call screen mini_screen
        else:
            call screen mini_screen with cfade
    
        $ tolabel = _return

        jump expression tolabel

    return

init python:
    def mini_launch_py():
        global taskButtons
        global itemHolders
        global tasks
        global curlevel
        global taskTemplates
        global roomArrows

        for bn, bt in taskButtons[curlevel].items():
            bt['curtask'] = None
            if 'taskless' in bt:
                bt['act'] = SetVariable('hinttext', levelHints[bt['taskless']])
            else:
                bt['act'] = SetVariable('hinttext', levelHints['default_taskless'])
            bt['imtask_active'] = f"mini/btn_task/btn_{bt['imtask']}_task_%s.png"
            bt['imtask_idle'] = f"mini/btn_task/btn_{bt['imtask']}_%s.png"
        for hn, h in itemHolders[curlevel].items():
            if not 'stack' in h['item']:
                h['item']['stack'] = 1
        for tn, t in tasks[curlevel]['infinite'].items():
            t['tasktype'] = tn
            for ttn, tt in taskTemplates[tn].items():
                if not ttn in t:
                    t[ttn] = tt
            if not 'tags' in t:
                t['tags'] = []
            if not t['type'] == 'small':
                taskq[tn] = {}
                if curlevel == 1 and tn == 'dishes_chain':
                    setTaskButton(tn, t, t['sequence'][0], bt_choice='6_1')
                    taskq[tn]['part'] = t['sequence'][0]
                else:
                    taskq[tn] = {}
                    if 'sequence' in t:
                        setTaskButton(tn, t, t['sequence'][0])
                        taskq[tn]['part'] = t['sequence'][0]
                    else:
                        setTaskButton(tn, t)
            else:
                bonusq[tn] = {}
                bonusq[tn]['btn'] = None
                if curlevel == 1:
                    # Make sure bonus candle quest doesn't trigger during tutorial
                    bonusq[tn]['t0'] = curtime + 31
                else:
                    bonusq[tn]['t0'] = getRandomTime(1, 20)
        for tn, t in store.tasks[store.curlevel]['single'].items():
            for ttn, tt in taskTemplates[t['tasktype']].items():
                if not ttn in t:
                    t[ttn] = tt
            if 't0' in t and t['t0'] <= curtime:
                addFquest(tn, t)
        for tn, t in store.tasks[store.curlevel]['optional'].items():
            for ttn, tt in taskTemplates[t['tasktype']].items():
                if not ttn in t:
                    t[ttn] = tt
            if 't0' in t and t['t0'] <= curtime:
                activateOptquest(tn, t)
        for r, ra in roomArrows[curlevel].items():
            fromroom = r
            for ar in ra:
                i1 = roomButtons[curlevel][fromroom]['num']
                i2 = roomButtons[curlevel][ar['toroom']]['num']
                tcost = roomProxim[curlevel][curfloor][i1][i2]
                aname = roomButtons[curlevel][ar['toroom']]['name'].upper()
                ar['btext'] = f'{aname} ◆ {tcost}'
                ar['tcost'] = tcost

label mini_launch(startroom='main', startfloor=0):
    python:
        levelInfo[curlevel]['bonus_remaining'] = 5

        tolabel = ''

        curtime = levelInfo[curlevel]['t0']

        productivity = 100.0
        player_attrs = [0, 0, 0]

        fetchq = []
        taskq = {}
        bonusq = {}

        curroom = 'main'
        prevroom = levelInfo[curlevel]['room0']
        curfloor = levelInfo[curlevel]['floor0']

        curtask = None
        curtask_btn = None
        curgame = None

        curholder = None
        curhand = -1
        invitems = ['air', 'air']
        invstacks = [1, 1]
        ichoice = None

        mini_launch_py()

    if isTutorial:
        window hide
        call screen confirm_noexit(
            "About to start tutorial.\nWould you like to skip?",
            Show(
                'confirm_noexit',
                message="Are you sure you would like to skip?\nThe tutorial contains important information on how to complete the game.",
                yes_action=[SetVariable('isTutorial', False), Return(), With(dissolve)],
                no_action=[Return(), With(dissolve)]),
            [Return(), With(dissolve)]) with dissolve
        # show screen confirm_noexit(
        #     "About to start tutorial.\nWould you like to skip?",
        #     Show(
        #         'confirm_noexit',
        #         message="Are you sure you would like to skip?\nThe tutorial contains important information on how to complete the game.",
        #         yes_action=[SetVariable('isTutorial', False), Hide('confirm_noexit')],
        #         no_action=Hide('confirm_noexit')),
        #     Hide('confirm_noexit')) with dissolve

    jump mini_main

label mini_failed:
    # TODO make this actually look good
    # also check w/ others: does the game kick you out or progress story as normal?
    "Minigame failed, skill issue"
    return
