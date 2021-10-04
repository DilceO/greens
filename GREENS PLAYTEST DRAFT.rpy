
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
    zoom 0.6
transform left_center:
    xalign 0.2
    yalign 1.0
transform right_center:
    xalign 0.8
    yalign 1.0

init python:
    attempts = 3
    def fail_clue(fail_label):
        globals()['attempts'] -= 1
        if globals()['attempts'] <= 0:
            renpy.jump(fail_label)
# START START START START START START START START START START START START START START START START START START



screen click_clue(x,y,found_label,fail_label):
    zorder 3
    modal True
    python:
        display_attempts = "Attempts: %d" % attempts

    text display_attempts xalign 0.5
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "fullscreen_button.png"
        action Function(fail_clue,fail_label)
    imagebutton:
        xalign x
        yalign y
        idle "clue_button.png"
        action Jump(found_label)




label start:
scene bg_black


python:
    playerName = renpy.input("What is your name?", length=32)
    playerName = playerName.strip()

scene bg_black

"{i}Ugh, we’re only halfway through the flight. I try to control my anxiety, but the FRC worlds competition is only two days away.{/i} "

play sound "audio/SFX_Alarm.ogg"

p "Huh?"

"{b}[[Warning! Critical engine failure! Attempting emergency landing]{/b}"

j "AAAAAAH!! WE’RE ALL GONNA DIE!"

e "Stay calm everyone, panicking won't help us. Grab your life vest from under the seats."

i "Relax, these high end planes are built for this, it should be able to make a water landing just fine."

j "Ok... just stay calm..."

"{i}I haven't even had time to process what's happening, but I find myself grabbing my life vest.
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

hide chr_ellie_scared
show chr_josh_scared at zoom_out,center

j "I don't know, everything was happening so fast! I can't believe it."
hide chr_josh_scared
show chr_ellie_scared at zoom_out,center
e "We need to do something! Let's call for help."

hide chr_ellie_scared
show chr_isaac_scared at zoom_out,center
i "My phone has no signal I can't send anything out"
hide chr_isaac_scared
show chr_ellie_scared at zoom_out,center
e "Mine too"
hide chr_ellie_scared
show chr_josh_scared at zoom_out,center
j "Same here"

p "What do we do?"

hide chr_josh_scared
show chr_isaac_thinking at zoom_out,center

i "We should split up. Maybe there's someone on the island that could help us."

hide chr_isaac_thinking
show chr_josh_scared at zoom_out,center

j "That's a terrible idea. That's what they always say in horror movies before something horrible happens."

hide chr_josh_scared
show chr_ellie_thinking at zoom_out,center

e "But he has a point, maybe we're not alone. I think we should start in the forest, if anything we may be able to find some important resources or shelter."

hide chr_ellie_thinking
show chr_josh_scared at zoom_out,center
j "No way! I'm staying right here, maybe someone will come by on a boat"

hide chr_josh_scared
show chr_isaac_thinking at zoom_out,center
i "I think there's a cave on the other side of the forest, I saw it when we were flying over - we should check it out"

hide chr_isaac_thinking
show chr_josh_scared at zoom_out,center
j "Are you crazy? I'm not doing that"

hide chr_josh_scared
show chr_ellie_neutral at zoom_out,center
e "Okay forget it, we're wasting daylight. Let's split up: [playerName] who do you want to go with?"

#option flashes across the screen for player to pick who they want to go with

menu:
    "Who do you want to go with?"
    "Ellie" if not forest_explored:
        $forest_explored = True
        jump forest_explore
    "Josh" if not beach_explored:
        $beach_explored = True
        jump beach_explore
    "Isaac" if not cave_explored:
        $cave_explored = True
        jump cave_explore

# FOREST FOREST FOREST FOREST FOREST FOREST FOREST FOREST FOREST FOREST FOREST FOREST FOREST FOREST

label forest_explore:

scene bg_forest_default

show chr_ellie_neutral at zoom_out, center

play music "audio/MU_Adventure.ogg" fadeout 1.0 fadein 1.0

e "Thanks for coming with me, I know I'm not showing it but I'm terrified"


e "We need to be on high alert. Any sign of human life could be the difference between when or if we get off this island. I can't believe this is our life right now."
e "I don't understand how it's even possible, doesn't it seem crazy? There has to be something here that could tell us more about where we are. Do you see anything?"
$attempts = 3
hide chr_ellie_neutral
window hide
show screen click_clue(0.4,0.3,"forest_found_clue","forest_fail_clue")
pause

label forest_found_clue:
window show
hide screen click_clue
p "There's a phone here."
show chr_ellie_neutral at zoom_out, center
e "Really? Let me look."

hide chr_ellie_neutral
show chr_ellie_thinking at zoom_out, center

