screen btn_room(bt, b_id):
    default cords = roomRects[curlevel][bt['floor']][b_id]
    default xp = (cords[2] + cords[0]) // 2
    default yp = (cords[3] + cords[1]) // 2
    default tx = get_room_text(b_id)
    textbutton tx:
        xpos xp
        ypos yp
        xanchor 0.5 yanchor 0.5
        action [SetVariable('curroom', b_id), Return('gotoroom_indirect')]
        text_style 'fancy_font'
        text_align 0.5
        text_size 60
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
        action [SetVariable('prevroom', curroom), SetVariable('curroom', bt['toroom']), SetVariable('curtime', curtime+bt['tcost']), Return('gotoroom_direct')]
        hovered SetVariable('cur_hov', hov_id)
        unhovered SetVariable('cur_hov', None)
        activate_sound audio.button_click_sfx
        vbox:
            spacing -75
            if bt['dir'] == 'up':
                add 'mini/ui/btn_room_down_idle.png':
                    at highlight_hov(cur_hov, hov_id), rot(180), zm(0.5)
                    xalign 0.5
                text bt['btext']:
                    xalign 0.5 text_align 0.5
                    style 'fancy_font'
                    size 40
                    at highlight_hov(cur_hov, hov_id)
            else:
                text bt['btext']:
                    xalign 0.5 text_align 0.5
                    style 'fancy_font'
                    size 40
                    at highlight_hov(cur_hov, hov_id)
                add 'mini/ui/btn_room_down_idle.png':
                    at highlight_hov(cur_hov, hov_id), rot(0), zm(0.5)
                    xalign 0.5

screen btn_tsk(bt, hov_id=None):
    if bt['curtask'] or not 'hidden' in bt:
        imagebutton:
            pos bt['p']
            xanchor 0.5 yanchor 0.5
            if bt['curtask']:
                auto bt['imtask_active']
                if 'item_req' in bt['curtask']:
                    if task_can_proceed(bt['curtask']['item_req']):
                        action bt['act']
                    else:
                        action SetVariable('hinttext', levelHints[bt['curtask']['fail_id']])
                else:
                    action bt['act']
                activate_sound audio.button_click_sfx
            else:
                auto bt['imtask_idle']
                action bt['act']
            if 'htext' in bt and not len(bt['htext']) == 0:
                if bt['curtask']:
                    if Task.SPECIAL in bt['curtask']['tags']:
                        hovered [SetVariable('cur_hov', hov_id), SetVariable('hinttext', fmtSpecialTask(bt['htext']))]
                    else:
                        hovered [SetVariable('cur_hov', hov_id), SetVariable('hinttext', bt['htext'])]
                    
                    unhovered SetVariable('cur_hov', None)
            if bt['curtask']:
                if 'rot' in bt:
                    at highlight_hov(cur_hov, hov_id), rot(bt['rot'])
                else:
                    at highlight_hov(cur_hov, hov_id)
            else:
                if 'rot' in bt:
                    at rot(bt['rot'])
        if 'tx' in bt:
            text bt['tx']['text']:
                pos bt['p']
                xanchor 0.5 yanchor 0.5
                if 'style' in bt['tx']:
                    style bt['tx']['style']
                if bt['curtask']:
                    at highlight_hov(cur_hov, hov_id)

# item holder
screen btn_item(bt, hov_id):
    imagebutton:
        pos bt['p']
        anchor(0.5,0.5)
        auto f"mini/btn_item/item_{itemsAll[bt['item']['id']]['im']}_%s.png"
        action [SetVariable('curholder', bt), If(inventoryOk(bt['item']['id']), true=[Function(update_inv, useholder=True), SetVariable('hinttext', levelHints['default_idle'])], false=Show('popup_trade'))]
        hovered [SetVariable('cur_hov', hov_id), SetVariable('hinttext', fmtItemDesc(bt['item']['id'], bt['item']['stack']))]
        unhovered SetVariable('cur_hov', None)
        at highlight_hov(cur_hov, hov_id)
        activate_sound audio.button_click_sfx

