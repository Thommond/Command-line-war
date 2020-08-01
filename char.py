from random import randint
from textwrap import dedent
import items

# Player class manages the players info such as name and what items he/she has.
class Player(object):

    player_inventory = {

    "rations": items.rations,
    "rifle": items.rifle,
    "gas_mask": items.gas_mask,

    }


    def __init__(self, saved_room, health, name='Joe'):
        self.saved_room = saved_room
        self.health = health
        self.name = name


    def inventory(newItem):
        """Inventory checks to make sure the player does not have more than 7 items"""
        if len(player_inventory) == 7:
            return dedent("You already have the maximum of 7 items in your inventory, looks like you will need to get rid of an item to get {}".format(newItem))

    def eating(self, health_addition):
        """Calculating player health additions depending the food"""

        if self.health == 100:
            return print(dedent("You are at full health you do not need nourishment from a {}!".format(health_addition)))

        else:

            self.health += health_addition
            if self.health > 100:
                self.health = 100

            return print(dedent("Your health is now {}".format(health)))

class Enemy(Player):
    """Enemies are characters the player battles, they clash with
    weapons, and math."""
    def __init__(self, weapon, health, name, boss=False):
        self.weapon = weapon
        super().__init__(health, name)
        self.boss = boss


    def boss():
        if self.boss == True:
            # TODO: Boss eats to gain health every 3 moves
            pass
