

# The game starts here.
label start:

    python:
        playerName = renpy.input("What is your name?", length=32)
        playerName = playerName.strip()

    scene bg_black



    "{i}Ugh, we’re only halfway through the flight. I try to control my anxiety, but the FRC worlds competition is only two days away.{/i} "

    play sound "audio/SFX_Alarm.ogg"
    p "Huh?"

    "{b}[[Warning! Critical engine failure! Attempting emergency landing]{/b}"


    j "AAAAAAH!! WE’RE ALL GONNA DIE!"

    e "Stay calm everyone, panicking won't help us. Grab your lifevest from under the seats."

    i "Relax, these high end planes are built for this, it should be able to make a water landing just fine."

    j "Ok... just stay calm..."

    "{i}I haven't even had time to process what's happening, but i find myself grabbing my life vest.
    I hope Isaac is right about this.{/i}"

    play sound "audio/SFX_Crash.ogg"
    pause 8.0
    scene bg_crash_site_default
    stop sound fadeout 0.5
    play music "audio/MU_Tense.ogg"

    show chr_ellie_scared at zoom_out,center
    e "Guys! What do we do? Where the hell are we?"

    show chr_josh_scared at zoom_out,center
    j "I don’t know everything was happening so fast I can’t believe it?"

    e "We need to do something! Let’s call for help."

    #TODO[ Option flashes across the screen for the player to try checking their phone but the cell service isn’t working. In flipping through their phone they see pictures of the team, but no picture of issac?]

    "[[TBD: insert more scared discussion]"

    show chr_isaac_thinking at zoom_out,center
    i"We should split up. Maybe there’s someone on the island that could help us?"

    show chr_josh_scared at zoom_out,center
    j "That’s a terrible idea. That’s what they always say in horror movies before something terrible happens. "

    e "But he has a point, maybe we’re not alone. I think we should start in the forest, if anything we may be able to find some important resources or shelter."

    j "No way! I’m staying right here, maybe someone will come by on a boat."

    i "I think there’s a cave on the other side of the forest, I saw it when we were flying over– we should check it out. "

    j "Are you crazy?! I’m not doing that."

    e "Okay forget it we’re wasting daylight. Let’s split up: [playerName] who do you want to go with?"

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


    # This ends the game.

    return
