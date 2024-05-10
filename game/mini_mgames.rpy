init python:
    def toggle_act(i):
        store.mgame_try[i] = not store.mgame_try[i]
        return 'done' if is_win_listeq() else 'refresh'

    def items_dragged(drags, drop):
        dragnum = int(drags[0].drag_name)
        store.curgame['drag'][dragnum]['xp'] = drags[0].x
        store.curgame['drag'][dragnum]['yp'] = drags[0].y
        if not drop:
            store.mgame_try[dragnum] = ''
        else:
            store.mgame_try[dragnum] = drop.drag_name
    
    def dishes_act(drags, drop):
        dragnum = int(drags[0].drag_name)
        store.curgame['drag'][dragnum]['xp'] = drags[0].x
        store.curgame['drag'][dragnum]['yp'] = drags[0].y
        if drop and not store.mgame_try[dragnum]:
            store.mgame_try[dragnum] = 1
            return 'refresh'
        return 'none'

    def dragged_grabdishes(drags, drop):
        ret = dishes_act(drags, drop)
        if ret == 'refresh':
            update_inv(otheritem='dish_dirty', otherstack=1)
            return ret
    
    def dragged_dropdishes(drags, drop):
        ret = dishes_act(drags, drop)
        if ret == 'refresh':
            update_inv(myitem='dish_dirty', mystack=1)
            return ret
    
    def waterpour_ok(cups):
        all_colors = []
        failed = False
        for cup in cups:
            cup_colors = cup['colors']
            if not len(cup_colors):
                continue
            curcolor = cup_colors[0]
            for c in cup_colors:
                if c in all_colors or c != curcolor:
                    failed = True
                    break
            if failed or curcolor in all_colors:
                failed = True
                break
            all_colors.append(curcolor)
        return 'refresh' if failed else 'done'

    def waterpour_act(sel, dest):
        color = store.curgame['cups'][sel]['colors'].pop()
        store.curgame['cups'][dest]['colors'].append(color)
        return waterpour_ok(curgame['cups'])

    def waterpour_act1(sel, dest):
        cups = []
        for cup in curgame['cups']:
            cups.append({'colors': cup['colors'].copy()})
        color = cups[sel]['colors'].pop()
        cups[dest]['colors'].append(color)
        return waterpour_ok(cups)

    def is_win_listeq():
        for i in range(len(store.mgame_try)):
            if store.mgame_try[i] != store.mgame_goal[i]:
                return False
        return True

    def is_win_count(tocount):
        return store.mgame_try.count(tocount) == store.mgame_goal

screen mgame_overlay():
    use mini_sidebar('mgame', curgame['type'])
    use mc_hintbox

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
    
    use mgame_overlay

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
        
    if 'overlay' in curgame:
        for overlay_itm in curgame['overlay']:
            add overlay_itm['im']:
                xpos overlay_itm['xp']
                ypos overlay_itm['yp']
                xanchor 0.5 yanchor 0.5
    
    use mgame_overlay

screen mgame_toggle():
    for i in range(len(curgame['goal'])):
        imagebutton:
            xpos curgame['xp'][i]
            ypos curgame['yp'][i]
            xanchor 0.5
            yanchor 0.5
            auto (curgame['on' if mgame_try[i] else 'off'][i])
            action Function(toggle_act, i)

    use mgame_overlay

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
            activate_sound audio.waterpour_click_sfx
            if waterpour_act1(sel, i) == 'done':
                action If(
                    sel < 0, true=SetScreenVariable('sel', i), false=If(
                        sel == i, true=SetScreenVariable('sel', -1), false=If(
                            len(c['colors']) >= 4,
                            true=SetVariable('hinttext', levelHints['waterpour_cup_full']),
                            false=[
                                Function(waterpour_act, sel=sel, dest=i),
                                SetScreenVariable('sel', -1),
                                SetVariable('hinttext', levelHints['waterpour_idle']),
                                With(cfade)
                            ]
                        )
                    )
                )
            else:
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
    
    use mgame_overlay
