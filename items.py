
from textwrap import dedent

class Items(object):
    """Items can create and manage the state of generic game items like
    the gask mask."""
    def __init__(self, name, quality, ration_rate, type=False):
        self.name = name
        self.quality = quality
        self.ration_rate = ration_rate
        self.type = type

class Weapons(Items):
    """Weapons can be used by the player to fend off
    enimes and various other tasks."""

    def __init__(self, damage, name, quality, ration_rate, type=False):
        self.damage = damage
        super().__init__(name, quality, ration_rate, type)

    def check_weapons_quality():
        """Notifies player of their weapons quality
        status and passes values to batte in the player class."""

        if quality > 3:
            return 'Quality is low remember to either repair or replace your weapons soon!'

        if quality == 0:
            return 'Your weapon is broke!!'

        else:
            return 'Looks like your weapon is a-okay and ready for your next battle!'

class Foods(Items):
    """Food heals or gives extra abilites to a player."""

    def __init__(self, health_addition, quantity, name, ration_rate, type=False, ability=False):
        self.health_addition = health_addition
        self.quantity = quantity
        super().__init__(name, ration_rate, ration_rate, type)
        self.ability = ability



    def abilities(sentence_of_ability):
        if self.ability == True:
            print(sentence_of_ability)


# Store inventory and fint_item check

# Classical items

gas_mask = Items("gas_mask", 10, 10)

boots = Items("boots", 10, 15)

bullet_plate = Items("bullet_plate", 30, 25)

helmet = Items("helmet", 15, 20)

#   Weapons
rifle = Weapons(2.5, "rifle", 20, 4, "weapon")

hands = Weapons(.5, "hands", 100, 0)

german_sniper = Weapons(10, "sniper", 12, 20)

mp40 = Weapons(5, "mp40", 18, 15)

glock = Weapons(3, "glock", 30, 8)

german_pistol = Weapons(4, "g-pistol", 25, 10)

machine_gun = Weapons(5, "machine_gun", 5, 25)

bazooka = Weapons(25, "bazooka", 1, 100)

# Food

rations = Foods(5, 10, "rations", 1)

chocolate = Foods(20, 1, "chocolate", 5)

meth = Foods(30, 1, "meth", 7)

list_of_items = {
    "weapons": {

    "rifle": rifle,
    "sniper": german_sniper
    },

    "items": {

    "gas_mask": gas_mask,
    "boots": boots
     },

    "food": {

    "rations": rations,
    "meth": meth
    }
};

def find_item(choice_of_item, user, desired_type):

    """Loops through all items to make sure player string input is a
    actual item from the game. And checks if
    they have that item in the inventory."""

    for category in list_of_items.values():
        for item in category:
            if choice_of_item == item and item in user.player_inventory:
                print('Your item choice is {}'.format(item))

                for item in category.values():
                    if desired_type == item.type:
                        return item

                    else:
                        return False
            else:
                return False
