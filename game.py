import engine
import map


# WW2 mania! #
# A command line ww2 story. #

map = map.Map('level_one_intro')  # initializing map class

ww2_mania = engine.GameEngine(map)  # allowing the game engine to read the room

ww2_mania.start()  # starting the game
