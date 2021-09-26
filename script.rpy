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





label InitialMomentofPanic:
    scene bg CrashSite
    show ellie scared
    e "Guys! What do we do? Where the hell are we?"
    show chr_josh_scared
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
show issac nuetral
    i = "We should split up. Maybe there's someone on the island that could help us."
    j = "That's a terrible idea. That's what they always say in horror movies before something horrible happens."
    show ellie thinking
    e = "But he has a point, maybe we're not alone. I think we should start in the forest, if anything we may be able to find some important resources or shelter."
    j = "No way! I'm staying right here, maybe someone will come by on a boat"
    i = "I think there's a cave on the other side fo the forest, I saw it when we were flying over - we should check it out"
    j = "Are you crazy? I'm not doing that"
    e = "Okay forget it, we're wasting daylight. Let's split up: [playerName] who do you want to go with?"
#option flashes across the screen for player to pick who they want to go with
menu:
    "Ellie" if not forest_explored:
        $forest_explored = True
        jump forest_explore
    "Josh" if not beach_explored:
        $beach_explored = True
        jump beach_explore
    "Issac" if not cave_explored:
        $cave_explored = True
        jump cave_explore



label forest_explore
scene bg forest
show ellie nuertral
e "Thanks for coming with me, I know I'm not showing it but I'm terrified"
p "Of course, what are we looking for?"
e "We need to be on high alert. Any sign of human life could be the difference between when or if we get off this island. I can't believe this is our life right now. I don't understand how it's even possible, doesn't it seem crazy? There has to be something here thart could gtell us more about where we are. Do you see anything?"
show ellie thinking
e "I don't know if this was an acciodent, I'm not sure how much I trust our tean– what are you thinking?"
#sus or not sus
menu:
    "I agree, this seems fishy":
        jump sus_agree
    "You're just being paranoid":
        jump sus_disagree

label sus_agree
p "I agree this seems fishy"
e "Thank god I thought I was going crazy! What should we do?"
p "We've got to tell the others maybe they've also noticed something wild going on?"
e "I don't know, something about the others seems off. Should we head back?"
jump forest_end

label sus_disagree
p "You're just being paranoid"
e "You think so? I don't know, this whole thing seems just a little too orchestrated to have been an accident"
p "But what are the odds that someone would do all of this and why?"
e "I'm not sure, but if it is, we better find out, should we head back?"
jump forest_end

label forest_end
forest_explored = True
menu:
    "Go find Isaac" if not cave_explored:
        $cave_explored = true
        jump cave_explore
    "Go find Josh" if not beach_explored:
        $beach_explored = True
        jump beach_explore = true
    "Head back with Ellie":
        jump discoveringClue

label discoveringClue
scene bg beach
show Issac neutral
show Ellie neutral
show Josh neutral

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
show Issac Angry
i "You're the last person to talk. You think I'm going to listen to someone afraid of their own fucking shadow? Fuck off Josh"
show Ellie Angry
e "Watch how you talk to him"
i "Oh and what are you going to do about it"
e "Don't be an asshole Issac"
i "Then don't be abitch Ellie"
p "Guys we should all calm down"
i "No one is talking to you [playerName] so shut it"
show Josh Angry
j "I'm tired of you treating everyone like dirt, just shut up Issac"
i "Fuck you!"
j "Fuck you!"
#more dialogue
show Ellie angry
show Issac angry
show Josh angry
e "Hey! Everyone cool it! We're never going to get off this isaland if we're fighting each other. Both of you take a break. Go for a walk, do whatever but don't come back until you've calmed down."
e "You can take a break too, you seem tired. I'm going to head over to the crash site and see if I can find anything else. Yell if you need me."
#choices menu appears for them to pick if everyone goes away or comes back




label questionedMystery
scene bg beach
show Ellie thinking
show Josh thinking
show Issac thinking
e "Something strange is happening on this island and we neeed to gigure it out"
p "I think I have a theory"

#choices menu to pick what's going on
j "I think so too, with that camera we found"
#choices to say what it is
i "What would they want with us though"
#choices

p "I think they're testing an experimental drug on us, something that affects how we react under stress. They could have even caused the plane to crash"
i "What, like the piece of trash you found in the cave? That's absurd"
e "Hmm, I have been feeling strangely calm considering what's happening"
j "But when could they have done this? I haven't seen anyone on the island"
#choices menu

p "It was on the plane."
j "What?! It was just the four of us then too."
e "Are you trying to say one of us did this?"



label pickingTraitor
show ELLIE thinking
show ISSAC thinking
show JOSH thinking
scene bg beach
p "it's the only thing that makes sense. One of us is lying."
i "But who?"
j "This is crazy! Why would this be happening?"
p "I don't know but if that countdown finishes and we don't know who it is, I don't think we're going to make it out of here alive"
e "This is psychotic____ what do we do?"
p " We're going to have to vote someone out....now."

#more dialogue tbd
#choices menu






    # This ends the game.

    return
