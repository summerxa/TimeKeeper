init python:
    def chars_init_and_load():
        charmenu_data = [
            persistent.mc_data,
            persistent.mother_data,
            persistent.amelia_data,
            persistent.bella_data
        ]

        for c in charmenu_data:
            if not c['id_name'] in store.chars_current:
                store.chars_current[c['id_name']] = {
                    'desc': 'desc_default',
                    'small': 'small_default',
                    'big': 'big_default',
                    'alive': True,
                    'friend': False,
                    'friendlvl': 0
                }
            if not c['id_name'] in persistent.chars_unlocked:
                persistent.chars_unlocked[c['id_name']] = False

label start:
    $ chars_init_and_load()

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
    $ chars_init_and_load()

    return
