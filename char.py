from random import randint
from textwrap import dedent
import items

# Player class manages the players info such as name and what items he/she has.
class Player(object):
    def __init__(self, name='Joe'):
        self.name = name
        health = 100

    def inventory(newItem):
        """Inventory checks to make sure the player does not have more than 7 items"""
        if len(player_inventory) == 7:
            return dedent("You already have the maximum of 7 items in your inventory, looks like you will need to get rid of an item to get {}".format(newItem))

    def player_inventory(self):

            player_inventory = {
            "gas_mask": False,
            "rifle": True,
            "rations": items.rations
            }

            return player_inventory.keys()

    def player_history(self):

            players_history = {
            # If a room is true the player has been completed the room if
            # false they are currently in it or need to complete it
            "intro" : True,
            }

    def eating(self, health_addition):
        """Calculating player health additions depending the food"""

        if health == 100:
            return print(dedent("You are at full health you do not need nourishment from a {}!".format(health_addition)))

        else:
            health += health_addition
            if health > 100:
                health = 100

            return print(dedent("Your health is now {}".format(health)))
