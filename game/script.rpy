label start:
    $ save_version = config.version

    $ all_init_and_load()

    # Disable the "back" button (commented out for testing purposes)
    # $ config.rollback_enabled = False

    call chapter1 from _call_chapter1

    return

label chapter1:

    # call c1_scene1 from _call_c1_scene1
    # #call c1_scene1_5 #only for testing
    # call c1_scene2 from _call_c1_scene2

    # # eventually this will be part of the tutorial minigame
    # call c1_scene3 from _call_c1_scene3

    show mc 1a
    s "Hello, before you start make sure to open {a=https://www.youtube.com/watch?v=dQw4w9WgXcQ}this form{/a} and fill it in as you play"

    # minigame
    $ node_unlock('c1_mgame')
    $ isTutorial = True
    $ curlevel = 1
    call mini_launch from _call_mini_launch_1

    show mc 1a

    $ score = calculateFinalScore()
    s "Your score was [score]\nStay on this screen, as you will need to record this score in the feedback form."

    # call c1_scene5 from _call_c1_scene5
    # call c1_scene6 from _call_c1_scene6
    # call c1_scene7 from _call_c1_scene7

    # TODO could del chapter 1 minigame data to free up space...?
    # code: del myDict[key]
    # just remember to save player score/fetch quests completed bc may be useful later

    return

label mgame_testing:
    # --- Minigame stuff ---

    $ curlevel = 1
    call mini_launch from _call_mini_launch

    call chap1_test_part2 from _call_chap1_test_part2

    return

label after_load:

    if save_version != config.version and persistent.showversionwarning:
        show screen prompt_diffversion(save_version, config.version)

    $ all_init_and_load()

    return

# --- FOR TESTING PURPOSES ONLY ---

label meet_all_chars:
    $ char_unlock('mc')
    $ char_unlock('mother')
    $ char_unlock('amelia')
    $ char_unlock('bella')

    $ mother_name = 'MOTHER'
    $ amelia_name = 'AMELIA'
    $ bella_name = 'BELLA'
    $ maria_name = 'MARIA'
    return

# simulates entering a fetch quest
# however, tasks can be done repeatedly or in any order for testing convenience
label mini_placeholder(quests):
    $ fquest = 'temp'
    while fquest != "leave":
        $ fquest = renpy.display_menu(quests + [("Leave minigame", "leave")])
        if fquest != "leave":
            call expression fquest from _call_expression
    return
