from random import randint
from textwrap import dedent

# Player class manages the players info such as name and what items he/she has.
class Player(object):
    def __init__(self, name):
        self.name = name
        health = 100
        player_items = {

        gas_mask: False,
        rifle: True,

        }

    def inventory(newItem):
        """Inventory checks to make sure the player does not have more than 3 items"""
        if len(player_items) == 3:
            return dedent("You already have 3 items in your inventory, looks like you will need to get rid of an item to get {}".format(newItem))

    def eating(health_addition):
        """Calculating player health additions depending the food"""

        if health == 100:
            return dedent("You are at full health you do not need nourishment from a {}!".format(health_addition))

        else:
            health += health_addition
            if health > 100:
                health = 100

            return dedent("Your health is now {}".format(health))

    def battle(attackers_weapon_damage, attackers_health):

        """Manages the battle and checks if player is dead or enemy is dead."""

        pass