screen mini_sidebar(curstate='main', gametype=None):
    default baseButtons = [
        {
            'y': 0.15,
            'act': Show('popup_notes'),
            'im': 'mini/ui/icon_notebook_%s.png',
            'hov_id': 'notes_btn'
        },
        {
            'y': 0.35,
            'act': Show('popup_map'),
            'im': 'mini/ui/icon_map_%s.png',
            'hov_id': 'map_btn'
        },
        {
            'y': 0.55,
            'act': Show('popup_onhand'),
            'im': 'mini/ui/icon_onhand_%s.png',
            'hov_id': 'onhand_btn'
        }
    ]

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
                    hovered SetVariable('cur_hov', bt['hov_id'])
                    unhovered SetVariable('cur_hov', None)
                    at highlight_hov(cur_hov, bt['hov_id'])
                    action bt['act']
                    activate_sound audio.button_click_sfx
            imagebutton:
                xalign 0.5
                yalign 0.75
                auto 'mini/ui/icon_help_%s.png'
                hovered SetVariable('cur_hov', 'help_btn')
                unhovered SetVariable('cur_hov', None)
                at highlight_hov(cur_hov, 'help_btn')
                if curstate == 'main' or curstate == 'inroom' or curstate == 'map':
                    action Show('popup_help', curstate='main')
                elif curstate == 'mgame':
                    action Show('popup_help', curstate=gametype)
                activate_sound audio.button_click_sfx
            imagebutton:
                xalign 0.5
                yalign 0.95
                auto 'mini/ui/icon_leave_%s.png'
                hovered SetVariable('cur_hov', 'leave_btn')
                unhovered SetVariable('cur_hov', None)
                at highlight_hov(cur_hov, 'leave_btn')
                if curstate == 'main':
                    action [ShowMenu('save')]
                elif curstate == 'inroom':
                    action [SetVariable('prevroom', curroom), SetVariable('curroom', 'main')]
                elif curstate == 'mgame':
                    action If(persistent.showleavewarning, true=[Show('popup_mgame_leave')], false=[Return(), With(cfade)])
                elif curstate == 'map':
                    action Hide('popup_map')
                activate_sound audio.button_click_sfx
        fixed:
            maximum(240, 303) # resolution of clock background image
            imagebutton:
                xalign 0.5
                yalign 0.5
                auto 'mini/ui/clock_%s.png'
                action [SetVariable('hinttext', fmtTimeHinttext())]
                hovered SetVariable('cur_hov', 'clock_btn')
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
    default act2 = [SetVariable('curtime', curtime+levelInfo[curlevel]['tstairs']), Return('gotoroom_direct')]
    if curfloor < levelInfo[curlevel]['nfloors']-1 or curstate == 'map':
        imagebutton:
            auto 'mini/ui/btn_floor_up_%s.png'
            xpos 0.14
            ypos 0.45
            xanchor 0.5
            yanchor 0.5
            if curstate == 'map':
                action SetScreenVariable('mapfloor', (mapfloor + 1) % levelInfo[curlevel]['nfloors'])
                hovered SetVariable('cur_hov', 'floor_up_btn')
            else:
                action act1 + [SetVariable('curfloor', curfloor+1)] + act2
                hovered [SetVariable('cur_hov', 'floor_up_btn'), SetVariable('hinttext', f"Go upstairs ({levelInfo[curlevel]['tstairs']} min)")]
            unhovered SetVariable('cur_hov', None)
            at highlight_hov(cur_hov, 'floor_up_btn')
            activate_sound audio.button_click_sfx
    text f'{curfloor+1}F':
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
                action SetScreenVariable('mapfloor', (mapfloor + levelInfo[curlevel]['nfloors'] - 1) % levelInfo[curlevel]['nfloors'])
                hovered SetVariable('cur_hov', 'floor_down_btn')
            else:
                action act1 + [SetVariable('curfloor', curfloor-1)] + act2
                hovered [SetVariable('cur_hov', 'floor_down_btn'), SetVariable('hinttext', f"Go downstairs ({levelInfo[curlevel]['tstairs']} min)")]
            unhovered SetVariable('cur_hov', None)
            at highlight_hov(cur_hov, 'floor_down_btn'), rot(180)
            activate_sound audio.button_click_sfx

