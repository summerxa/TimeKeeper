label start:
    $ save_version = config.version

    $ all_init_and_load()

    # Disable the "back" button (commented out for testing purposes)
    # $ config.rollback_enabled = False

    # Unlock all characters and set their names (for testing purposes only)
    call meet_all_chars

    call chap1_test_animation


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

# for testing purposes only
label meet_all_chars:
    $ char_unlock('mc')
    $ char_unlock('mother')
    $ char_unlock('amelia')
    $ char_unlock('bella')

    $ mother_name = 'MOTHER'
    $ amelia_name = 'AMELIA'
    $ bella_name = 'BELLA'
    $ maria_name = 'MARIA'
