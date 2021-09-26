# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Ellie", color="#ff0000")
define j = Character("Josh", color="#ffff00")
define i = Character("Isaac", color="#0000ff")
default playerName = "player"
define p = Character("[playerName]")


default cave_explored = False
default forest_explored = False
default beach_explored = False

transform zoom_out:
    zoom 0.2

# The game starts here.

label InitialMomentofPanic:
    scene bg_crash_site_default
    show chr_ellie_scared at zoom_out,center

    e "Guys! What do we do? Where the hell are we?"

    show chr_josh_scared at zoom_out,center

    j "I don't know, eveyrthing was happening so fast! I can't believe it."
    e "We need to do something! Let's call for help."

#Option flashes across the screen for the player to try checking their phone but cell service isn't working

menu:
    "What should I do?"
    "Check Phone" if not phone_no:
        $ phone_no = True
        jump phone_no
    "Don't check phone" if not phone_yes:
        $ phone_yes = True
        jump phone_yes


    i "My phone has no signal I can't send anything out"
    e "Mine too"
    j "Same here"
    p "What do we do?"

show chr_isaac_thinking at zoom_out,center
    i = "We should split up. Maybe there's someone on the island that could help us."
show chr_josh_scared at zoom_out,center
    j = "That's a terrible idea. That's what they always say in horror movies before something horrible happens."
show chr_ellie_thinking at zoom_out,center
    e = "But he has a point, maybe we're not alone. I think we should start in the forest, if anything we may be able to find some important resources or shelter."
    j = "No way! I'm staying right here, maybe someone will come by on a boat"
    i = "I think there's a cave on the other side fo the forest, I saw it when we were flying over - we should check it out"
    j = "Are you crazy? I'm not doing that"
    e = "Okay forget it, we're wasting daylight. Let's split up: [playerName] who do you want to go with?"
#option flashes across the screen for player to pick who they want to go with

menu:
    "Who do you want to go with?"
    "Ellie" if not forest_explored:
        $forest_explored = True
        jump forest_explore
    "Josh" if not beach_explored:
        $beach_explored = True
        jump beach_explore
    "Issac" if not cave_explored:
        $cave_explored = True
        jump cave_explore

    return
