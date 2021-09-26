label forest_explore
scene BG_forest_default
show chr_ellie_neutral at zoom_out, center
play sound "audio/MU_Adventure.ogg"
e "Thanks for coming with me, I know I'm not showing it but I'm terrified"
p "Of course, what are we looking for?"
e "We need to be on high alert. Any sign of human life could be the difference between when or if we get off this island. I can't believe this is our life right now. I don't understand how it's even possible, doesn't it seem crazy? There has to be something here thart could gtell us more about where we are. Do you see anything?"

show chr_ellie_thinking at zoom_out, center

e "I don't know if this was an acciodent, I'm not sure how much I trust our tean– what are you thinking?"

#sus or not sus question
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
