label start:
    call chars_init_and_load

    # The following line disables the "back" button when uncommented
    # $ config.rollback_enabled = False

    # call chap1_test_sprites
    call chap1_test_charmenu


    # --- Minigame stuff ---

    $ curlevel = 1
    call mini_launch

    call chap1_test_part2

    return

label after_load:
    call chars_init_and_load

    return

label chars_init_and_load:
    python:
        for c in persistent.charmenu_data:
            if not c['id_name'] in chars_current:
                chars_current[c['id_name']] = {
                    'desc': 'desc_default',
                    'small': 'small_default',
                    'big': 'big_default',
                    'alive': True,
                    'unlocked': False,
                    'friend': False,
                    'friendlvl': 0
                }
    return