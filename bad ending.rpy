# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.


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
