

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

# START START START START START START START START START START START START START START START START START START
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

#PANIC PANIC PANIC PANIC PANIC PANIC PANIC PANIC PANIC PANIC PANIC PANIC PANIC PANIC PANIC PANIC PANIC PANIC PANIC PANIC PANIC

label InitialMomentofPanic:

    scene bg_crash_site_default

    show chr_ellie_scared at zoom_out,center

    e "Guys! What do we do? Where the hell are we?"

    show chr_josh_scared at zoom_out,center

    j "I don't know, eveyrthing was happening so fast! I can't believe it."

    e "We need to do something! Let's call for help."

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

# FOREST FOREST FOREST FOREST FOREST FOREST FOREST FOREST FOREST FOREST FOREST FOREST FOREST FOREST

label forest_explore

scene BG_forest_default

show chr_ellie_neutral at zoom_out, center

play sound "audio/MU_Adventure.ogg"

e "Thanks for coming with me, I know I'm not showing it but I'm terrified"

p "Of course, what are we looking for?"

e "We need to be on high alert. Any sign of human life could be the difference between when or if we get off this island. I can't believe this is our life right now. I don't understand how it's even possible, doesn't it seem crazy? There has to be something here thart could gtell us more about where we are. Do you see anything?"

show chr_ellie_thinking at zoom_out, center

e "I don't know if this was an acciodent, I'm not sure how much I trust our tean– what are you thinking?"

#more dialogue
#insert a clue somewhere here

menu:
    "Go find Isaac" if not cave_explored:
        $cave_explored = true
        jump cave_explore
    "Go find Josh" if not beach_explored:
        $beach_explored = True
        jump beach_explore = true
    "Head back with Ellie":
        jump discoveringClue

#BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH

label beach_explore:

    scene bg_crash_site_default

    show chr_josh_neutral at zoom_out, center

    j  "Ok, I guess we should look around for anything that might help us"

    hide chr_josh_neutral

    #[Player explores beach, clicking on objects, some may not be important (different camera angles?)]

    #[Finds main clue]
    p "Hmmm, this is interesting…"

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

#CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE

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
#    "[[TBD More dialogue]"

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

#the menus about picking who to go with needs an end option

#CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE

label discoveringClue

scene bg beach

show chr_issac_nuetral at zoom_out, right

show chr_ellie_neutral at zoom_out, left

show chr_josh_neutral at zoom_out, center

j "Did you guys find anything?"

p "No people, but a coupole of things out of the ordinary..."

e "Something is going on here..."

i "What do you mean?"

p "I don't think that our plane crash was an accident. Someone wanted us here."

j "That's crazy!"

e "wait no, maybe they're onto something"

i "I'm with Josh, you're off your rocker"

e "Watch your mouth, just because we're stuck here doesn't mean you get to act like a dick"

i "What did you just call me?"

j "Isaac back off, she's not wrong you we shouldn't be turning on eachother, that's the worst thing we can do"

show chr_issac_angry at zoom_out, center

i "You're the last person to talk. You think I'm going to listen to someone afraid of their own fucking shadow? Fuck off Josh"

show chr_ellie_angry at zoom_out, center

e "Watch how you talk to him"

i "Oh and what are you going to do about it"

e "Don't be an asshole Issac"

i "Then don't be abitch Ellie"

p "Guys we should all calm down"

i "No one is talking to you [playerName] so shut it"

show chr_josh_angry at zoom_out, center

j "I'm tired of you treating everyone like dirt, just shut up Issac"

i "Fuck you!"

j "Fuck you!"

e "Hey! Everyone cool it! We're never going to get off this isaland if we're fighting each other. Both of you take a break. Go for a walk, do whatever but don't come back until you've calmed down."

e "You can take a break too, you seem tired. I'm going to head over to the crash site and see if I can find anything else. Yell if you need me."

#insert inner monologue of character

#MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY

label questionedMystery

scene BG_crashsite_default

show chr_ellie_thinking

show chr_josh_thinking

show chr_issac_thinking

e "Something strange is happening on this island and we neeed to gigure it out"

p "I think I have a theory, we're being watched"

j "I think so too, with that camera we found"

i "What would they want with us though"

p "I think they're testing an experimental drug on us, something that affects how we react under stress. They could have even caused the plane to crash"

i "What, like the piece of trash you found in the cave? That's absurd"

e "Hmm, I have been feeling strangely calm considering what's happening"

j "But when could they have done this? I haven't seen anyone on the island"

p "It was on the plane."

j "What?! It was just the four of us then too."

e "Are you trying to say one of us did this?"

#TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR

label pickingTraitor

show chr_ellie_thinking

