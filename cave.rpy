# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label cave_explore:

    scene bg_cave_default
    show chr_isaac_neutral at zoom_out, center
    i "Well, this is a cool cave, but I doubt there's anything to help us here"

    "I think i’ll look around just in case"
    hide chr_isaac_neutral
    "[[Finds clue]"

    "Hmmm, what’s this?"

    "[[scrap of paper with info about experimental drug
    Effects set in 15-30 minutes after administration, and persist for up to 8 hours.
    Recipients have heightened awareness and senses. They remain calm even in extreme stress.]"


    "It's about some sort of drug? Why is this here?"

    show chr_isaac_neutral at zoom_out, center
    i "It must be some trash, perhaps it flew off a boat in strong wind. Anyways, it won’t help us get off this island."
    "[[TBD More dialogue]"
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
