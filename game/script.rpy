label start:
    $ save_version = config.version

    $ all_init_and_load()

    # The following line disables the "back" button when uncommented
    # $ config.rollback_enabled = False

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
