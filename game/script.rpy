label start:
    $ save_version = config.version

    $ all_init_and_load()

    # The following line disables the "back" button when uncommented
    # $ config.rollback_enabled = False

    # This label unlocks all characters and sets their names when uncommented
    call meet_all_chars

    call chap1_test_bgs

    call chap1_test_snow


    # --- Minigame stuff ---

    $ curlevel = 1
    call mini_launch

    call chap1_test_part2

    return

label after_load:
    if save_version != config.version and persistent.showversionwarning:
        show screen popup_diffversion_prompt(save_version, config.version)

    $ all_init_and_load()

    return

label meet_all_chars:
    $ char_unlock('mc')
    $ char_unlock('mother')
    $ char_unlock('amelia')
    $ char_unlock('bella')

    $ mother_name = 'Mother'
    $ amelia_name = 'Amelia'
    $ bella_name = 'Bella'
    $ maria_name = 'Maria'
