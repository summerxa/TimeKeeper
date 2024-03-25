init python:
    def items_dragged(drags, drop):
        dragnum = int(drags[0].drag_name)
        store.curgame['drag'][dragnum]['xp'] = drags[0].x
        store.curgame['drag'][dragnum]['yp'] = drags[0].y
        if not drop:
            store.mgame_try[dragnum] = ''
        else:
            store.mgame_try[dragnum] = drop.drag_name
    
    def process_dishes(drags, drop):
        dragnum = int(drags[0].drag_name)
        store.curgame['drag'][dragnum]['xp'] = drags[0].x
        store.curgame['drag'][dragnum]['yp'] = drags[0].y
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

screen mgame_dragdrop(tfull):
    draggroup:
        # drop
        for d in curgame['drop']:
            drag:
                drag_name d['n']
                xpos d['xp']
                ypos d['yp']
                draggable False
                droppable True
                child d['im']
        
        # drag
        for d in curgame['drag']:
            drag:
                drag_name d['n']
                xpos d['xp']
                ypos d['yp']
                draggable True
                droppable False
                dragged items_dragged
                drag_raise True
                child d['im']
    
    use mgame_exit(curgame['type'], tfull)

screen mgame_dragdrop_dishes(tfull):
    draggroup:
        # drop
        for d in curgame['drop']:
            drag:
                drag_name d['n']
                xpos d['xp']
                ypos d['yp']
                draggable False
                droppable True
                child d['im']
        
        # drag
        for d in curgame['drag']:
            if not mgame_try[int(d['n'])]:
                drag:
                    drag_name d['n']
                    xpos d['xp']
                    ypos d['yp']
                    draggable True
                    droppable False
                    if curgame['type'] == 'grabdishes':
                        dragged dragged_grabdishes
                    else:
                        dragged dragged_dropdishes
                    drag_raise True
                    child d['im']
    
    use mgame_exit(curgame['type'], tfull)

screen mgame_toggle(curgame, tfull):
    for i in range(len(curgame['goal'])):
        if mgame_try[i]:
            $ tx = 'on'
        else:
            $ tx = 'off'
        imagebutton:
            xpos curgame['xp'][i]
            ypos curgame['yp'][i]
            xanchor 0.5
            yanchor 0.5
            auto curgame[tx][i]
            action Function(toggle_mgame_try, i)

    use mgame_exit(curgame['type'], tfull)
