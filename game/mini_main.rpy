screen btn_room(bt, b_id):
    default cords = roomRects[curlevel][bt['floor']][b_id]
    default xp = (cords[2] + cords[0]) // 2
    default yp = (cords[3] + cords[1]) // 2
    textbutton bt['btext']:
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

screen btn_roomarrow(bt, hov_id):
    default act = [SetVariable('prevroom', curroom), SetVariable('curroom', bt['toroom']), SetVariable('curtime', curtime+bt['tcost']), Return('gotoroom_direct')]
    
    imagebutton:
        auto 'mini/ui/btn_room_down_%s.png'
        if bt['dir'] == 'up':
            at highlight_hov(cur_hov, hov_id), rot(180)
            ypos 0.15
        else:
            at highlight_hov(cur_hov, hov_id)
            ypos 0.85
        xpos bt['xp']
        action act
        xanchor 0.5
        yanchor 0.5
        hovered SetVariable('cur_hov', hov_id)
        unhovered SetVariable('cur_hov', None)
    textbutton bt['btext']:
        xpos bt['xp']
        if bt['dir'] == 'up':
            ypos 0.03
        else:
            ypos 0.97
        action act
        xanchor 0.5
        yanchor 0.5
        text_style 'fancy_font'
        text_size 50
        hovered SetVariable('cur_hov', hov_id)
        unhovered SetVariable('cur_hov', None)
        at highlight_hov(cur_hov, hov_id)

screen btn_tsk(bt, hov_id=None):
    if bt['curtask'] or not 'hidden' in bt:
        imagebutton:
            xpos bt['xp'] ypos bt['yp']
            xanchor 0.5 yanchor 0.5
            if bt['curtask']:
                auto f"mini/btn_task/btn_{bt['imtask']}_task_%s.png"
                if 'item_req' in bt['curtask']:
                    if task_can_proceed(bt['curtask']['item_req']):
                        action bt['act']
                    else:
                        action SetVariable('hinttext', levelHints[bt['curtask']['fail_id']])
                else:
                    action bt['act']
            else:
                auto f"mini/btn_task/btn_{bt['imtask']}_%s.png"
                action bt['act']
            if 'htext' in bt and not len(bt['htext']) == 0:
                if bt['curtask']:
                    if Task.SPECIAL in bt['curtask']['tags']:
                        hovered [SetVariable('cur_hov', hov_id), SetVariable('hinttext', fmtSpecialTask(bt['htext']))]
                    else:
                        hovered [SetVariable('cur_hov', hov_id), SetVariable('hinttext', bt['htext'])]
                    
                    unhovered SetVariable('cur_hov', None)
                    at highlight_hov(cur_hov, hov_id)

# item holder
screen btn_item(bt, hov_id):
    imagebutton:
        xpos bt['xp']
        ypos bt['yp']
        auto itemsAll[bt['item']['id']]['im']
        action [SetVariable('curholder', bt), If(inventoryOk(bt['item']['id']), true=[Function(update_inv, useholder=True), SetVariable('hinttext', levelHints['default_idle'])], false=Show('popup_trade'))]
        hovered [SetVariable('cur_hov', hov_id), SetVariable('hinttext', fmtItemDesc(bt['item']['id'], bt['item']['stack']))]
        unhovered SetVariable('cur_hov', None)
        at highlight_hov(cur_hov, hov_id)

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
                    action [SetVariable('prevroom', curroom), SetVariable('curroom', 'main'), Function(set_room_text)]
                elif curstate == 'mgame':
                    action If(persistent.showleavewarning, true=[Show('popup_mgame_leave')], false=[Return(), With(cfade)])
                elif curstate == 'map':
                    action Hide('popup_map')
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

screen mc_hintbox:
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
        minimum (400, 250)
        viewport:
            area (10, 10, 360, 200)
            mousewheel True
            draggable True
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            text hinttext

