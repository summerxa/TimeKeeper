init python:
    def getMainMap(lvl, floor):
        return f"mini/map/map_{lvl}_main_{floor}.png"

    # returns True if there are no fetch quests active
    # otherwise, returns True if this button has the currently active fetch quest; and False if it doesn't
    def can_show_task(bt):
        if not bt['curtask']:
            return False
        not_noble_req = (not fetchq or (bt['curtask']['tasktype'] == 'fetchquest' or bt['curtask']['tasktype'] == 'fetchquest_end'))
        not_optional = (not Task.OPTIONAL in bt['curtask']['tags'])
        return not_noble_req and not_optional

    # returns True if last label was a room change (gotoroom) function
    def was_from_roomchange():
        return (len(store.tolabel) >= 8 and store.tolabel[:8] == 'gotoroom')
    
    # whether you have the required items to do the task in your inventory
    def task_can_proceed(item_req=[]):
        if not len(item_req):
            return True
        for i in item_req:
            if i in store.invitems:
                return True
        return False

    # increment the current time and adjust the player's productivity
    # triggers any related events (such as new fetch quests or bonus tasks)
    def addTime(mins, isProductive=False, isBonusTask=False):
        global curtime
        global productivity
        curtime += mins
        for tn, t in store.tasks[store.curlevel]['single'].items():
            if 't0' in t and t['t0'] <= curtime and not tn in fetchq and not tn in levelInfo[curlevel]['quests_done']:
                addFquest(tn, t)
        for tn, t in store.tasks[store.curlevel]['optional'].items():
            if t['t0'] <= curtime and not tn in levelInfo[curlevel]['quests_done']:
                taskButtons[curlevel][t['btn']]['curtask'] = t
        for tn, t in store.bonusq.items():
            if t['t0'] <= curtime and not bonusq[tn]['btn']:
                setTaskButton(tn, tasks[curlevel]['infinite'][tn], task_part='', isBonus=True)
        if isBonusTask:
            productivity = min(100, productivity + 10)
        elif isProductive:
            productivity += (100 - productivity) * 0.01 * mins
        else:
            productivity = max(0, productivity - mins)

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

    # formats the time in mc textbox when player hovers on the clock
    def fmtTimeHinttext():
        mleft = store.levelInfo[store.curlevel]['tf'] - store.curtime
        hleft = mleft // 60
        mleft %= 60
        sleft = ""
        if hleft:
            sleft += f"{hleft} {'hours' if hleft > 1 else 'hour'}"
        if mleft:
            sleft += f"{' and ' if hleft else ''}{mleft} {'minutes' if mleft > 1 else 'minute'}"
        return f"It's currently {getTimeDig(store.curtime)}. I have {sleft} left."

    # calculates minigame score
    def calculateFinalScore():
        for i in range(3):
            if store.player_attrs[i] < store.levelInfo[store.curlevel]['level_threshold'][i]:
                return 0
        return sum(store.player_attrs) * store.productivity * 0.01

    # --- TASK/TASKBUTTON FORMATTING ---

    def fmtTask(task_name, task_part='', task_type='infinite'):
        d = store.tasks[store.curlevel][task_type][task_name]
        if task_type == 'infinite' and 'sequence' in store.tasks[store.curlevel]['infinite'][task_name]:
            d = store.taskTemplates[task_part]
        # if cost of time is 9999 (skips entire minigame), show a smaller value for the time cost
        return d['desc'] + " (" + str(min(levelInfo[curlevel]['tf'] - levelInfo[curlevel]['t0'], d['tcost'])) + " min)"

    # DON'T call this directly! helper method for setTaskButton
    def getTaskButton(all_btns):
        a = all_btns.copy()
        while a:
            bt = renpy.random.choice(a)
            if not store.taskButtons[store.curlevel][bt]['curtask']:
                return bt
            else:
                # ensures we don't keep drawing occupied buttons
                a.remove(bt)
        return None

    # ONLY USE FOR INFINITE GENREATING TASKS
    # task_name = ID of the task
    # task = the actual task itself
    # task_part = optional - for multi-part tasks, the ID of the specific part
    def setTaskButton(task_name, task, task_part='', isBonus=False):
        if 'sequence' in task:
            btn_list = task['btns'][task_part]
        else:
            btn_list = task['btns']

        bt_choice = getTaskButton(btn_list)
        if isBonus:
            bonusq[task_name]['btn'] = bt_choice
        else:
            taskq[task_name]['btn'] = bt_choice
        
        bt = store.taskButtons[store.curlevel][bt_choice]
        bt['curtask'] = task

        bt['act'] = [SetVariable('curtask', task), SetVariable('curtask_btn', bt)]
        if 'sequence' in task:
            to_label = store.taskTemplates[task_part]['tlabel']
            bt['act'] += [SetVariable('curgame', {'type': task_part})]
        else:
            to_label = task['tlabel']
            bt['act'] += [SetVariable('curgame', {'type': task['tasktype']})]
        bt['act'] += [Return(to_label)]
        if 'tags' in task and not Task.NO_FADE in task['tags']:
            bt['act'] += [With(cfade)]
        
        bt['htext'] = fmtTask(task_name, task_part)
    
    # used to find the time that the next bonus task will trigger
    # returns curtime + (random number between a and b)
    # if curtime + b exceeds the time limit of the current level, instead
    #   returns curtime + (random number between a and time remaining)
    def getRandomTime(a, b):
        return curtime + renpy.random.randint(1, min(20, levelInfo[curlevel]['tf'] - curtime))

    # adds a fetch quest to fetchq
    def addFquest(task_name, task):
        fetchq.append(task_name)
        if len(fetchq) == 1:
            activateFquest(task_name, task)
    
    # activates the fetch quest
    def activateFquest(task_name, t):
        bt = store.taskButtons[store.curlevel][t['btn']]
        bt['curtask'] = t
        bt['htext'] = fmtTask(task_name, '', 'single')
        bt['act'] = [SetVariable('curtask', t), SetVariable('curtask_btn', bt), SetVariable('curgame', {}), Return(t['tlabel'])]
    
    # activates the optional quest
    def activateOptquest(task_name, t):
        bt = store.taskButtons[store.curlevel][t['btn']]
        bt['act'] = [SetVariable('curtask', t), SetVariable('curtask_btn', bt), SetVariable('curgame', {}), Return(t['tlabel'])]
    

    # --- ROOM/MAP STUFF ---

    # formats room names in the large map
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

    # tname = name of task
    # goodjob = task was completed (instead of ditching)
    # task_type = either infinite or single
    def docurtask(tname=None, goodjob=True, task_type='infinite'):
        if task_type == 'infinite':
            t = taskTemplates[tname]
        else:
            t = store.tasks[store.curlevel][task_type][tname]
        store.curtask_btn['curtask'] = None
        if task_type == 'infinite':
            if t['type'] == 'small':
                store.bonusq[tname]['btn'] = None
                if levelInfo[curlevel]['bonus_remaining'] > 0:
                    levelInfo[curlevel]['bonus_remaining'] -= 1
                    store.bonusq[tname]['t0'] = getRandomTime(1, 20)
                else:
                    store.bonusq[tname]['t0'] = 9999
            else:
                if 'next' in t:
                    store.taskq[t['parent']]['part'] = t['next']
                    setTaskButton(t['parent'], tasks[curlevel]['infinite'][t['parent']], t['next'])
                else:
                    setTaskButton(tname, tasks[curlevel]['infinite'][tname])
        else:
            if task_type == 'single':
                del fetchq[0]
                if 'next' in t:
                    fetchq.insert(0, t['next'])
                if fetchq: # activate next quest in quest chain, if it is unlocked
                    activateFquest(fetchq[0], tasks[curlevel]['single'][fetchq[0]])
            levelInfo[curlevel]['quests_done'].add(tname)
        
        if goodjob:
            for i in range(len(player_attrs)):
                player_attrs[i] += t['attributes'][i]
            addTime(t['tcost'], goodjob, t['type'] == 'small')
        else:
            addTime(t['tcost'] // 2, goodjob, t['type'] == 'small')

    # --- ITEM/INVENTORY STUFF ---

    # formats name of item when seen in inventory
    def fmtItemName(itm, stk=1):
        tx = itemsAll[itm]['name']
        if itemsAll[itm]['stackable']:
            tx += " (" + str(stk) + ")"
        return tx

    # formats flavor text for items when moused over in map
    def fmtItemDesc(itm, stk=1):
        tx = itemsAll[itm]['desc']
        if itemsAll[itm]['stackable']:
            tx += " (" + str(stk) + ")"
        return tx

    # sorry I forgot what this function does :'D
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

    # counts how many instances of "itm" are in the player's inventory
    def invCountNum(itm):
        counter = 0
        for i in range(len(invitems)):
            if invitems[i] == itm:
                counter += invstacks[i]
        return counter

    # helper method that verifies if player can pick up an item on the map
    def inventoryOk(item_id):
        oneHandEmpty = 'air' in invitems
        itemCanStack = (itemsAll[item_id]['stackable'] and invGetStack(item_id) >= 0)
        return oneHandEmpty or itemCanStack

    '''
    This implementation is absolutely awful spaghetti code, but it hasn't broken yet
    (knock on wood). Don't worry about how it works until something goes horribly wrong.
    USAGE:
    holder = itemholder to drop the item into (this should always be None except when clicking an item button)
    myitem = item in your inventory to remove
    mystack = if myitem is stackable, how many stacks of it to remove
    otheritem = item to place in your inventory
    otherstack = if otheritem is stackable, how many stacks to place
    useholder = if True, swaps the target item b/w your inventory and an itemholder (again, should always be False by default)
    '''
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
            addTime(roomProxim[curlevel][curfloor][i1][i2])
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

# shows menu to give an item to an NPC in fetch quests
label give_item_prompt(npc, npc_id, msg, vb='Give', both_hands=False):
    $ showlh = (invitems[0] != 'air')
    if both_hands:
        $ showrh = (invitems[1] != 'air')
    else:
        $ showrh = (invitems[1] != 'air' and invitems[1] != invitems[0])

    $ ltext = fmtItemName(invitems[0], invstacks[0])
    $ rtext = fmtItemName(invitems[1], invstacks[1])

    # make sure the speaking character is highlighted
    $ clear_focus()
    $ focus_on([npc_id])

    if both_hands:
        menu:
            npc "[msg]"

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
            npc "[msg]"
            
            "[vb] [ltext]" if showlh:
                $ ichoice = invitems[0]
            "[vb] [rtext]" if showrh:
                $ ichoice = invitems[1]
            "Leave for now":
                $ ichoice = None
    $ clear_focus()
    return
