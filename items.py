
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
        status and passes values to battle in the player class."""

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

gas_mask = Items("gas_mask", 10, 10, "item")

boots = Items("boots", 10, 15)

bullet_plate = Items("bullet_plate", 30, 25, "item")

helmet = Items("helmet", 15, 20, "item")

#   Weapons
rifle = Weapons(2.5, "rifle", 20, 4, "weapon")

hands = Weapons(.5, "hands", 100, 0, "weapon")

german_sniper = Weapons(10, "sniper", 12, 20, "weapon")

mp40 = Weapons(5, "mp40", 18, 15, "weapon")

glock = Weapons(3, "glock", 30, 8, "weapon")

german_pistol = Weapons(4, "g-pistol", 25, 10, "weapon")

machine_gun = Weapons(5, "machine_gun", 5, 25, "weapon")

bazooka = Weapons(25, "bazooka", 1, 100, "weapon")

# Food

rations = Foods(5, 10, "rations", 1, "food")

chocolate = Foods(20, 1, "chocolate", 5, "food")

meth = Foods(30, 1, "meth", 7, "food")


list_of_items = {
    "weapons": {

    "rifle": rifle,
    "sniper": german_sniper,
    "hands": hands
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

    """Loops through all items to make sure p
    layer string input is an actual item from the game.
    And checks if they have that item in the inventory.
    Finally returns the item if it matches the desired type."""

    for category in list_of_items.values():
        if choice_of_item in user.player_inventory:
            for item in category.values():
                if item.name == choice_of_item:
                    if item.type == desired_type:
                        print(item.type)
                        return item
        else:
            return False

    return "Looks like that is not a item at all."

def repair_item(item_to_repair):

    """Updating the users weapon or
        items to restore to default."""

    if item_to_repair.repair_cost == False:
        message_pop_up('This item cannot be repaired.')

    else:

        print('So you want to repair the {}, for {}?'.format(item_to_repair, item_to_repair.repair_cost))

        choice = input('# ')

        if 'y' in choice:

            # Repair the item quality.
            pass

        elif 'n' in choice:
            print('Okay, going back to shop.')

            return 'shop'

        else:

            message_pop_up()
