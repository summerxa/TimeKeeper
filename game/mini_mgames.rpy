init python:
    def is_win_listeq():
        for i in range(len(store.mgame_try)):
            if store.mgame_try[i] != store.mgame_goal[i]:
                return False
        return True

    def is_win_count(tocount):
        return store.mgame_try.count(tocount) == store.mgame_goal


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

    def waterpour_init():
        i = 0
        for c in curgame['cups']:
            c['colors'] = curgame['original'][i].copy()
            i += 1

    def waterpour_act(sel, dest):
        color = store.curgame['cups'][sel]['colors'].pop()
        store.curgame['cups'][dest]['colors'].append(color)
        return waterpour_ok(curgame['cups'])

    def laundry_ok():
        global mgame_try
        global curgame
        if -1 in mgame_try:
            return False
        if -1 in curgame['starts'] or not 0 in curgame['starts'] or not 1 in curgame['starts'] or not 2 in curgame['starts']:
            return False
        for i in range(3):
            for j in range(len(mgame_try)):
                if mgame_try[j] == i and curgame['drag'][j]['type'] != curgame['starts'][i]:
                    return False
        return True

    def laundry_act_drag(drags, drop):
        dragnum = int(drags[0].drag_name)
        store.curgame['drag'][dragnum]['p'] = (drags[0].x, drags[0].y)
        if not drop:
            store.mgame_try[dragnum] = -1
        else:
            store.mgame_try[dragnum] = int(drop.drag_name)
        return 'done' if laundry_ok() else 'refresh'

    def laundry_act_start(i, t):
        curgame['starts'][i] = curgame['time_to_weight'][t]
        return 'done' if laundry_ok() else 'refresh'

screen mgame_overlay(shaded=True, has_mc=True):
    use mini_overlay('mgame', curgame['type'], shaded, has_mc)

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
        add 'mini/tgame/grab_dropdishes/plate_clean.png':
            pos (778, 618)
            anchor (0.5,0.5)
    
    if curgame['type'] == 'grabdishes':
        use mgame_overlay(shaded=shaded)

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
                    child 'mini/tgame/grab_dropdishes/plate_dirty.png'
    
    if curgame['type'] == 'dropdishes':
        use mgame_overlay(shaded=shaded)
        
        add 'mini/tgame/grab_dropdishes/dropdishes_faucet.png':
            pos (678, 413)
            xanchor 0.5 yanchor 0.5

screen mgame_toggle(shaded=True):
    for i in range(len(curgame['goal'])):
        imagebutton:
            pos curgame['p'][i]
            xanchor 0.5
            yanchor 0.5
            auto (curgame['on' if mgame_try[i] else 'off'][i])
            action Function(toggle_act, i)
            
    use mgame_overlay(shaded=shaded)

screen mgame_waterpour(shaded=True):
    default sel = -1
    default yp = 0.513
    default xplist = [0.24, 0.38, 0.52, 0.66]

    for i, c in enumerate(curgame['cups']):
        if sel != i:
            add 'mini/tgame/waterpour/waterpour_reflection.png':
                xpos xplist[i]
                ypos yp + 0.22
                xanchor 0.5 yanchor 0.5
        imagebutton:
            xpos xplist[i]
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
                xpos xplist[i]
                ypos yp - (0.1 if sel == i else 0.)
                xanchor 0.5 yanchor 0.5
                at tint(curcolor)
        add 'mini/tgame/waterpour/waterpour_highlights.png':
            xpos xplist[i]
            ypos yp - (0.1 if sel == i else 0.)
            xanchor 0.5 yanchor 0.5
    textbutton "{b}RESET{/b}":
        action If(persistent.showresetwarning, true=[Show('popup_mgame_reset')], false=[Return('reset'), With(cfade)])
        pos (320, 865)
        anchor (0.5, 0.5)
        text_style 'fancy_font'
        text_size 40
        hovered SetVariable('cur_hov', 'waterpour_reset')
        unhovered SetVariable('cur_hov', None)
        at highlight_hov(cur_hov, 'waterpour_reset')
    
    use mgame_overlay(shaded=shaded)

screen mgame_laundry_start(i, p_):
    dismiss action Hide('mgame_laundry_start')

    frame:
        anchor (0.5,0.5)
        pos (p_[0], p_[1] + 175)
        vbox:
            label "Select Time:"
            for j in range(3):
                textbutton (f"> {curgame['times'][j]} MINUTES <" if (curgame['time_to_weight'][curgame['times'][j]] == curgame['starts'][i]) else f"{curgame['times'][j]} MINUTES"):
                    action [Function(laundry_act_start, i=i, t=curgame['times'][j]), Hide('mgame_laundry_start')]

screen mgame_laundry(shaded=True):

    for i, p_ in enumerate([[435, 180], [995, 293], [1660, 430]]):
        imagebutton:
            anchor (0.5,0.5)
            pos (p_[0], p_[1])
            auto f'mini/tgame/laundry/start{(2-i)+1}_%s.png'
            action If(
                renpy.get_screen('mgame_laundry_start'),
                true=Hide('mgame_laundry_start'),
                false=Show('mgame_laundry_start', i=i, p_=p_)
            )
            hovered SetVariable('cur_hov', f'laundrystart{i}')
            unhovered SetVariable('cur_hov', None)
            at highlight_hov(cur_hov, f'laundrystart{i}')
    
    draggroup:
        # drop
        for i, p_ in enumerate([[285, 500], [785, 595], [1330, 710]]):
            drag:
                drag_name f"{i}"
                anchor (0.5,0.5)
                pos p_
                draggable False
                droppable True
                add 'mini/mini_rect.png':
                    align (0.5,0.5)
                    xysize(200, 200)
                    at opac(0.0)
        
        # drag
        for d in curgame['drag']:
            drag:
                drag_name f"{d['n']}"
                pos d['p']
                anchor (0.,0.)
                draggable True
                droppable False
                dragged laundry_act_drag
                drag_raise True
                add f"mini/tgame/laundry/laundry_{d['type']}_{d['type_sub']}.png"

    use mgame_overlay(shaded=shaded, has_mc=False)
