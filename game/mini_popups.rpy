screen popup_button_close(xp, yp, screenname):
    imagebutton:
        auto 'mini/icon_map_mc_%s.png'
        xalign 1.
        yalign 0.
        action Hide(screenname)
        hovered SetVariable('cur_hov', 'popup_close_btn')
        unhovered SetVariable('cur_hov', None)
        at highlight_hov(cur_hov, 'popup_close_btn')

screen popup_notes:
    modal True
    zorder 200
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
                            hovered SetVariable('cur_hov', f'{tab[1]}_tab')
                            unhovered SetVariable('cur_hov', None)
                            at highlight_hov(cur_hov, f'{tab[1]}_tab')
                hbox:
                    xalign 1.
                    yalign 0.
                    use popup_button_close(1., 0., 'popup_notes')

            viewport:
                area (50, 75, 900, 500)

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
    zorder 200
    add 'gui/overlay/confirm.png'

    style_prefix "confirm"

    default ltext = f"Left hand:\n{fmtItemName(invitems[0], invstacks[0])}"
    default rtext = f"Right hand:\n{fmtItemName(invitems[1], invstacks[1])}"

    frame:
        xalign 0.5
        yalign 0.5
        maximum (800, 500)

        label "On-hand"

        hbox:
            xalign 0.5
            yalign 0.6
            spacing 100
            text ltext:
                xalign 0.
                textalign 0.5
            text rtext:
                xalign 1.
                textalign 0.5
    
        use popup_button_close(1., 0., 'popup_onhand')

screen popup_trade:
    modal True
    zorder 200
    add 'gui/overlay/confirm.png'

    style_prefix "confirm"

    default drop_vb = ('drop' if curholder['item']['id'] == 'air' else 'swap')
    default ltext = f"Left hand:\n{fmtItemName(invitems[0], invstacks[0])}"
    default rtext = f"Right hand:\n{fmtItemName(invitems[1], invstacks[1])}"

    frame:
        xalign 0.5
        yalign 0.5
        maximum (800, 550)

        vbox:
            xalign 0.5 yalign 0.5

            text f'Both hands are full. Which item would you like to {drop_vb}?':
                textalign 0.5

            hbox:
                xalign 0.5
                ypos 0.85 yanchor 0.5
                spacing 100

                textbutton ltext:
                    xpos 0.2
                    yalign 0.6
                    xanchor 0.5
                    action [Hide('popup_trade'), SetVariable('curhand', 0), Function(update_inv, useholder=True), SetVariable('hinttext', levelHints['default_idle'])]

                textbutton rtext:
                    xpos 0.7
                    yalign 0.6
                    xanchor 0.5
                    action [Hide('popup_trade'), SetVariable('curhand', 1), Function(update_inv, useholder=True), SetVariable('hinttext', levelHints['default_idle'])]
    
        use popup_button_close(1., 0., 'popup_trade')

screen popup_help(curstate='main'):
    modal True
    zorder 200
    add 'gui/overlay/confirm.png'

    style_prefix "confirm"

    frame:
        xalign 0.5
        yalign 0.5
        maximum (800, 500)

        label "Help"

        text '[curstate]':
            xalign 0.5
            yalign 0.5

        use popup_button_close(1., 0., 'popup_help')

screen popup_mgame_leave:
    modal True
    zorder 200
    add 'gui/overlay/confirm.png'

    style_prefix "confirm"

    default close_leave = [Hide('popup_mgame_leave')]

    frame:
        xalign 0.5
        yalign 0.5
        maximum (800, 500)
        vbox:
            text f"Do you want to leave?\n\nLeaving will cost:\n{curtask['tcost']} minutes if the task is complete.\n{curtask['tcost'] // 2} minutes if the task is incomplete.":
                xalign 0.5
                yalign 0.2
            textbutton "Don't show this message again.":
                xalign 0.5 ypos 0.7 yanchor 0.5
                text_align 0.5
                action ToggleVariable('persistent.showleavewarning')
                if persistent.showleavewarning:
                    text_color '#aaa'
                else:
                    text_color '#fff'
            
            hbox:
                xalign 0.5
                ypos 0.85 yanchor 0.5
                spacing 150
                textbutton "Yes":
                    text_align 0.5
                    action close_leave + [SetVariable('hinttext', levelHints['default_idle']), Return('leave'), With(cfade)]
                textbutton "No":
                    text_align 0.5
                    action close_leave

# TODO fix the alignment and change btn_tx to textbutton... if this screen is actually needed, LOL
# screen popup_mgame_hint(tcost):
#     modal True
#     zorder 200
#     add 'gui/overlay/confirm.png'

#     style_prefix "confirm"

#     frame:
#         xalign 0.5
#         yalign 0.5
#         maximum(500, 300)
#         $ close_leave = [Hide('popup_mgame_hint')]
#         if showhint:
#             text 'No more hints available.':
#                 xalign 0.5
#                 yalign 0.3
#             use btn_tx({
#                 'xp': 0.5,
#                 'yp': 0.7,
#                 'btext': 'Close',
#                 'act': close_leave,
#             })
#         else:
#             text 'Do you want a hint?\nHint will cost [tcost] minute(s).':
#                 xalign 0.5
#                 yalign 0.3
#             use btn_tx({
#                 'xp': 0.4,
#                 'yp': 0.7,
#                 'btext': 'Yes',
#                 'act': close_leave + [SetVariable('curtime', curtime+tcost), SetVariable('showhint', True)]
#             })
#             use btn_tx({
#                 'xp': 0.6,
#                 'yp': 0.7,
#                 'btext': 'No',
#                 'act': close_leave
#             })

screen tx_room(bt, b_id):
    default cords = roomRects[curlevel][bt['floor']][b_id]
    default xp = (cords[2] + cords[0]) // 2
    default yp = (cords[3] + cords[1]) // 2
    default tx = bt['btext'] + ('\n(YOU ARE HERE)' if (curroom == b_id or prevroom == b_id) else '')
    text tx:
        xpos xp
        ypos yp
        xanchor 0.5 yanchor 0.5
        style 'fancy_font'
        textalign 0.5
        size 60

# doesn't follow the same code as the other popups but idk where else to put this lol
screen popup_map:
    modal True

    default mapfloor = curfloor

    add "bg mgame_main":
        xalign 0.5 yalign 0.5
    
    use mini_mapbase(mapfloor)
    
    use mini_sidebar('map')
    use floor_sidebar('map', mapfloor)

    text '(Currently viewing map, rooms are not interactable)':
        xalign 0.5
        ypos 45 yanchor 0.5
        textalign 0.5
        style 'fancy_font'
        size 50

    for bn, bt in roomButtons[curlevel].items():
        if bt['floor'] != mapfloor:
            continue
        use tx_room(bt, bn)
