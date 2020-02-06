import engine
import map


# WW2 mania! #


map = map.Map('level_one_intro')

ww2_mania = engine.GameEngine(map)

ww2_mania.start()
