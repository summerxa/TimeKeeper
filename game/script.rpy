label start:
    $ save_version = config.version

    $ all_init_and_load()

    # Disable the "back" button (commented out for testing purposes)
    # $ config.rollback_enabled = False

    # Unlock all characters and set their names (for testing purposes only)
    call meet_all_chars

    call chapter1

    call mgame_testing

    return

label chapter1:

    call c1_scene1
    call c1_scene2

    # call the minigame, since amelia cutscene is after the tutorial level
    call mini_placeholder([("Amelia sick scene", "c1_scene3")])

    # actual minigame
    call mini_placeholder([
        ("Fetch quest 1 (wine)", "c1_fetch1"),
        ("Fetch quest 2 (jacket)", "c1_fetch2"),
        ("Fetch quest 3 (first Bella interference)", "c1_fetch3"),
        ("Fetch quest 4 (Bella confrontation)", "c1_fetch4")
    ])

    call c1_scene5
    call c1_scene6
    call c1_scene7

    return

label mgame_testing:
    # --- Minigame stuff ---

    $ curlevel = 1
    call mini_launch

    call chap1_test_part2

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
    $ completion = 0
    $ fquest = 'temp'
    while fquest != "leave":
        $ fquest = renpy.display_menu(quests + [("Leave minigame", "leave")])
        if fquest != "leave":
            call expression fquest
            $ completion += 1
    if not completion:
        jump mini_failed
    return
