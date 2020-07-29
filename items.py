
from textwrap import dedent

class Items(Object):
    """Items can create and manage the state of generic game items like
    the gask mask."""
    def __init__(self, quality)


class Weapons(Items):
    """ Weapons can be used by the player to fend off enimes and various other tasks."""

    def __init__(self, damage, quality):
        self.damage = damage
        super().__init__(quality, quality)

    def check_weapons_quality():
        """Notifies player of their weapons quality status and passes values to batte in the player class."""
        if quality > 3:
            print(dedent('Quality is low remember to either repair or replace your weapons soon!'))

        if quality == 0:
            print(dedent('Your weapon is broken!!'))
            return 'broke'

class Food(Items):
    """Food heals or gives extra abilites to a player."""

    def __init__(self, health_addition, quality, ability):
        self.health_addition = health_addition
        super().__init__(quality, quality)
        self.ability = False
