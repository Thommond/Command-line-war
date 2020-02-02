from game import *

# A command line based game made from classes
# and functions


class World(object):  # a containor for all the chains of levels
    def __init__(self):
        print('For the two main "worlds" this game will be navigating.')


class Europe(World):  # a list of levels

    def __init__(self):
    print('For the first part of the game ')

    def death(self):
        pass


class EastAsia(World):  # a list of levels
    def __init__(self):
        print('For the second part of the game rules apply.')


class Normandy(Europe):  # first level in the first world
    def __init__(self):
        print('For the first part of the game rules apply.')


class Phillipiens(EastAsia):  # first level in the second world
    def __init__(self):
        print('For the second part of the game rules apply.')
