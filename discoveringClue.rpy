


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
#choices menu appears for them to pick if everyone goes away or comes back
#Just realized a MAJOR plotline problem will need to pivot and change this sequence (ahhh)
menu:
    "What should I do?"
    "Wait for them to come back" :
        jump questionedMystery
    "Snoop through their phones":
        jump snoopPhones

label snoopPhones
menu:
    "Whose phone should I look through?"
    "Ellie" if not elliePhone_checked:
        $elliePhone_checked = True
        jump elliePhone
    "Josh" if not joshPhone_checked:
        $joshPhone_checked = True
        jump JoshPhone
    "Issac" if not issacPlhone_checked:
        $issacPhone_checked
        jump IssacPhone
