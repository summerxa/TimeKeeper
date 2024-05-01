screen popup_button_close(xp, yp, screenname):
    imagebutton:
        auto 'mini/icon_map_mc_%s.png'
        xalign 1.
        yalign 0.
        action Hide(screenname)
        hovered SetVariable('cur_hov', 'popup_close_btn')
        unhovered SetVariable('cur_hov', None)
        at highlight_hov(cur_hov, 'popup_close_btn')
        activate_sound audio.button_click_sfx

screen popup_notes():
    modal True
    zorder 200
    add 'gui/overlay/confirm.png'
    
    style_prefix "confirm"

    default notes_tab = 'tasks'
    default tx = notes_text_s if persistent.showspecial else notes_text

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
                            action [
                                SetScreenVariable('notes_tab', tab[1]),
                                If(
                                    (tab[1] == 'tasks'),
                                    true=SetScreenVariable('tx', notes_text_s if persistent.showspecial else notes_text),
                                    false=SetScreenVariable('tx', levelInfo[curlevel][tab[1]] if tab[1] in levelInfo[curlevel] else "This is an error message :(")
                                )
                            ]
                            auto tab[2]
                            hovered SetVariable('cur_hov', f'{tab[1]}_tab')
                            unhovered SetVariable('cur_hov', None)
                            at highlight_hov(cur_hov, f'{tab[1]}_tab')
                            activate_sound audio.button_click_sfx
                hbox:
                    xalign 1.
                    yalign 0.
                    use popup_button_close(1., 0., 'popup_notes')

            viewport:
                area (50, 75, 900, 500)
                
                mousewheel True
                draggable True
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"
                text tx

screen popup_onhand():
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

screen popup_trade():
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
                    activate_sound audio.button_click_sfx

                textbutton rtext:
                    xpos 0.7
                    yalign 0.6
                    xanchor 0.5
                    action [Hide('popup_trade'), SetVariable('curhand', 1), Function(update_inv, useholder=True), SetVariable('hinttext', levelHints['default_idle'])]
                    activate_sound audio.button_click_sfx
    
        use popup_button_close(1., 0., 'popup_trade')

screen popup_help(curstate='main'):
    modal True
    zorder 200
    add 'gui/overlay/confirm.png'

    style_prefix "confirm"

    default h_tab = "main" if (curstate == 'main' or not curstate in levelHelp) else 'rules'

    frame:
        xalign 0.5
        yalign 0.5
        maximum (1000, 800)

        label "Help"

        vbox:
            area (0, 60, 880, 600)
            spacing 23

            if curstate != 'main' and curstate in levelHelp:
                hbox:
                    spacing 23

                    textbutton "Minigame rules":
                        action SetScreenVariable("h_tab", "rules")
                        activate_sound audio.button_click_sfx
                        xalign 0.

                    textbutton "Main gameplay":
                        action SetScreenVariable("h_tab", "main")
                        activate_sound audio.button_click_sfx
                        xalign 1.

            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"

                if h_tab == 'main':
                    text levelHelp['main']
                else:
                    text levelHelp[curstate]
        
        use popup_button_close(1., 0., 'popup_help')

screen popup_mgame_leave():
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
                    text_color gui.idle_color
                else:
                    text_color gui.selected_color
                activate_sound audio.button_click_sfx
            
            hbox:
                xalign 0.5
                ypos 0.85 yanchor 0.5
                spacing 150
                textbutton "Yes":
                    text_align 0.5
                    action close_leave + [SetVariable('hinttext', levelHints['default_idle']), Return('leave'), With(cfade)]
                    activate_sound audio.button_click_sfx
                textbutton "No":
                    text_align 0.5
                    action close_leave
                    activate_sound audio.button_click_sfx

screen tx_room(bt, b_id):
    default cords = roomRects[curlevel][bt['floor']][b_id]
    default xp = (cords[2] + cords[0]) // 2
    default yp = (cords[3] + cords[1]) // 2
    default tx = bt['name'].upper() + ('\n{size=-20}* YOU ARE HERE{/size}' if (curroom == b_id or prevroom == b_id) else '')
    text tx:
        xpos xp
        ypos yp
        xanchor 0.5 yanchor 0.5
        style 'fancy_font'
        textalign 0.5
        size 60

# doesn't follow the same code as the other popups but idk where else to put this lol
screen popup_map():
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