show chr_issac_thinking

show chr_josh_thinking

scene BG_crashsite_default

play sound "audio/MU_tense.ogg"

p "it's the only thing that makes sense. One of us is lying."

i "But who?"

j "This is crazy! Why would this be happening?"

p "I don't know but if that countdown finishes and we don't know who it is, I don't think we're going to make it out of here alive"

e "This is psychotic____ what do we do?"

p " We're going to have to vote someone out....now."

menu:
    "Who do I vote out?" :
        "Ellie":
            jump bad_end_ellie
        "Josh":
            jump bad_end_josh
        "Issac":
            jump goodEnd

#BAD ENDING BAD ENDING BAD ENDING BAD ENDING BAD ENDING BAD ENDING BAD ENDING BAD ENDING BAD ENDING BAD ENDING BAD ENDING

label bad_end_ellie:

    p "I don't trust Ellie"

    show chr_ellie_scared at center, zoom_out

    e "What the hell, what do you mean!"

    show chr_isaac_thinking at center, zoom_out

    i "I agree, Ellie has been acting really weird"

    show chr_ellie_neutral at center, zoom_out

    e "Hey! Don't jump to conclusions, I'm just stressed."

    show chr_isaac_neutral at center, zoom_out

    i "No You're a traitor! We're leaving without you"

    show chr_josh_neutral at center, zoom_out

    j "We still haven't figured out that leaving part yet..."

    show chr_isaac_neutral at center, zoom_out

    i "Actually, I found a radio before leaving that cave, I think I can call for help"

    hide chr_isaac_neutral at center, zoom_out

    "We tried the radio, and managed to call for help."

    show chr_ellie_neutral at center, zoom_out

    e "You're not actually going to leave without me, are you?"


    p "You got us into this mess, you can find your own way back"

    show chr_ellie_neutral at center, zoom_out with vpunch

    "With Ellie unconscious, we made our way to the rescue boat"

    hide chr_ellie_neutral

    show bg_black with fade

    p "It feels so good to be out of this mess right isa-"

    "I feel a sharp pain in my back."

    "Turning around, I see Isaac holding a bloody knife"

    "[[BAD END]"

label bad_end_josh:

    p "I don't trust Josh"

    show chr_josh_scared at center, zoom_out

    j "What the hell, what do you mean!"

    show chr_isaac_thinking at center, zoom_out

    i "I agree, Josh has been acting really weird"

    show chr_josh_neutral at center, zoom_out

    j "Hey! Don't jump to conclusions, I'm just stressed."

    show chr_isaac_neutral at center, zoom_out

    i "No You're a traitor! We're leaving without you"

    show chr_ellie_neutral at center, zoom_out

    e "We still haven't figured out that leaving part yet..."

    show chr_isaac_neutral at center, zoom_out

    i "Actually, I found a radio before leaving that cave, I think I can call for help"

    "We tried the radio, and managed to call for help."

    show chr_josh_neutral at center, zoom_out

    j "You're not actually going to leave without me, are you?"

    p "You got us into this mess, you can find your own way back"

    show chr_josh_neutral at center, zoom_out with vpunch

    "With Josh unconscious, we made our way to the rescue boat"

    hide chr_josh_neutral

    show bg_black with fade

    p "It feels so good to be out of this mess right isa-"

    "I feel a sharp pain in my back."

    "Turning around, I see Isaac holding a bloody knife"

    "[[BAD END]"

#GOOD ENDING GOOD ENDING GOOD ENDING GOOD ENDING GOOD ENDING GOOD ENDING GOOD ENDING GOOD ENDING GOOD ENDING GOOD ENDING

label goodEnd

p "Issac"

show chr_issac_evilLaugh

play sound "audio/MU_tense.ogg"

play sound "audio/SFX_thunder.ogg"

i "You guys should've seen your faces! 'oh no the plane is crashing' ha! You never would've caught on"

e "What the fuck is wrong with you? You could've gotten us killed!"

j" it's not about you, it's about money. 2 million dollars? I'd do it again!"

p "You won't get away with this!"

i "I already have. You won't even–"

show chr_issac_unconscience at center, zoom_out with vpunch

"Ellie decked Issac"

e "I fucking knew he was messed up! Okay come on guys he won't be out for long. Let's check his pockets to see if we can find something get off this island"

j "Gius! Look! A Phone!"

e "I'll call for help"

"Ellie was smart enough to locate a hidden phone number entitled 'extraction team' in Issac's phone. She sent them a message asking for a boat set to chart course to the nearest country and we were out of there. Once in Estonia we were able to call the embassy and get home. Fuck Issac."

"THE END"

    # This ends the game.

    return
