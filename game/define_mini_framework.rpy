init python:
    def getMainMap(lvl, floor):
        return f"mini/map/map_{lvl}_main_{floor}.png"

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

    def fmtTimeHinttext():
        mleft = store.tlimit - store.curtime
        hleft = mleft // 60
        mleft %= 60
        sleft = ""
        if hleft:
            sleft += f"{hleft} {'hours' if hleft > 1 else 'hour'}"
        if mleft:
            sleft += f"{' and ' if hleft else ''}{mleft} {'minutes' if mleft > 1 else 'minute'}"
        return f"It's currently {getTimeDig(store.curtime)}. I have {sleft} left."

    # --- TASK/TASKBUTTON FORMATTING ---

    def setTlimit(t):
        t['t0'] = store.curtime
        if ('tf' in t and t['tf'] == 9999) or ('dur' in t and t['dur'] == 9999):
            t['tf'] = store.tlimit
        elif 'dur' in t:
            t['tf'] = min(t['t0'] + t['dur'], store.tlimit)

    def fmtTsk(t):
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
        return "{i}" + t + "{/i}"

    def fmtBaseTask(t):
        return f"- {fmtTsk(t)} [[{roomButtons[curlevel][t['room']]['name']}]"

    def fmtTskButton(t):
        return f"{fmtTsk(t)} ({t['tcost']} min)"

    # sorts tasks by tf, tiebreaking by t0 and then room name
    def generateTodo():
        if len(store.taskq) == 0:
            store.notes_text = "No tasks right now."
            store.notes_text_s = store.notes_text
            return
        tqs = []
        for t in store.taskq:
            tqs.append([t['tf'], t['t0'], not Task.SPECIAL in t['tags'], -t['scorebonus'], fmtBaseTask(t)])
        tqs.sort()
        tq = []
        tq_s = []
        for t in tqs:
            tx = t[4]
            tq.append(tx)
            if not t[2]:
                tx = fmtSpecialTask(tx, True)
            tq_s.append(tx)
        store.notes_text = '\n'.join(tq)
        store.notes_text_s = '\n'.join(tq_s)
    
    def generateScore():
        tx = "Approval rating: "
        if store.completion < store.levelInfo[store.curlevel]['threshold'][0]:
            tx += "Bad"
        elif store.completion > store.levelInfo[store.curlevel]['threshold'][1]:
            tx += "Good"
        else:
            tx += "Mid"
        tx += f"\n\nQuests completed: {completion_f}/{len(store.levelInfo[store.curlevel]['quests'])}"
        for qn, q_ in store.levelInfo[store.curlevel]['quests'].items():
            tx += f"\n- {qn} "
            if q_:
                tx += "(done)"
            else:
                tx += "(to-do)"
        return tx

    # --- ROOM/MAP STUFF ---

    def get_room_text(toRoom, is_map=False):
        if curroom == 'main' and not prevroom:
            return toRoom.upper()

        tx = toRoom.upper()

        froRoom = (prevroom if curroom == 'main' else curroom)
        froRoom_id = roomButtons[curlevel][froRoom]['num']
        toRoom_id = roomButtons[curlevel][toRoom]['num']
        
        add_line = (toRoom == froRoom or not is_map)

        if add_line:
            tx += "\n{size=-20}"
            if toRoom == froRoom:
                tx += "* YOU ARE HERE"
            elif not is_map:
                tx += f"{roomProxim[curlevel][curfloor][froRoom_id][toRoom_id]} MIN"

        return tx + ("{/size}" if add_line else "")

    # --- TASK STUFF ---

    # goodjob = task was done correctly
    # punish = subtract from completion score if not goodjob
    def docurtask(goodjob=True, punish=True, tsk=None, tname=None):
        if not tsk:
            tsk = store.curtask
        if goodjob:
            store.curtime += tsk['tcost']
            tsk['done'] = True
            store.completion += tsk['scorebonus']
            if Task.SPECIAL in tsk['tags'] and tname:
                store.completion_f += 1
                store.levelInfo[store.curlevel]['quests'][tname] = True
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

    # t0 = -1 -> starts when minigame starts
    # t0 = -2 -> has one prerequisite task (that contains *this* task in its 'nxt')
    # t0 = -3 -> has multiple prereqs (contained in *this* task's 'prq')
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

            bt = store.taskButtons[curlevel][t['btn']]
            if t in store.taskq:
                if not t['activated']:
                    store.taskq.remove(t)
                    # if not t['done']:
                    #     store.completion -= t['scorepenalty']
                    try:
                        store.taskrq.remove(tn)
                    except:
                        pass
                    bt['curtask'] = None
                    bt['htext'] = ''
                    if 'hidden' in bt:
                        bt['act'] = []
                    else:
                        if 'taskless' in bt:
                            bt['act'] = SetVariable('hinttext', levelHints[bt['taskless']])
                        else:
                            bt['act'] = SetVariable('hinttext', levelHints['default_taskless'])
            else:
                if t['activated']:
                    store.taskq.append(t)
                    bt['curtask'] = t
                    bt['act'] = [SetVariable('curtask', t), SetVariable('curtask_btn', bt)]
                    if 'game' in t:
                        bt['act'].append(SetVariable('curgame', t['game']))
                    bt['act'] += [Return(t['tlabel'])]
                    if not Task.NO_FADE in t['tags']:
                        bt['act'] += [With(cfade)]
                    bt['htext'] = fmtTskButton(bt['curtask'])
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
        return oneHandEmpty or itemCanStack

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
    
    # check if an item is of a certain type
    def item_is_of_type(itm, typ):
        itm_split = itm.split("_")
        return itm_split[0] == typ

# only if going to a room indirectly using the large map
init python:
    def gotoroom_indirect_py():
        global prevroom
        global roomButtons
        global curtime
        global hinttext
        if prevroom and prevroom != 'main':
            i1 = roomButtons[curlevel][prevroom]['num']
            i2 = roomButtons[curlevel][curroom]['num']
            curtime += roomProxim[curlevel][curfloor][i1][i2]
            prevroom = 'main'
            if i1 != i2:
                hinttext = levelHints['default_idle']

label gotoroom_indirect:
    $ gotoroom_indirect_py()
    jump mini_main

# just refreshes mini_main to check if time limit was reached...
label gotoroom_direct:
    $ hinttext = levelHints['default_idle']
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
            "[vb] [ltext] and [rtext]" if showlh and showrh:
                $ ichoice = invitems
            "[vb] [ltext]" if showlh and not showrh:
                $ ichoice = invitems[0]
            "[vb] [rtext]" if showrh and not showlh:
                $ ichoice = invitems[1]
            "Leave for now":
                $ ichoice = None
    else:
        menu:
            "[vb] [ltext]" if showlh:
                $ ichoice = invitems[0]
            "[vb] [rtext]" if showrh:
                $ ichoice = invitems[1]
            "Leave for now":
                $ ichoice = None
    return
