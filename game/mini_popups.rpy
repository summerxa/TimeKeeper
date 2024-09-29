screen popup_button_close(screenname):
    textbutton 'X':
        text_color gui.hover_color
        text_size 60
        align (1.,0.)
        if isTutorial:
            if tutorialText[tutStep]['btn'] == 'popup_button_close':
                action [Function(progressTutorial), Hide(screenname)]
            else:
                action NullAction()
        else:
            action Hide(screenname)
        hovered SetVariable('cur_hov', 'popup_close_btn')
        unhovered SetVariable('cur_hov', None)
        at highlight_hov(cur_hov, 'popup_close_btn')
        activate_sound audio.button_click_sfx

screen popup_button_info(info_name, info_title):
    imagebutton:
        auto 'mini/ui/icon_popup_info_%s.png'
        align (0.,1.)
        if isTutorial:
            if tutorialText[tutStep]['btn'] == 'popup_button_info':
                action [Function(progressTutorial), Show('popup_info', info_name=info_name, info_title=info_title)]
            else:
                action NullAction()
        else:
            action Show('popup_info', info_name=info_name, info_title=info_title)
        hovered SetVariable('cur_hov', 'popup_info_btn')
        unhovered SetVariable('cur_hov', None)
        at highlight_hov(cur_hov, 'popup_info_btn')

screen popup_info(info_name, info_title):
    modal True
    zorder 210
    add 'gui/overlay/confirm.png'
    
    style_prefix "confirm"

    frame:
        xalign 0.5
        yalign 0.5
        maximum (800, 600)

        label f"◆ {info_title} ◆":
            text_color gui.hover_color
            text_size 50
            xalign 0.5

        viewport:
            area (10, 85, 900, 400)
            
            mousewheel True
            draggable True
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            
            vbox:
                spacing 10
                for t_ in infoText[info_name]:
                    if t_[0] == ">":
                        text t_[1:]:
                            size 25
                            xanchor 0.
                            xpos 0.05
                    else:
                        text t_:
                            size 25
                            xalign 0.
        
        textbutton 'X':
            text_color gui.hover_color
            text_size 60
            align (1.,0.)
            if isTutorial:
                if tutorialText[tutStep]['btn'] == 'popup_button_close':
                    action [Function(progressTutorial), Hide('popup_info')]
                else:
                    action NullAction()
            else:
                action Hide('popup_info')
            hovered SetVariable('cur_hov', 'popup_close_btn_2')
            unhovered SetVariable('cur_hov', None)
            at highlight_hov(cur_hov, 'popup_close_btn_2')
            activate_sound audio.button_click_sfx

screen task_display(t, t_part=None, t_blocked=False, is_bonus=False):
    vbox:
        anchor(0., 0.5) pos(0.05, 0.5)
        xmaximum 520
        hbox:
            xminimum 520
            text f"{t['title']}":
                xalign 0.
                yalign 0.5
                style 'tasks_font'
                bold True
                kerning -1.5
            hbox:
                xalign 1.
                for idx, txt in [[0, 'cleanliness'], [1, 'coverage'], [2, 'service']]:
                    add 'mini/ui/[txt]Icon.png':
                        yalign 0.5
                    text f"{t['attributes'][idx]}":
                        yalign 0.5
                        style 'tasks_font'
                        bold True
        if t['tasktype'] == 'fetchquest' or t['tasktype'] == 'fetchquest_end':
            text f"Location: {roomButtons[curlevel][taskButtons[curlevel][t['btn']]['room']]['name']}":
                style 'tasks_font'
        else:
            if is_bonus:
                text f"Location: {roomButtons[curlevel][taskButtons[curlevel][bonusq[t['tasktype']]['btn']]['room']]['name']}":
                    style 'tasks_font'
            else:
                text f"Location: {roomButtons[curlevel][taskButtons[curlevel][taskq[t['tasktype']]['btn']]['room']]['name']}":
                    style 'tasks_font'
        if t_part:
            text f"Time: {t_part['tcost']}m":
                style 'tasks_font'
        else:
            text f"Time: {t['tcost']}m":
                style 'tasks_font'
        text f"{t['desc']}":
            style 'tasks_font'
        if t_blocked:
            text "{i}Must complete previous guest request to unlock this task{/i}":
                style 'tasks_font'

