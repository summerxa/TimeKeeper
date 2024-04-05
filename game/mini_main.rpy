screen btn_room(b, b_id):
    textbutton b['btext']:
        xpos b['xp'] ypos b['yp'] xanchor 0.5 yanchor 0.5
        action [SetVariable('curroom', b_id), Return('gotoroom_indirect')]
        text_style 'fancy_font'
        text_align 0.5
        text_size 50
        hovered SetVariable('cur_hov', f'{b_id}_room_btn')
        unhovered SetVariable('cur_hov', None)
        at highlight_hov(cur_hov, f'{b_id}_room_btn')

screen btn_im(b, act=None):
    imagebutton:
        xpos b['xp']
        ypos b['yp']
        if 'xa' in b:
            xanchor b['xa']
            yanchor b['ya']
        else:
            xanchor 0.5
            yanchor 0.5
        if 'im' in b:
            auto b['im']
        else:
            auto 'mini/icon_map_mc_%s.png'
        # 'act' argument takes priority over pre-existing b['act']
        if act:
            action act
        elif 'act' in b:
            action b['act']
        else:
            action NullAction()
        if 'rot' in b:
            at rot(b['rot'])
        if 'htext' in b:
            hovered SetVariable('hinttext', b['htext'])

screen btn_roomarrow(b, hov_id):
    default act = [SetVariable('prevroom', curroom), SetVariable('curroom', b['toroom']), SetVariable('curtime', curtime+b['tcost']), Return('gotoroom_direct')]
    
    imagebutton:
        auto 'mini/ui/btn_room_down_%s.png'
        if b['dir'] == 'up':
            at rot(180)
            ypos 0.15
        else:
            ypos 0.85
        xpos b['xp']
        action act
        xanchor 0.5
        yanchor 0.5
        hovered SetVariable('cur_hov', hov_id)
        unhovered SetVariable('cur_hov', None)
        at highlight_hov(cur_hov, hov_id)
    textbutton b['btext']:
        xpos b['xp']
        if b['dir'] == 'up':
            ypos 0.15 - room_arrow_yoffset
        else:
            ypos 0.85 + room_arrow_yoffset
        action act
        xanchor 0.5
        yanchor 0.5
        text_style 'fancy_font'
        hovered SetVariable('cur_hov', hov_id)
        unhovered SetVariable('cur_hov', None)
        at highlight_hov(cur_hov, hov_id)

# basically a layered button, but doesn't render if button has no task
# unless the button has an idle label to call
screen btn_tsk(b, hov_id=None):
    if b['curtask'] or not 'hidden' in b:
        imagebutton:
            xpos b['xp']
            ypos b['yp']
            if b['curtask']:
                # if persistent.showspecial and Task.SPECIAL in b['curtask']['tags']:
                #     auto 'mini/task_special_%s.jpg'
                # else:
                auto b['imtask']
                if 'item_req' in b['curtask']:
                    if task_can_proceed(b['curtask']['item_req']):
                        action b['act']
                    else:
                        action SetVariable('hinttext', levelHints[b['curtask']['fail_id']])
                else:
                    action b['act']
            else:
                auto b['imidle']
                action b['act']
            if 'htext' in b and not len(b['htext']) == 0:
                if b['curtask']:
                    if Task.SPECIAL in b['curtask']['tags']:
                        hovered [SetVariable('cur_hov', hov_id), SetVariable('hinttext', fmtSpecialTask(b['htext']))]
                    else:
                        hovered [SetVariable('cur_hov', hov_id), SetVariable('hinttext', b['htext'])]
                    
                    unhovered SetVariable('cur_hov', None)
                    at highlight_hov(cur_hov, hov_id)

