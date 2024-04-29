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
            update_inv(otheritem='dish_dirty', otherstack=1)
            return ret
    
    def dragged_dropdishes(drags, drop):
        ret = process_dishes(drags, drop)
        if ret == 'refresh':
            update_inv(myitem='dish_dirty', mystack=1)
            return ret
    
    def waterpour_act(sel, dest):
        color = store.curgame['cups'][sel]['colors'].pop()
        store.curgame['cups'][dest]['colors'].append(color)

    def is_win_listeq():
        for i in range(len(store.mgame_try)):
            if store.mgame_try[i] != store.mgame_goal[i]:
                return False
        return True

    def is_win_count(tocount):
        return store.mgame_try.count(tocount) == store.mgame_goal

screen mgame_dragdrop():
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
    
    use mini_sidebar('mgame', curgame['type'])

screen mgame_dragdrop_dishes():
    if curgame['type'] == 'dropdishes' and 1 in mgame_try:
        add curgame['in_sink']['im']:
            xpos curgame['in_sink']['xp'] xanchor 0.5
            ypos curgame['in_sink']['yp'] yanchor 0.5
    
    draggroup:
        # drop
        for d in curgame['drop']:
            drag:
                drag_name d['n']
                xpos d['xp'] xanchor 0.
                ypos d['yp'] yanchor 0.
                draggable False
                droppable True
                add 'mini/mini_rect.png':
                    xysize(d['w'], d['h'])
                    at opac(0.0)
        
        # drag
        for d in curgame['drag']:
            if not mgame_try[int(d['n'])]:
                drag:
                    drag_name d['n']
                    xpos d['xp'] xanchor 0.5
                    ypos d['yp'] yanchor 0.5
                    draggable True
                    droppable False
                    if curgame['type'] == 'grabdishes':
                        dragged dragged_grabdishes
                    else:
                        dragged dragged_dropdishes
                    drag_raise True
                    child d['im']
    
    use mini_sidebar('mgame', curgame['type'])
    use mc_hintbox

screen mgame_toggle():
    for i in range(len(curgame['goal'])):
        imagebutton:
            xpos curgame['xp'][i]
            ypos curgame['yp'][i]
            xanchor 0.5
            yanchor 0.5
            auto (curgame['on' if mgame_try[i] else 'off'][i])
            action ToggleDict(mgame_try, i)

    use mini_sidebar('mgame', curgame['type'])
    use mc_hintbox

screen mgame_waterpour():
    default sel = -1
    default yp = 0.513

    for i, c in enumerate(curgame['cups']):
        if sel != i:
            add 'mini/tgame/waterpour/waterpour_reflection.png':
                xpos c['xp']
                ypos yp + 0.22
                xanchor 0.5 yanchor 0.5
        imagebutton:
            xpos c['xp']
            ypos yp - (0.1 if sel == i else 0.)
            xanchor 0.5 yanchor 0.5
            auto 'mini/tgame/waterpour/waterpour_cup_%s.png'
            action If(
                sel < 0, true=SetScreenVariable('sel', i), false=If(
                    sel == i, true=SetScreenVariable('sel', -1), false=If(
                        len(c['colors']) >= 4,
                        true=SetVariable('hinttext', levelHints['waterpour_cup_full']),
                        false=[
                            Function(waterpour_act, sel=sel, dest=i),
                            SetScreenVariable('sel', -1),
                            SetVariable('hinttext', levelHints['waterpour_idle'])
                        ]
                    )
                )
            )
        for j, curcolor in list(enumerate(c['colors'])):
            add f'mini/tgame/waterpour/waterpour_{j}.png':
                xpos c['xp']
                ypos yp - (0.1 if sel == i else 0.)
                xanchor 0.5 yanchor 0.5
                at tint(curcolor)
        add 'mini/tgame/waterpour/waterpour_highlights.png':
            xpos c['xp']
            ypos yp - (0.1 if sel == i else 0.)
            xanchor 0.5 yanchor 0.5
    
    use mini_sidebar('mgame', curgame['type'])
    use mc_hintbox