screen popup_notes():
    modal True
    zorder 200
    add 'gui/overlay/confirm.png'
    
    style_prefix "confirm"

    default notes_tab = 'tasks'

    frame:
        xalign 0.5
        yalign 0.5
        maximum (1517, 1001)
        background 'mini/ui/notebook.png'
        padding(75,20,20,60)

        hbox:
            spacing 23
            align (0.5,0.)
            xminimum 1367
            vbox:
                spacing 23
                xmaximum 650
                text f"◆ Tasks ◆":
                    style 'fancy_font'
                    size 50
                    xalign 0.5

                viewport:
                    area (0, 20, 600, 750)
                    
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    vscrollbar_unscrollable "hide"

                    vbox:
                        spacing 23

                        text levelInfo[curlevel]['task_popup_text']:
                            size 30
                            color '#906548'

                        text "{b}Priority Tasks{/b}":
                            size 30
                            color '#906548'

                        add 'mini/mini_rect.png':
                            yalign 0.5
                            xysize(600, 5)
                            matrixcolor TintMatrix('#906548')

                        if fetchq:
                            vbox:
                                spacing 23
                                for fq in fetchq:
                                    use task_display(tasks[curlevel]['single'][fq], t_blocked = (fq != fetchq[0]))
                        else:
                            text "None right now.":
                                size 30
                                anchor(0., 0.5) pos(0.05, 0.5)
                                color '#906548'
            
            vbox:
                text f"◆ Tasks ◆":
                    style 'fancy_font'
                    size 50
                    xalign 0.5
                
                text "{b}Other Tasks{/b}":
                    size 30
                    color '#906548'
                
                add 'mini/mini_rect.png':
                    yalign 0.5
                    xysize(550, 5)
                    matrixcolor TintMatrix('#906548')

                viewport:
                    area (0, 20, 600, 735)
                    
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    vscrollbar_unscrollable "hide"
                    vbox:
                        spacing 23
                        for tn, tsk in bonusq.items():
                            if tsk['btn']:
                                use task_display(tasks[curlevel]['infinite'][tn], is_bonus=True)
                        for tn, tsk in taskq.items():
                            if 'sequence' in tasks[curlevel]['infinite'][tn]:
                                use task_display(tasks[curlevel]['infinite'][tn], taskTemplates[tsk['part']])
                            else:
                                use task_display(tasks[curlevel]['infinite'][tn])
        
        button:
            anchor (0.,0.)
            pos (1360,7)
            add 'mini/mini_rect.png':
                xysize(55,60)
            if isTutorial:
                if tutorialText[tutStep]['btn'] == 'popup_button_close':
                    action [Function(progressTutorial), Hide('popup_notes')]
                else:
                    action NullAction()
            else:
                action Hide('popup_notes')
            at opac(0.)
            activate_sound audio.button_click_sfx
        use popup_button_info('notes', 'About the Notebook')
    
    use tut_overlay()

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

        label "◆ On-hand ◆":
            xalign 0.5

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
    
        use popup_button_close('popup_onhand')
        use popup_button_info('onhand', 'About On-hand')
    use tut_overlay()

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
                xmaximum 700

                textbutton ltext:
                    align (0.,0.6)
                    text_align 0.5
                    if isTutorial:
                        action [Function(progressTutorial), Hide('popup_trade'), SetVariable('curhand', 0), Function(update_inv, useholder=True), Function(setIdle)]
                    else:
                        action [Hide('popup_trade'), SetVariable('curhand', 0), Function(update_inv, useholder=True), Function(setIdle)]
                    activate_sound audio.button_click_sfx

                textbutton rtext:
                    align(1.,0.6)
                    text_align 0.5
                    if isTutorial:
                        action [Function(progressTutorial), Hide('popup_trade'), SetVariable('curhand', 1), Function(update_inv, useholder=True), Function(setIdle)]
                    else:
                        action [Hide('popup_trade'), SetVariable('curhand', 1), Function(update_inv, useholder=True), Function(setIdle)]
                    activate_sound audio.button_click_sfx
    
        use popup_button_close('popup_trade')
        use popup_button_info('trade', 'Both hands full')
    use tut_overlay()

screen popup_help(curstate='main'):
    modal True
    zorder 200
    add 'gui/overlay/confirm.png'

    style_prefix "confirm"

    default h_tab = "main" if (curstate == 'main' or not curstate in helpText) else curstate

    frame:
        xalign 0.5
        yalign 0.5
        maximum (1000, 800)

        label "◆ Help ◆":
            text_color gui.hover_color
            xalign 0.5

        vbox:
            area (0, 80, 880, 600)
            spacing 23

            if curstate != 'main' and curstate in helpText:
                hbox:
                    spacing 23

                    textbutton "Minigame rules":
                        action SetScreenVariable("h_tab", curstate)
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

                vbox:
                    xmaximum 800
                    for t_ in helpText[h_tab]:
                        if t_[0] == ">":
                            text t_[1:]:
                                size 25
                                xanchor 0.
                                xpos 0.05
                        else:
                            text t_:
                                size 25
                                xalign 0.
        
        use popup_button_close('popup_help')
    use tut_overlay()

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
            text f"Do you want to leave?\n\nLeaving will cost:\n{getTcost()} minutes if the task is complete.\n{getTcost() // 2} minutes if the task is incomplete.":
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
                    action close_leave + [Function(setIdle), Return('leave'), With(cfade)]
                    activate_sound audio.button_click_sfx
                textbutton "No":
                    text_align 0.5
                    action close_leave
                    activate_sound audio.button_click_sfx

screen popup_mgame_reset():
    modal True
    zorder 200
    add 'gui/overlay/confirm.png'

    style_prefix "confirm"

    default close_leave = [Hide('popup_mgame_reset')]

    frame:
        xalign 0.5
        yalign 0.5
        maximum (800, 500)
        vbox:
            text f"Do you want to reset the minigame?\nThis cannot be undone.":
                xalign 0.5
                yalign 0.2
            textbutton "Don't show this message again.":
                xalign 0.5 ypos 0.7 yanchor 0.5
                text_align 0.5
                action ToggleVariable('persistent.showresetwarning')
                if persistent.showresetwarning:
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
                    action close_leave + [Function(setIdle), Return('reset'), With(cfade)]
                    activate_sound audio.button_click_sfx
                textbutton "No":
                    text_align 0.5
                    action close_leave
                    activate_sound audio.button_click_sfx

screen tx_room(bt, b_id):
    default cords = roomRects[curlevel][bt['floor']][b_id]
    default xp = (cords[2] + cords[0]) // 2
    default yp = (cords[3] + cords[1]) // 2
    default tx = get_room_text(b_id, True)
    text tx:
        xpos xp
        ypos yp
        xanchor 0.5 yanchor 0.5
        style 'fancy_font'
        textalign 0.5
        size 50

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
        size 30

    for bn, bt in roomButtons[curlevel].items():
        if bt['floor'] != mapfloor:
            continue
        use tx_room(bt, bn)
    use tut_overlay()