e "It's locked, but there's a text message I can read"
e "It says 'Is our agent ready?'"

p "What? Agent? Like a spy?"

e "Maybe"
e "I don't know if this crash was an accident, I'm not sure how much I trust our team– what are you thinking?"

p "Hmm, I'm not going to jump to conclusions yet."

jump forest_end
label forest_fail_clue:
window show
hide screen click_clue
p "Nope, couldn't find anything around here"

label forest_end:
p "I'm going to see what the others have to say"

menu:
    "Go find Isaac" if not cave_explored:
        $cave_explored = True
        jump cave_explore
    "Go find Josh" if not beach_explored:
        $beach_explored = True
        jump beach_explore
    "Head back with Ellie" if cave_explored and beach_explored:
        jump discoveringClue

#BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH BEACH

label beach_explore:

scene bg_crash_site_default

show chr_josh_scared at zoom_out, center

j  "I can't believe this is happening! I knew there was a reason to be scared of flying."

p "Let's just stay focused, we need to find a way to get help"

j  "Ok, I guess we should look around for anything that might help us"

hide chr_josh_neutral

$attempts = 3
window hide
show screen click_clue(0.5,0.8,"beach_found_clue","beach_fail_clue")
pause

label beach_found_clue:
window show
hide screen click_clue
p "Hmmm, this is interesting…"

scene bg_crash_site_camera

show chr_josh_neutral at zoom_out, center

j "It's... a camera?"

p "It looks like its turned on too"

p "why would a camera be on this random island"

show chr_josh_thinking at zoom_out, center
j "Maybe somebody's studying the wildlife?"

p "It's definitely strange though"
jump beach_end

label beach_fail_clue:
window show
hide screen click_clue
p "Sorry, couldn't find anything here"

label beach_end:
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
    "Head back to the beach" if cave_explored and forest_explored:
        jump discoveringClue

#CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE CAVE

label cave_explore:

scene bg_cave_default

show chr_isaac_neutral at zoom_out, center

i "Well, this is a cool cave, but I doubt there's anything to help us here"

i "I suppose we no longer have a chance to compete in FRC Worlds. What a shame"

p "Oh, I totally forgot about that..."

p "Anyways, I think I’ll look around here just in case there's something useful"

hide chr_isaac_neutral

$attempts = 3
window hide
show screen click_clue(0.7,0.3,"cave_found_clue","cave_fail_clue")
pause

label cave_found_clue:
window show
hide screen click_clue
scene bg_cave_stickynote

p "Hmmm, what’s this?"

"[[scrap of paper with info about experimental drug]"
"-Effects set in 15-30 minutes after administration, and persist for up to 4 hours."
"-Recipients have heightened awareness and senses. They remain calm even in extreme stress."

p "It's about some sort of drug? Why is this here?"

show chr_isaac_neutral at zoom_out, center

i "It must be some trash, perhaps it flew off a boat in strong wind. Anyways, it won’t help us get off this island."

p "Sure, but it seems interesting."
jump cave_end

label cave_fail_clue:
window show
hide screen click_clue

p "Looks like there's nothing here."

show chr_isaac_neutral at zoom_out, center
i "I told you so."

label cave_end:
p "I'll go see what else is going on"
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
    "Head back to the beach" if beach_explored and forest_explored:
        jump discoveringClue



#CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE CLUE

label discoveringClue:

scene BG_crash_site_default

show chr_isaac_neutral at zoom_out, right_center

show chr_ellie_neutral at zoom_out, left_center

show chr_josh_neutral at zoom_out, center

j "Did you guys find anything?"

p "No people, but a couple of things out of the ordinary..."

e "Something is going on here..."

i "What do you mean?"

p "I don't think that our plane crash was an accident. Someone wanted us here."

j "That's crazy!"

e "wait no, maybe they're onto something"

i "I'm with Josh, you're off your rocker"

e "Watch your mouth, just because we're stuck here doesn't mean you get to act like a dick"

i "What did you just call me?"

j "Isaac back off! she's not wrong, we shouldn't be turning on eachother, that's the worst thing we can do"

scene bg_crash_site_default
show chr_isaac_neutral at zoom_out, center

i "You're the last person to talk. You think I'm going to listen to someone afraid of their own fucking shadow? Fuck off Josh"

hide chr_isaac_neutral
show chr_ellie_neutral at zoom_out, center

e "Watch how you talk to him"

hide chr_ellie_neutral
show chr_isaac_neutral at zoom_out, center

i "Oh and what are you going to do about it"

hide chr_isaac_neutral
show chr_ellie_neutral at zoom_out, center

e "Don't be an asshole Isaac"

hide chr_ellie_neutral
show chr_isaac_neutral at zoom_out, center

i "Then don't be a bitch Ellie"

p "Guys we should all calm down"

