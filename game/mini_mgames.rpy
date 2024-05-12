init python:
    def toggle_act(i):
        store.mgame_try[i] = not store.mgame_try[i]
        return 'done' if is_win_listeq() else 'refresh'

    def items_dragged(drags, drop):
        dragnum = int(drags[0].drag_name)
        store.curgame['drag'][dragnum]['p'] = (drags[0].x, drags[0].y)
        if not drop:
            store.mgame_try[dragnum] = ''
        else:
            store.mgame_try[dragnum] = drop.drag_name
        return 'done' if is_win_listeq() else 'refresh'
    
    def dishes_act(drags, drop):
        dragnum = int(drags[0].drag_name)
        store.curgame['drag'][dragnum]['p'] = (drags[0].x, drags[0].y)
        if drop and not store.mgame_try[dragnum]:
            store.mgame_try[dragnum] = 1
            return 'done' if not 0 in store.mgame_try else 'refresh'
        return 'none'

    def dragged_grabdishes(drags, drop):
        ret = dishes_act(drags, drop)
        if ret == 'refresh' or ret == 'done':
            update_inv(otheritem='dish_dirty', otherstack=1)
            return ret
        return 'refresh'
    
    def dragged_dropdishes(drags, drop):
        ret = dishes_act(drags, drop)
        if ret == 'refresh' or ret == 'done':
            update_inv(myitem='dish_dirty', mystack=1)
            return ret
        return 'refresh'
    
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

    def is_win_listeq():
        for i in range(len(store.mgame_try)):
            if store.mgame_try[i] != store.mgame_goal[i]:
                return False
        return True

    def is_win_count(tocount):
        return store.mgame_try.count(tocount) == store.mgame_goal

screen mgame_overlay(shaded=True):
    use mini_overlay('mgame', curgame['type'], shaded)

screen mgame_dragdrop():
    draggroup:
        # drop
        for d in curgame['drop']:
            drag:
                drag_name d['n']
                pos d['p']
                draggable False
                droppable True
                child d['im']
        
        # drag
        for d in curgame['drag']:
            drag:
                drag_name d['n']
                pos d['p']
                draggable True
                droppable False
                dragged items_dragged
                drag_raise True
                child d['im']

screen mgame_dragdrop_dishes(shaded=True):
    if curgame['type'] == 'dropdishes' and 1 in mgame_try:
        add curgame['in_sink']['im']:
            pos curgame['in_sink']['p']
            anchor (0.5,0.5)
    
    draggroup:
        # drop
        for d in curgame['drop']:
            drag:
                drag_name d['n']
                pos d['p']
                anchor (0.,0.)
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
                    pos d['p']
                    anchor (0.,0.)
                    draggable True
                    droppable False
                    if curgame['type'] == 'grabdishes':
                        dragged dragged_grabdishes
                    else:
                        dragged dragged_dropdishes
                    drag_raise True
                    child d['im']
        
    use mgame_overlay(shaded=shaded)

    if 'overlay' in curgame:
        for overlay_itm in curgame['overlay']:
            add overlay_itm['im']:
                pos overlay_itm['p']
                xanchor 0.5 yanchor 0.5

screen mgame_toggle():
    for i in range(len(curgame['goal'])):
        imagebutton:
            pos curgame['p'][i]
            xanchor 0.5
            yanchor 0.5
            auto (curgame['on' if mgame_try[i] else 'off'][i])
            action Function(toggle_act, i)

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

screen mgame_dragdrop_laundry(shaded=True):
    for i in range(3):
        text f"{times[i]} MINUTES":
            font gui.label_text_font
            color '#ffffff'
            size 60
            yalign 0.1
            xalign (0.25 * (i+1))

    draggroup:
        # drop
        for i in range(3):
            drag:
                drag_name f"{i}"
                xalign (0.25 * (i+1))
                yalign 0.25
                draggable False
                droppable True
                add 'mini/mini_rect.png':
                    xysize(200, 200)
                    # at opac(0.0)
        
        # drag
        for d in curgame['drag']:
            drag:
                drag_name f"{d['n']}"
                pos d['p']
                anchor (0.,0.)
                draggable True
                droppable False
                dragged items_dragged
                drag_raise True
                add f"mini/tgame/laundry/clothes_{d['type']}.png"

    use mgame_overlay(shaded=shaded)
