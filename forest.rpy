# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label forest_explore:

    show chr_ellie_neutral at zoom_out, center
    e "We need to be on high alert. Any sign of human life could be the difference between when or if we get off this island. I can’t believe this is our life right now. I don’t understand how it’s even possible, doesn’t it seem crazy? There has to be something around here that could tell us more about where we are. Do you see anything?"

 #TODO[Player is prompted to look around and see if anything feels out of place– if they see the hidden clue they are able to click on it, if not the game keeps going.
    "[[Player finds clue (phone)]"

#TODO what is on phone
    "[[TBD dialogue about phone]"

    show chr_ellie_thinking
    e "I don’t know if this was an accident, I’m not sure how much I trust our team– what are you thinking?"

#[Player is prompted either to tell ellie she’s suspicious or not]


#[Insert more ellie dialogue]

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