i "No one is talking to you [playerName] so shut it"

hide chr_isaac_neutral
show chr_josh_neutral at zoom_out, center

j "I'm tired of you treating everyone like dirt, just shut up Isaac"

hide chr_josh_neutral
show chr_isaac_neutral at zoom_out, center

i "Fuck you!"

hide chr_isaac_neutral
show chr_josh_neutral at zoom_out, center

j "Fuck you!"

hide chr_josh_neutral
show chr_ellie_neutral at zoom_out, center
e "Hey! Everyone cool it! We're never going to get off this island if we're fighting each other. Both of you take a break. Go for a walk, do whatever but don't come back until you've calmed down."

e "You can take a break too, you seem tired. I'm going to head over to the crash site and see if I can find anything else. Yell if you need me."

#insert inner monologue of character

#MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY MYSTERY


label questionedMystery:

default wrongGuesses = 0

scene bg_crash_site_default

"{i}After a while, everyone calmed down{/i}"

show chr_ellie_thinking at zoom_out, right_center

show chr_josh_thinking at zoom_out, left_center

show chr_isaac_thinking at zoom_out, center

e "Something strange is happening on this island and we need to figure it out"

p "I think I have a theory..."

menu:
    "What is happening?"

    "Someone is watching us":
        jump Q1_correct
    "We are hallucinating":
        $wrongGuesses += 1
        jump Q1_fail
    "We just happened to crash on a random island":
        $wrongGuesses += 1
        jump Q1_fail

label Q1_fail:
    e "No, that doesn't make sense to me."

    i "Yeah, what are you saying?"

    j "I think someone is watching us, I found a hidden camera on the beach"
    jump Q2
label Q1_correct:
j "I think so too, there was a secret camera on the beach"

label Q2:
i "Who is watching though?"

menu:
    "Who is watching us?"

    "A crazy billionare who owns this island":
        $wrongGuesses += 1
        jump Q2_fail
    "A biomedical company":
        jump Q2_correct
    "The Illuminati":
        $wrongGuesses += 1
        jump Q2_fail

label Q2_correct:
i "There was that strange paper in the cave talking about a drug, but I doubt it's relevant"

e "Hmm, but I have been feeling somewhat nauseous, but it may just be stress"

j "Yeah, same here"
jump Q3

label Q2_fail:
    j "That can't be right"

    i "This may have something to do with that strange note in the cave..."
    i "It mentioned some sort of drug. Perhaps we are being experimented on?"

label Q3:
j "So you think we were drugged? But when?"

menu:
    "When were we given the drug?"

    "On the plane before we crashed":
        jump Q3_correct
    "At the airport":
        $wrongGuesses += 1
        jump Q3_fail_1
    "After we crashed":
        $wrongGuesses += 1
        jump Q3_fail_2

label Q3_fail_1:
    i "You're not making any sense"
    i "The note said the effects last for 4 hours, It's been way longer than that"

    j "So it must have been on the plane?"
    jump Q4
label Q3_fail_2:
    e "Huh? But we havent eaten anything after we crashed"
    j "I think it must have been on the plane."
    jump Q4

label Q3_correct:
    e "Yeah that would be the only time it could happen..."
label Q4:
i "But how can that be, there was nobody else on that plane!"

e "Are you trying to say one of us did this?"

#TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR TRAITOR

label pickingTraitor:

show chr_ellie_thinking at zoom_out, right_center

show chr_josh_thinking at zoom_out, left_center

show chr_isaac_thinking at zoom_out, center

play music "audio/MU_tense.ogg" fadein 1.0 fadeout 1.0

p "it's the only thing that makes sense. One of us is lying."

i "But who?"

j "This is crazy! Why would this be happening?"

p "I don't know, but our lives could be at risk if we don't find out"

e "This is psychotic! what do we do?"

p " We're going to have to vote someone out....now."

if wrongGuesses >= 2:
    jump bad_end_player

menu:
    "Who do I vote out?"
    "Ellie":
        jump bad_end_ellie
    "Isaac":
        jump goodEnd
    "Josh":
        jump bad_end_josh

#BAD ENDING BAD ENDING BAD ENDING BAD ENDING BAD ENDING BAD ENDING BAD ENDING BAD ENDING BAD ENDING BAD ENDING BAD ENDING

label bad_end_ellie:

scene bg_crash_site_default
p "I don't trust Ellie"

show chr_ellie_scared at center, zoom_out

e "What the hell, what do you mean!"

hide chr_ellie_scared
show chr_isaac_thinking at center, zoom_out

i "I agree, Ellie has been acting really weird"

hide chr_isaac_thinking
show chr_ellie_neutral at center, zoom_out

e "Hey! Don't jump to conclusions, I'm just stressed."

