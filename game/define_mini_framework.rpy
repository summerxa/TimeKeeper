init python:
    def getMiniMap(lvl, room, floor):
        return f"mini/map/map_{lvl}_{room}_{floor}.png"

    # returns True if last label was a room change (gotoroom) function
    def was_from_roomchange():
        return (len(store.tolabel) >= 8 and store.tolabel[:8] == 'gotoroom')
    
    def task_can_proceed(item_req=[]):
        if not len(item_req):
            return True
        for i in item_req:
            if i in store.invitems:
                return True
        return False

    # --- TASK/TASKBUTTON FORMATTING ---

    # returns time in am/pm
    def getTimeDig(t):
        tx = ''
        if (t // 60) % 12:
            tx += str((t // 60) % 12)
        else:
            tx += '12'
        tx += ':'
        if t % 60 < 10:
            tx += '0'
        tx += str(t % 60)
        if (t // 60) % 24 < 12:
            tx += 'am'
        else:
            tx += 'pm'
        return tx

    def setTlimit(t):
        t['t0'] = store.curtime
        if ('tf' in t and t['tf'] == 9999) or ('dur' in t and t['dur'] == 9999):
            t['tf'] = store.tlimit
        else:
            if 'dur' in t:
                t['tf'] = min(t['t0'] + t['dur'], store.tlimit)

    def fmtTskButton(t):
        tx = "("
        if t['t0'] != -1:
            tx += getTimeDig(t['t0'])
        else:
            tx += getTimeDig(tstart)
        tx += '-'
        if t['tf'] != 9999:
            tx += getTimeDig(t['tf'])
        else:
            tx += getTimeDig(tlimit)
        tx += ") " + t['desc']
        return tx

    # by default, checks if special highlight is enabled in settings
    # passing forced=True forces the fn. to add special formatting regardless of settings
    def fmtSpecialTask(t, forced=False):
        if not persistent.showspecial and not forced:
            return t
        return "{color=#ebe834}" + t + "{/color}"

    def fmtBaseTask(t):
        return "- " + fmtTskButton(t) + " [[" + roomButtons[curlevel][t['room']]['name'] + "]"

    def setHtext(b):
        b['htext'] = fmtTskButton(b['curtask'])

    # sorts tasks by tf, tiebreaking by t0 and then room name
    def generateTodo():
        if len(store.taskq) == 0:
            store.notes_text = "No tasks right now."
            store.notes_text_s = store.notes_text
            return
        tqs = []
        for t in store.taskq:
            tqs.append([t['tf'], t['t0'], t['room'], fmtBaseTask(t), Task.SPECIAL in t['tags']])
        tqs.sort()
        tq = []
        tq_s = []
        for t in tqs:
            tx = t[3]
            tq.append(tx)
            if t[4]:
                tx = fmtSpecialTask(tx, True)
            tq_s.append(tx)
        store.notes_text = '\n'.join(tq)
        store.notes_text_s = '\n'.join(tq_s)

    # --- ROOM/MAP STUFF ---

    def set_room_text():
        if prevroom and prevroom != 'main':
            froRoom = roomButtons[curlevel][prevroom]['num']
            for name, b in roomButtons[curlevel].items():
                if b['floor'] != curfloor:
                    continue
                toRoom = b['num']
                bname = b['name']
                if toRoom == froRoom:
                    bname += "\n(YOU ARE HERE)"
                else:
                    bname += " (" + str(roomProxim[curlevel][curfloor][froRoom][toRoom]) + ")"
                roomButtons[curlevel][name]['btext'] = bname

    # --- TASK STUFF ---

    # goodjob = task was done correctly
    # punish = subtract from completion score if not goodjob
    def docurtask(goodjob=True, punish=True, tsk=None):
        if not tsk:
            tsk = store.curtask
        if goodjob:
            store.curtime += tsk['tcost']
            tsk['done'] = True
            store.completion += tsk['scorebonus']
        else:
            store.curtime += tsk['tcost'] // 2
            if Task.NO_REDO in tsk['tags']:
                tsk['done'] = True
                if punish:
                    store.completion -= tsk['scorepenalty']
        if tsk['done'] or store.curtime > tsk['tf']:
            store.hinttext = store.levelHints['default_idle']
        if tsk['done']:
            # activate any follow-ups
            if 'nxt' in tsk:
                for tn in tsk['nxt']:
                    t = store.tasks[curlevel][tn]
                    if t['t0'] == -2:
                        setTlimit(t)

    def update_taskq():
        for tn, t in store.tasks[curlevel].items():
            if t['t0'] == -3:
                meet_prereq = True
                for tn in t['prq']:
                    if not store.tasks[curlevel][tn]['done']:
                        meet_prereq = False
                        break
                if meet_prereq:
                    setTlimit(t)

            if t['done'] or t['t0'] < -1 or (store.curtime < t['t0'] or t['tf'] < store.curtime):
                t['activated'] = False
            elif not t['done'] and (t['t0'] <= store.curtime and store.curtime <= t['tf']):
                t['activated'] = True

            b = store.taskButtons[curlevel][t['btn']]
            if t in store.taskq:
                if not t['activated']:
                    store.taskq.remove(t)
                    if not t['done']:
                        store.completion -= t['scorepenalty']
                    try:
                        store.taskrq.remove(tn)
                    except:
                        pass
                    b['curtask'] = None
                    b['htext'] = ''
                    if 'hidden' in b:
                        b['act'] = []
                    else:
                        if 'taskless' in b:
                            b['act'] = SetVariable('hinttext', levelHints[b['taskless']])
                        else:
                            b['act'] = SetVariable('hinttext', levelHints['default_taskless'])
            else:
                if t['activated']:
                    store.taskq.append(t)
                    b['curtask'] = t
                    b['act'] = [SetVariable('curtask', t)]
                    if 'game' in t:
                        b['act'].append(SetVariable('curgame', t['game']))
                    b['act'] += [Return(t['tlabel']), With(cfade)]
                    setHtext(b)
        generateTodo()
        return

    # --- ITEM/INVENTORY STUFF ---

    def fmtItemName(itm, stk=1):
        tx = itemsAll[itm]['name']
        if itemsAll[itm]['stackable']:
            tx += " (" + str(stk) + ")"
        return tx

    def fmtItemDesc(itm, stk=1):
        tx = itemsAll[itm]['desc']
        if itemsAll[itm]['stackable']:
            tx += " (" + str(stk) + ")"
        return tx

    def invGetStack(giveitem):
        nonestack = True
        for i in range(len(invitems)):
            if not store.itemsAll[store.invitems[i]]['stackable']:
                nonestack = False
        if nonestack:
            return False
        stackhand = -1
        for i in range(len(invitems)):
            if invitems[i] == giveitem:
                stackhand = i
        return stackhand

    def invCountNum(itm):
        counter = 0
        for i in range(len(invitems)):
            if invitems[i] == itm:
                counter += invstacks[i]
        return counter

    def inventoryOk(item_id):
        oneHandEmpty = 'air' in invitems
        itemCanStack = (itemsAll[item_id]['stackable'] and invGetStack(item_id) >= 0)
        bothHandsEqual = (invitems[0] == invitems[1])
        return oneHandEmpty or itemCanStack or bothHandsEqual

    def update_inv(holder=None, myitem=None, mystack=-1, otheritem='air', otherstack=1, useholder=False):
        if useholder:
            if not holder:
                holder = store.curholder

        if useholder:
            giveitem = holder['item']['id']
            givestack = holder['item']['stack']
        else:
            giveitem = otheritem
            givestack = otherstack

        if curhand < 0 and not myitem and not inventoryOk(giveitem):
            # hands are full, but no hand/item is selected, do nothing and leave
            return
        
        stackhand = invGetStack(giveitem)
        canstack = (store.itemsAll[giveitem]['stackable'] and stackhand >= 0)

        if curhand == -1:
            if canstack:
                myhand = stackhand
            else:
                if myitem:
                    myhand = store.invitems.index(myitem)
                elif (giveitem == 'air') == (store.invitems[1] == 'air'):
                    # right hand and item holder: both are air or both are items
                    myhand = (1 if invitems[0] == invitems[1] else 0)
                    # ^ if both hands identical, no point prompting the player to choose a hand
                else:
                    myhand = 1
        else:
            myhand = curhand
            
        if mystack >= 0:
            store.invstacks[myhand] -= mystack
            if store.invstacks[myhand] <= 0:
                store.invitems[myhand] = 'air'
                store.invstacks[myhand] = 1
        else:
            temp = giveitem
            giveitem = store.invitems[myhand]
            store.invitems[myhand] = temp

            if canstack:
                store.invstacks[myhand] += givestack
                givestack = 1
            else:
                temp = givestack
                givestack = store.invstacks[myhand]
                store.invstacks[myhand] = temp

        if useholder:
            if canstack:
                giveitem = {'id': 'air', 'stack': 1}
            else:
                giveitem = {'id': giveitem, 'stack': givestack}
            if holder:
                holder['item'] = giveitem
            else:
                curholder['item'] = giveitem
        
        store.curhand = -1

# only if going to a room indirectly using the large map
label gotoroom_indirect:
    python:
        if prevroom and prevroom != 'main':
            i1 = roomButtons[curlevel][prevroom]['num']
            i2 = roomButtons[curlevel][curroom]['num']
            curtime += roomProxim[curlevel][curfloor][i1][i2]
            prevroom = 'main'
    jump mini_main

# just refreshes mini_main to check if time limit was reached...
label gotoroom_direct:
    jump mini_main

label give_item_prompt(vb='Give', both_hands=False):
    $ showlh = (invitems[0] != 'air')
    if both_hands:
        $ showrh = (invitems[1] != 'air')
    else:
        $ showrh = (invitems[1] != 'air' and invitems[1] != invitems[0])

    $ ltext = fmtItemName(invitems[0], invstacks[0])
    $ rtext = fmtItemName(invitems[1], invstacks[1])

    if both_hands:
        menu:
            "([vb] [ltext] and [rtext])" if showlh and showrh:
                $ ichoice = invitems
            "([vb] [ltext])" if showlh and not showrh:
                $ ichoice = invitems[0]
            "([vb] [rtext])" if showrh and not showlh:
                $ ichoice = invitems[1]
            "(Leave for now)":
                $ ichoice = None
    else:
        menu:
            "([vb] [ltext])" if showlh:
                $ ichoice = invitems[0]
            "([vb] [rtext])" if showrh:
                $ ichoice = invitems[1]
            "(Leave for now)":
                $ ichoice = None
    return
