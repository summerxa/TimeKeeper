screen popup_button_close(xp, yp, screenname):
    imagebutton:
        auto 'mini/icon_map_mc_%s.png'
        xalign 1.
        yalign 0.
        action Hide(screenname)

screen popup_notes:
    modal True
    zorder popup_zorder
    add 'gui/overlay/confirm.png'
    
    style_prefix "confirm"

    default notes_tab = 'tasks'

    frame:
        xalign 0.5
        yalign 0.5
        minimum (1000, 800)
        # maximum (1000, 800)
        side 't b':
            hbox:
                xminimum 1000
                hbox:
                    xalign 0.
                    yalign 0.
                    for tab in [[0., 'tasks', 'mini/icon_map_mc_%s.png'], [0.1, 'info', 'mini/icon_map_mc_%s.png']]:
                        imagebutton:
                            xpos tab[0]
                            xanchor 0.
                            yalign 0.
                            action SetScreenVariable('notes_tab', tab[1])
                            auto tab[2]
                hbox:
                    xalign 1.
                    yalign 0.
                    use popup_button_close(1., 0., 'popup_notes')

            viewport:
                area (100, 100, 800, 500)

                $ tx = ''
                if notes_tab == 'tasks':
                    if persistent.showspecial:
                        $ tx = notes_text_s
                    else:
                        $ tx = notes_text
                else:
                    $ tx = levelInfo[curlevel][notes_tab]
                
                mousewheel True
                draggable True
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"
                text tx

screen popup_onhand:
    modal True
    zorder popup_zorder
    add 'gui/overlay/confirm.png'

    style_prefix "confirm"

    frame:
        xalign 0.5
        yalign 0.5
        maximum (800, 500)

        $ ltext = fmtItem(invitems[0], invstacks[0])
        $ rtext = fmtItem(invitems[1], invstacks[1])

        text 'Left hand:\n[ltext]':
            xpos 0.2
            ypos 0.5
            xanchor 0.5
            yanchor 0.5
        text 'Right hand:\n[rtext]':
            xpos 0.7
            ypos 0.5
            xanchor 0.5
            yanchor 0.5
    
        use popup_button_close(1., 0., 'popup_onhand')

screen popup_clock:
    modal True
    zorder popup_zorder
    add 'gui/overlay/confirm.png'

    use popup_button_close(0.75, 0.25, 'popup_clock')

screen popup_help(curstate='main'):
    modal True
    zorder popup_zorder
    add 'gui/overlay/confirm.png'

    style_prefix "confirm"

    frame:
        xalign 0.5
        yalign 0.5
        maximum (800, 500)

        text '[curstate]':
            xalign 0.5
            yalign 0.5

        use popup_button_close(1., 0., 'popup_help')

screen popup_trade:
    modal True
    zorder popup_zorder
    add 'gui/overlay/confirm.png'

    style_prefix "confirm"

    frame:
        xalign 0.5
        yalign 0.5
        maximum (800, 550)

        $ drop_vb = ('drop' if curholder['item']['id'] == 'air' else 'swap')

        text f'Both hands are full. Which item would you like to {drop_vb}?':
            textalign 0.5
            xalign 0.5
            yalign 0.3

        textbutton f"Left hand:\n{fmtItem(invitems[0], invstacks[0])}":
            xpos 0.2
            yalign 0.6
            xanchor 0.5
            action [Hide('popup_trade'), SetVariable('curhand', 0), Function(update_inv, useholder=True)]

        textbutton f"Right hand:\n{fmtItem(invitems[1], invstacks[1])}":
            xpos 0.7
            yalign 0.6
            xanchor 0.5
            action [Hide('popup_trade'), SetVariable('curhand', 1), Function(update_inv, useholder=True)]
    
        use popup_button_close(1., 0., 'popup_trade')

screen popup_mgame_leave(tfull):
    modal True
    zorder popup_zorder
    add 'gui/overlay/confirm.png'

    style_prefix "confirm"

    $ thalf = tfull // 2

    frame:
        xalign 0.5
        yalign 0.5
        maximum (800, 500)
        text 'Do you want to leave?\n\nLeaving will cost:\n[tfull] minutes if the task is complete.\n[thalf] minutes if the task is incomplete.':
            xalign 0.5
            yalign 0.2
        if persistent.showleavewarning:
            use btn_tx({
                'xp': 0.5,
                'yp': 0.7,
                'btext': '{color=#aaa}Don\'t show this message again.{/color}',
                'act': ToggleVariable('persistent.showleavewarning')
            })
        else:
            use btn_tx({
                'xp': 0.5,
                'yp': 0.7,
                'btext': '{color=#fff}Don\'t show this message again.{/color}',
                'act': ToggleVariable('persistent.showleavewarning')
            })
        $ close_leave = [Hide('popup_mgame_leave')]
        use btn_tx({
            'xp': 0.4,
            'yp': 0.85,
            'btext': 'Yes',
            'act': close_leave + [Return('leave'), With(Fade(fadetime, 0.0, fadetime))]
        })
        use btn_tx({
            'xp': 0.6,
            'yp': 0.85,
            'btext': 'No',
            'act': close_leave
        })

# TODO fix the alignment... if this screen is actually needed, LOL
screen popup_mgame_hint(tcost):
    modal True
    zorder popup_zorder
    add 'gui/overlay/confirm.png'

    style_prefix "confirm"

    frame:
        xalign 0.5
        yalign 0.5
        maximum(500, 300)
        $ close_leave = [Hide('popup_mgame_hint')]
        if showhint:
            text 'No more hints available.':
                xalign 0.5
                yalign 0.3
            use btn_tx({
                'xp': 0.5,
                'yp': 0.7,
                'btext': 'Close',
                'act': close_leave,
            })
        else:
            text 'Do you want a hint?\nHint will cost [tcost] minute(s).':
                xalign 0.5
                yalign 0.3
            use btn_tx({
                'xp': 0.4,
                'yp': 0.7,
                'btext': 'Yes',
                'act': close_leave + [SetVariable('curtime', curtime+tcost), SetVariable('showhint', True)]
            })
            use btn_tx({
                'xp': 0.6,
                'yp': 0.7,
                'btext': 'No',
                'act': close_leave
            })

# doesn't follow the same code as the other popups but idk where else to put this lol
screen popup_map:
    modal True

    on "show" action SetVariable('mapfloor', curfloor)

    window:
        xalign 0
        yalign 0
        background getMiniMap(curlevel, 'main', mapfloor)
    
    use mini_sidebar('map')
    use floor_sidebar('map')

    vbox:
        xalign 0.5
        yalign 0.05
        $ mapfloor1 = mapfloor + 1
        text '{color=#000}Currently viewing map...\nFloor [mapfloor1]{/color}'

    for bn, b in roomButtons[curlevel].items():
        if b['floor'] != mapfloor:
            continue
        $ temp = '{color=#000}' + b['name'] + '{/color}'
        text temp xpos b['xp'] ypos b['yp']
        # TODO (not a todo) ^ changed text color bc otherwise its barely visible

    if curfloor == mapfloor:
        $ room = None
        if curroom != 'main':
            $ room = curroom
        elif prevroom and prevroom != 'main':
            $ room = prevroom
        if room:
            add 'mini/icon_map_mc.png':
                xpos mcIconLoc[curlevel][room][0]
                ypos mcIconLoc[curlevel][room][1]
                xanchor 0.5
                yanchor 0.5
