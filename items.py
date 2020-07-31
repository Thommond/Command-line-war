
from textwrap import dedent

class Items(object):
    """Items can create and manage the state of generic game items like
    the gask mask."""
    def __init__(self, quality, ration_rate):
        self.quality = quality
        self.ration_rate = ration_rate


class Weapons(Items):
    """Weapons can be used by the player to fend off enimes and various other tasks."""

    def __init__(self, damage, quality, ration_rate):
        self.damage = damage
        super().__init__(quality, ration_rate)

    def check_weapons_quality():
        """Notifies player of their weapons quality status and passes values to batte in the player class."""
        if quality > 3:
            print(dedent('Quality is low remember to either repair or replace your weapons soon!'))

        if quality == 0:
            print(dedent('Your weapon is broken!!'))
            return 'broke'

class Foods(Items):
    """Food heals or gives extra abilites to a player."""

    def __init__(self, health_addition, quantity, ration_rate, ability=False):
        self.health_addition = health_addition
        self.quantity = quantity
        self.ability = ability
        super().__init__(ration_rate, ration_rate)



    def abilities(sentence_of_ability):
        if self.ability == True:
            print(sentence_of_ability)

# The following instances of the class are for weapons, items and Food used in the game.

gas_mask = Items(10, 10)

boots = Items(10, 15)

bullet_plate = Items(30, 25)

helmet = Items(15, 20)


#   Weapons
rifle = Weapons(2.5, 20, 4)

hands = Weapons(.5, 100, 0)

german_snimper = Weapons(10, 12, 20)

mp40 = Weapons(5, 18, 15)

glock = Weapons(3, 30, 8)

german_pistol = Weapons(4, 25, 10)

machine_gun = Weapons(5, 5, 25)

bazooka = Weapons(25, 1, 100)

# Food

rations = Foods(5, 10, 1)

bag_of_rice = Foods(15, 1, 2)

bag_of_potatos = Foods(15, 1, 3)

chocolate = Foods(20, 1, 5)

Meth = Foods(30, 1, 7)