# layered button that holds a grabbable item
screen btn_item(b, hov_id):
    imagebutton:
        xpos b['xp']
        ypos b['yp']
        auto itemsAll[b['item']['id']]['im']
        action [SetVariable('curholder', b), If(inventoryOk(b['item']['id']), true=[Function(update_inv, useholder=True), SetVariable('hinttext', levelHints['default_idle'])], false=Show('popup_trade'))]
        hovered [SetVariable('cur_hov', hov_id), SetVariable('hinttext', fmtItemDesc(b['item']['id'], b['item']['stack']))]
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
            for b in baseButtons:
                imagebutton:
                    xalign 0.5
                    yalign b['y']
                    auto b['im']
                    hovered SetVariable('cur_hov', b['hov_id'])
                    unhovered SetVariable('cur_hov', None)
                    at highlight_hov(cur_hov, b['hov_id'])
                    action b['act']
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

screen floor_sidebar(curstate='game'):
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
                action SetVariable('mapfloor', (mapfloor + 1) % levelInfo[curlevel]['nfloors'])
            else:
                action act1 + [SetVariable('curfloor', curfloor+1)] + act2
            hovered SetVariable('cur_hov', 'floor_up_btn')
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
                action SetVariable('mapfloor', (mapfloor + levelInfo[curlevel]['nfloors'] - 1) % levelInfo[curlevel]['nfloors'])
            else:
                action act1 + [SetVariable('curfloor', curfloor-1)] + act2
            hovered SetVariable('cur_hov', 'floor_down_btn')
            unhovered SetVariable('cur_hov', None)
            at highlight_hov(cur_hov, 'floor_down_btn'), rot(180)

screen mc_hintbox:
    add 'mc 1a s':
        zoom 1.05
        xalign 1.07
        yalign 0.
        matrixcolor TintMatrix('#000000') * OpacityMatrix(0.5)
    add 'mc 1a s':
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

screen mini_screen:
    modal True

    window:
        xalign 0
        yalign 0
        background getMiniMap(curlevel, curroom, curfloor)

    if curroom == 'main':
        use mini_sidebar
        for bn, b in roomButtons[curlevel].items():
            if b['floor'] == curfloor:
                use btn_room(b, bn)
    else:
        use mini_sidebar('inroom')
        for bn, b in taskButtons[curlevel].items():
            if curroom == b['room']:
                use btn_tsk(b, bn)
        for hn, h in itemHolders[curlevel].items():
            if curroom == h['room']:
                use btn_item(h, hn)
        if curroom in roomArrows[curlevel]:
            for a in roomArrows[curlevel][curroom]:
                use btn_roomarrow(a, f"to_{a['toroom']}_btn")
    
    use floor_sidebar('game')
    use mc_hintbox

label mini_main():
    # TODO maybe hide quickmenu? if its too obtrusive
    scene bg minigame

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

        if was_from_roomchange():
            # don't use get_screen to check if screen is open
            # b/c call screen gets weird when there's no return statement
            show screen mini_screen
            hide screen mini_screen with cfade

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
        for bn, b in roomButtons[curlevel].items():
            b['btext'] = b['name']
        for bn, b in taskButtons[curlevel].items():
            b['curtask'] = None
            if 'hidden' in b:
                b['act'] = []
            else:
                if 'taskless' in b:
                    b['act'] = SetVariable('hinttext', levelHints[b['taskless']])
                else:
                    b['act'] = SetVariable('hinttext', levelHints['default_taskless'])
            imname = b['imtask']
            b['imtask'] = f'mini/btn_task/btn_{imname}_task_%s.jpg'
            b['imidle'] = f'mini/btn_task/btn_{imname}_%s.jpg'
        for hn, h in itemHolders[curlevel].items():
            if not 'stack' in h['item']:
                h['item']['stack'] = 1
        for tn, t in tasks[curlevel].items():
            t['activated'] = False
            t['done'] = False
            t['room'] = taskButtons[curlevel][t['btn']]['room']
        for r, ra in roomArrows[curlevel].items():
            fromroom = r
            for a in ra:
                i1 = roomButtons[curlevel][fromroom]['num']
                i2 = roomButtons[curlevel][a['toroom']]['num']
                tcost = roomProxim[curlevel][curfloor][i1][i2]
                aname = roomButtons[curlevel][a['toroom']]['name']
                a['btext'] = f'{aname}({tcost})'
                a['tcost'] = tcost
    jump mini_main
