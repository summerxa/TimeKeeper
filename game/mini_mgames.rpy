init python:
    def items_dragged(drags, drop):
        dragnum = int(drags[0].drag_name)
        if not drop:
            store.mgame_try[dragnum] = ''
        else:
            store.mgame_try[dragnum] = drop.drag_name
        store.taskGames[store.curlevel][store.curtask['name']]['drag'][dragnum]['xp'] = drags[0].x
        store.taskGames[store.curlevel][store.curtask['name']]['drag'][dragnum]['yp'] = drags[0].y
    
    def process_dishes(drags, drop):
        dragnum = int(drags[0].drag_name)
        store.taskGames[store.curlevel][store.curtask['name']]['drag'][dragnum]['xp'] = drags[0].x
        store.taskGames[store.curlevel][store.curtask['name']]['drag'][dragnum]['yp'] = drags[0].y
        if drop and not store.mgame_try[dragnum]:
            store.mgame_try[dragnum] = 1
            return 'refresh'
        return 'none'

    def dragged_grabdishes(drags, drop):
        ret = process_dishes(drags, drop)
        if ret == 'refresh':
            update_inv(otheritem='dirtydishes', otherstack=1)
            return ret
    
    def dragged_dropdishes(drags, drop):
        ret = process_dishes(drags, drop)
        if ret == 'refresh':
            update_inv(myitem='dirtydishes', mystack=1)
            return ret

    # why doesnt setvariable work on lists :skull:
    def toggle_mgame_try(i):
        store.mgame_try[i] = not store.mgame_try[i]
    
    def is_win_listeq():
        for i in range(len(store.mgame_try)):
            if store.mgame_try[i] != store.mgame_goal[i]:
                return False
        return True

    def is_win_count(tocount):
        return store.mgame_try.count(tocount) == store.mgame_goal

screen mgame_hint(tcost):
    imagebutton:
        auto 'mini/icon_map_mc_%s.png'
        xalign 1.
        yalign 0.
        action Show('popup_mgame_hint', tcost=tcost)

screen mgame_hinttext(tx):
    if showhint:
        vbox:
            xpos 0.3
            ypos 0.1
            text tx

screen mgame_exit(gametype, tfull):
    use mini_sidebar('mgame', gametype, tfull)

screen mgame_dragdrop(tgame, tfull):
    draggroup:
        # drop
        for d in tgame['drop']:
            drag:
                drag_name d['n']
                xpos d['xp']
                ypos d['yp']
                draggable False
                droppable True
                child d['im']
        
        # drag
        for d in tgame['drag']:
            drag:
                drag_name d['n']
                xpos d['xp']
                ypos d['yp']
                draggable True
                droppable False
                dragged items_dragged
                drag_raise True
                child d['im']
    
    # use mgame_hint(tgame['hint'][0])
    # use mgame_hinttext(tgame['hint'][1])
    use mgame_exit(tgame['type'], tfull)

screen mgame_dragdrop_dishes(tgame, tfull):
    draggroup:
        # drop
        for d in tgame['drop']:
            drag:
                drag_name d['n']
                xpos d['xp']
                ypos d['yp']
                draggable False
                droppable True
                child d['im']
        
        # drag
        for d in tgame['drag']:
            if not mgame_try[int(d['n'])]:
                drag:
                    drag_name d['n']
                    xpos d['xp']
                    ypos d['yp']
                    draggable True
                    droppable False
                    if tgame['type'] == 'grabdishes':
                        dragged dragged_grabdishes
                    else:
                        dragged dragged_dropdishes
                    drag_raise True
                    child d['im']
    
    # use mgame_hint(tgame['hint'][0])
    # use mgame_hinttext(tgame['hint'][1])
    use mgame_exit(tgame['type'], tfull)

screen mgame_toggle(tgame, tfull):
    for i in range(len(tgame['goal'])):
        if mgame_try[i]:
            $ tx = 'on'
        else:
            $ tx = 'off'
        imagebutton:
            xpos tgame['xp'][i]
            ypos tgame['yp'][i]
            xanchor 0.5
            yanchor 0.5
            auto tgame[tx][i]
            action Function(toggle_mgame_try, i)

    # use mgame_hint(tgame['hint'][0])
    # use mgame_hinttext(tgame['hint'][1])
    use mgame_exit(tgame['type'], tfull)
