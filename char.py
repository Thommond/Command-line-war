from random import randint
from textwrap import dedent
import map
import items

class Player(object):
    """The player class manages all methods and attributes with
    the main character the user is playing."""
    def __init__(self, saved_room, health, name=False):
        self.saved_room = saved_room
        self.health = health
        self.name = name

    # What the player currently is "holding"
    player_inventory = {
        "rations": items.rations.quantity,
        "rifle": items.rifle.ration_rate,
        "gas_mask": items.gas_mask,
        "hands": items.hands.quality,
    }

    def add_to_inventory(self, newItem):

        """Inventory checks to make sure
        the player does not have more than 7 items"""

        if len(self.player_inventory) == 7:
            print("""You already have the maximum of 7 items in your inventory,
            looks like you will need to get rid of an item to get {}""".format(newItem.name))

            print("Would you like to get rid of an item to add the {} to your inventory?".format(newItem.name))
            choice = input('# ')

            if 'y' in choice:
                # TODO: Create drop method.
                dropping = player_inventory.drop(item_name)
                print(dedent('Okay, {} was removed from your inventory.'))

            if 'n' in choice:
                print(dedent('Okay redirecting you back to shop.'))
                return False

            else:
                print(dedent('Seems like you did not make a valid choice, aborting ...'))
                return False

        else:
            self.player_inventory[newItem.name] = newItem
            print(dedent("""Nice {} has been added to your inventory!""".format(newItem.name)))

    def check_inventory(self):

        inventory = ", ".join(self.player_inventory.keys())
        print(dedent("""
        #####################################################################
        Time to take a look in my bag. I have a {} and thats it.""".format(inventory)
        ))

    def add_to_player_health(self, health_addition):

        """Calculating player health
        additions depending the food"""

        if self.health == 100:
            return print(dedent("You are at full health you do not need nourishment from a {}!".format(health_addition)))

        else:

            self.health += health_addition

            if self.health > 100:
                self.health = 100

            return print(dedent("Your health is now {}".format(self.health)))

    def attack(self, weapon, victim):

        if map.user != victim:
            weap_quality = items.get_player_item_val(weapon.name, map.user)

            if weap_quality <= 0:
                return 'Your weapon is broken, looks like you forfit this move.'

        if range(1, 20) == 12 and weapon.name != 'hands':
            print(dedent("Oh no looks like {}'s {} broke!!".format(self.name, weapon.name)))

        if randint(1, 10) == 4:
            victim.health -= (weapon.damage * 2)
            print("Oh no double damage!")
            print("{}'s health is down to {} because of an attack by {} with {} as their weapon.".format(victim.name, victim.health, self.name, weapon.name))

        else:
            victim.health -= weapon.damage
            print(dedent("{}'s health is down to {} because of an attack by {} with {} as their weapon".format(victim.name, victim.health, self.name, weapon.name)))

        if map.user == victim:
            print(dedent("""
            Looks like {} attacked you. What will you do?

            A. Attack back using a weapon from your inventory.

            B. Try to escape.
            """.format(self.name)))
        else:
            weap_quality -= 1
            print('Weapon quality decreased by one, to {}'.format(weap_quality))
            print('...')

    def attack_choice(self, user_choice):

        """Checking the users choice to
         limit if/else nesting"""

        if 'A' in user_choice:
            return 'What is the name of your item?'

        elif 'B' in user_choice:
            if randint(1, 4) == 3:
                return False

            else:
                return "Well looks like your escape attempt failed."
        else:
            return "Please choose either 'A' or 'B'"


class Enemy(Player):

    """Enemies are characters the player battles, they clash with
    weapons, and math."""

    def __init__(self, health, name, boss=False):
        super().__init__(self, health, name)
        self.boss = boss