screen mini_mapbase(floor=curfloor):
    for rname, rm in roomRects[curlevel][floor].items():
        add 'mini/map/map_roomrect.png':
            xpos rm[0] ypos rm[1]
            xanchor 0.0 yanchor 0.
            xysize (rm[2] - rm[0], rm[3] - rm[1])

screen mini_screen:
    modal True

    if curroom == 'main':
        use mini_mapbase
        use mini_sidebar
        for bn, bt in roomButtons[curlevel].items():
            if bt['floor'] == curfloor:
                use btn_room(bt, bn)
    else:
        add f"mini/map/map_{curlevel}_{curroom}.png":
            xalign 0.5 yalign 0.5
        fixed:
            xalign 0.5 yalign 0.5
            minimum (1920,1080)
            for bn, bt in taskButtons[curlevel].items():
                if curroom == bt['room']:
                    use btn_tsk(bt, bn)
            for hn, ht in itemHolders[curlevel].items():
                if curroom == ht['room']:
                    use btn_item(ht, hn)
        use mini_sidebar('inroom')
        if curroom in roomArrows[curlevel]:
            for ar in roomArrows[curlevel][curroom]:
                use btn_roomarrow(ar, f"to_{ar['toroom']}_btn")
    
    use floor_sidebar('game')
    use mc_hintbox

label mini_main():
    # TODO maybe hide quickmenu if its too obtrusive

    # TODO play soundtrack (if not playing already) - alt version based on how much time left
    # if we feeling fancy, make transition from normal to fast version smoother by calculating
    # where to start in the fast track based on position in the normal track

    scene bg mgame_main

    $ update_taskq()

    # time is not up, still remaining tasks
    if curtime < tlimit and (taskq or taskrq):
        if not was_from_roomchange():
            call screen mini_screen with cfade
        else:
            call screen mini_screen
    
        $ tolabel = _return

        jump expression tolabel
    else:
        python:
            for tname, t in tasks[curlevel].items():
                if t['tf'] >= curtime and not t['done']:
                    completion -= t['scorepenalty']

    return

label mini_launch(startroom='main', startfloor=0):
    python:
        completion = 0
        hinttext = levelHints['default_start']
        taskq.clear()
        taskrq = taskRoots[curlevel].copy()
        curroom = startroom
        prevroom = None
        curfloor = startfloor
        curholder = None
        notes_tab = 'tasks'
        tstart = levelInfo[curlevel]['t0']
        curtime = tstart
        tlimit = levelInfo[curlevel]['tf']
        invitems = ['air', 'air']
        invstacks = [1, 1]
        for bn, bt in roomButtons[curlevel].items():
            bt['btext'] = bt['name'].upper()
        for bn, bt in taskButtons[curlevel].items():
            bt['curtask'] = None
            if 'hidden' in bt:
                bt['act'] = []
            else:
                if 'taskless' in bt:
                    bt['act'] = SetVariable('hinttext', levelHints[bt['taskless']])
                else:
                    bt['act'] = SetVariable('hinttext', levelHints['default_taskless'])
        for hn, h in itemHolders[curlevel].items():
            if not 'stack' in h['item']:
                h['item']['stack'] = 1
        for tn, t in tasks[curlevel].items():
            t['activated'] = False
            t['done'] = False
            t['room'] = taskButtons[curlevel][t['btn']]['room']
        for r, ra in roomArrows[curlevel].items():
            fromroom = r
            for ar in ra:
                i1 = roomButtons[curlevel][fromroom]['num']
                i2 = roomButtons[curlevel][ar['toroom']]['num']
                tcost = roomProxim[curlevel][curfloor][i1][i2]
                aname = roomButtons[curlevel][ar['toroom']]['name'].upper()
                ar['btext'] = f'{aname}({tcost})'
                ar['tcost'] = tcost
    jump mini_main

label mini_failed:
    # TODO make this actually look good
    # TODO (check w/ others) does the game kick you out or progress story as normal?
    "Minigame failed, skill issue"
    return
