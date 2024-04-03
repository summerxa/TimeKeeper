label start:
    $ all_init_and_load()

    # The following line disables the "back" button when uncommented
    # $ config.rollback_enabled = False

    # call chap1_test_namechange


    # --- Minigame stuff ---

    $ curlevel = 1
    call mini_launch

    call chap1_test_part2

    return

label after_load:
    $ all_init_and_load()

    return