hide chr_ellie_neutral
show chr_isaac_neutral at center, zoom_out

i "No You're a traitor! We're leaving without you"

hide chr_isaac_neutral
show chr_josh_neutral at center, zoom_out

j "We still haven't figured out that leaving part yet..."

hide chr_josh_neutral
show chr_isaac_neutral at center, zoom_out

i "Actually, I found a radio before leaving that cave, I think I can call for help"

hide chr_isaac_neutral at center, zoom_out

"{i}We tried the radio, and managed to call for help.{/i}"

show chr_ellie_neutral at center, zoom_out

e "You're not actually going to leave without me, are you?"

p "You got us into this mess, you can find your own way back"

show chr_ellie_neutral at center, zoom_out with vpunch
stop music fadeout 1.0
"With Ellie unconscious, we made our way to the rescue boat"

hide chr_ellie_neutral

show bg_black with fade

p "It feels so good to be out of this mess right isa-"

"{i}I feel a sharp pain in my back.

Turning around, I see Isaac holding a bloody knife{/i}"

"[[BAD END :( ]"

return

label bad_end_josh:

scene bg_crash_site_default
p "I don't trust Josh"

show chr_josh_scared at center, zoom_out

j "What the hell, what do you mean!"

hide chr_josh_scared
show chr_isaac_thinking at center, zoom_out

i "I agree, Josh has been acting really weird"

hide chr_isaac_thinking
show chr_josh_neutral at center, zoom_out

j "Hey! Don't jump to conclusions, I'm just stressed."

hide chr_josh_neutral
show chr_isaac_neutral at center, zoom_out

i "No You're a traitor! We're leaving without you"

hide chr_isaac_neutral
show chr_ellie_neutral at center, zoom_out

e "We still haven't figured out that leaving part yet..."

hide chr_ellie_neutral
show chr_isaac_neutral at center, zoom_out

i "Actually, I found a radio before leaving that cave, I think I can call for help"

"{i}We tried the radio, and managed to call for help.{/i}"

show chr_josh_neutral at center, zoom_out

j "You're not actually going to leave without me, are you?"

p "You got us into this mess, you can find your own way back"

show chr_josh_neutral at center, zoom_out with vpunch
stop music fadeout 1.0
"With Josh unconscious, we made our way to the rescue boat"

hide chr_josh_neutral

show bg_black with fade

p "It feels so good to be out of this mess right isa-"

"{i}I feel a sharp pain in my back.

Turning around, I see Isaac holding a bloody knife{/i}"

"[[BAD END :( ]"
return


label bad_end_player:
i "If anything, I don't trust you [playerName]"

e "Yeah, you seemed like you were trying to throw us off from finding out what was happening"

j "I hate to say it, but thats right..."

p "Wait! Think about what you're doing!"

i "No You're a traitor! We're leaving without you"

e "We still haven't figured out that leaving part yet..."

i "Actually, I found a radio before leaving that cave, I think I can call for help"

p "You're not actually going to leave without me, are you?"

i "You got us into this mess, you can find your own way back!"

scene bg_black with vpunch

"[[BAD END]"
return




#GOOD ENDING GOOD ENDING GOOD ENDING GOOD ENDING GOOD ENDING GOOD ENDING GOOD ENDING GOOD ENDING GOOD ENDING GOOD ENDING

label goodEnd:

scene bg_crash_site_default
p "Isaac"

show chr_isaac_neutral at zoom_out,center

i "You guys should've seen your faces! 'oh no the plane is crashing' ha! You never would've caught on"

hide chr_isaac_neutral
show chr_ellie_neutral at zoom_out,center

e "What the fuck is wrong with you? You could've gotten us killed!"

hide chr_ellie_neutral
show chr_isaac_neutral at zoom_out,center

i" it's not about you, it's about money. 2 million dollars? I'd do it again!"

p "You won't get away with this!"

i "I already have. You won't even–"

show chr_isaac_neutral at zoom_out,center with vpunch

"{i}Ellie decked Isaac{/i}"

hide chr_isaac_neutral
show chr_ellie_neutral at zoom_out,center

e "I fucking knew he was messed up! Okay come on guys he won't be out for long. Let's check his pockets to see if we can find something get off this island"

hide chr_ellie_neutral
show chr_josh_neutral at zoom_out,center

j "Guys! Look! He had a phone!"

hide chr_josh_neutral
show chr_ellie_neutral at zoom_out,center

e "I'll call for help"

stop music fadeout 1.0
"{i}Ellie was smart enough to locate a hidden phone number entitled 'extraction team' in Isaac's phone.{/i}"
"{i}She sent them a message asking for a boat set to chart a course to the nearest country and we were out of there. Once in Estonia we were able to call the embassy and get home. Fuck Isaac.{/i}"

"THE END"


return
