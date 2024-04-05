label start:
    $ save_version = config.version

    $ all_init_and_load()

    # The following line disables the "back" button when uncommented
    # $ config.rollback_enabled = False

    call chap1_test_charmenu


    # --- Minigame stuff ---

    $ curlevel = 1
    call mini_launch

    call chap1_test_part2

    return

label after_load:
    if save_version and save_version != config.version:
        show screen popup_diffversion_prompt(save_version, config.version)

    $ all_init_and_load()

    return
