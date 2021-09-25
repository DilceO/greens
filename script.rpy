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