screen mc_hintbox(shaded=True):
    if shaded:
        add 'mc minigame':
            zoom 1.05
            xalign 1.07
            yalign 0.
            matrixcolor TintMatrix('#000000') * OpacityMatrix(0.5)
    add 'mc minigame':
        zoom 1.05
        xalign 1.1
        yalign 0.5

    frame:
        xalign 0.9
        yalign 0.85
        minimum (482, 288)
        style 'hintbox_frame'
        fixed:
            area (30, 30, 400, 228)
            text hinttext:
                xalign 0.5 yalign 0.5
                text_align 0.5

screen mini_overlay(curstate='main', gametype=None, shaded=True, has_mc=True):
    use mini_sidebar(curstate, gametype)
    if has_mc:
        use mc_hintbox(shaded)

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
        use mini_overlay('inroom')
        if curroom in roomArrows[curlevel]:
            for ar in roomArrows[curlevel][curroom]:
                use btn_roomarrow(ar, f"to_{ar['toroom']}_btn")
    
    use floor_sidebar('game')

init python:
    def process_scorepenalty():
        global tasks
        global curlevel
        global curtime
        global completion
        for tname, t in tasks[curlevel].items():
            if t['tf'] >= curtime and not t['done']:
                completion -= t['scorepenalty']

label mini_main():

    $ update_taskq()

    # TODO stop skipping (if player is skipping fetch quests, it gets stuck when it returns to minigame)

    hide screen mgame_overlay

    # time is not up, still remaining tasks
    if curtime < tlimit and (taskq or taskrq) and not (len(taskq) == 1 and not taskrq and Task.DONOTHING in taskq[0]['tags']):
        # TODO maybe hide quickmenu if its too obtrusive

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
    else:
        $ process_scorepenalty()

    return

init python:
    def mini_launch_py():
        global taskButtons
        global itemHolders
        global taskrq
        global tasks
        global curlevel
        global taskTemplates
        global roomArrows

        for bn, bt in taskButtons[curlevel].items():
            bt['curtask'] = None
            if 'hidden' in bt:
                bt['act'] = []
            else:
                if 'taskless' in bt:
                    bt['act'] = SetVariable('hinttext', levelHints[bt['taskless']])
                else:
                    bt['act'] = SetVariable('hinttext', levelHints['default_taskless'])
            bt['imtask_active'] = f"mini/btn_task/btn_{bt['imtask']}_task_%s.png"
            bt['imtask_idle'] = f"mini/btn_task/btn_{bt['imtask']}_%s.png"
        for hn, h in itemHolders[curlevel].items():
            if not 'stack' in h['item']:
                h['item']['stack'] = 1
        taskrq = []
        for tn, t in tasks[curlevel].items():
            t['activated'] = False
            t['done'] = False
            t['room'] = taskButtons[curlevel][t['btn']]['room']
            if not 'tags' in t:
                t['tags'] = []
            if 'game' in t and t['game']['type'] in taskTemplates:
                for tn_, t_ in taskTemplates[t['game']['type']].items():
                    if tn_ == 'dur':
                        t['tf'] = t['t0'] + t_
                    t[tn_] = t_
            if not Task.NON_ROOT in t['tags']:
                taskrq.append(tn)
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
        tolabel = ''

        tstart = levelInfo[curlevel]['t0']
        curtime = tstart
        tlimit = levelInfo[curlevel]['tf']
        completion = 0
        completion_f = 0

        curroom = 'main'
        prevroom = levelInfo[curlevel]['room0']
        curfloor = levelInfo[curlevel]['floor0']

        curtask = None
        curtask_btn = None
        curgame = None
        taskq = []
        taskrq = []

        curholder = None
        curhand = -1
        invitems = ['air', 'air']
        invstacks = [1, 1]
        ichoice = None

        notes_text = ''
        notes_text_s = ''

        mini_launch_py()

    jump mini_main

label mini_failed:
    # TODO make this actually look good
    # also check w/ others: does the game kick you out or progress story as normal?
    "Minigame failed, skill issue"
    return
