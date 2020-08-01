from random import randint
from textwrap import dedent
import items

# Player class manages the players info such as name and what items he/she has.
class Player(object):

    player_inventory = {
        "gas_mask": False,
        "rifle": True,
        "rations": items.rations
    }

    health = 100

    saved_room = "level_one_intro"

    def __init__(self, name='Joe'):
        self.name = name

    def inventory(newItem):
        """Inventory checks to make sure the player does not have more than 7 items"""
        if len(player_inventory) == 7:
            return dedent("You already have the maximum of 7 items in your inventory, looks like you will need to get rid of an item to get {}".format(newItem))

    def eating(self, health_addition):
        """Calculating player health additions depending the food"""

        if health == 100:
            return print(dedent("You are at full health you do not need nourishment from a {}!".format(health_addition)))

        else:
            health += health_addition
            if health > 100:
                health = 100

            return print(dedent("Your health is now {}".format(health)))
