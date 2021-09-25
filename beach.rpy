# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.


label beach_explore:

    scene bg_crash_site_default
    show chr_josh_neutral at zoom_out, center
    j  "Ok, I guess we should look around for anything that might help us"
    hide chr_josh_neutral
    #[Player explores beach, clicking on objects, some may not be important (different camera angles?)]

    #[Finds main clue]
    "Hmmm, this is interesting…"

    scene bg_crash_site_camera
    show chr_josh_neutral at zoom_out, center
    j "Its... a camera?"

    p "It looks like its turned on too"
    p "why would a camera be on this random island"

    j "Maybe somebody's studying the wildlife?"

    p "It's definetly strange though"
    p "I'm gonna go see what else is on this island"
    menu:

        "Who should I go with?"

        "Josh" if not beach_explored:
            $ beach_explored = True
            jump beach_explore
        "Ellie" if not forest_explored:
            $ forest_explored = True
            jump forest_explore
        "Isaac" if not cave_explored:
            $ cave_explored = True
            jump cave_explore
