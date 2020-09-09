from random import randint
from textwrap import dedent
import map
import items


# Player class manages the players info such as name and what items he/she has.

player_inventory = {

"rations": items.rations,
"rifle": items.rifle,
"gas_mask": items.gas_mask,
"hands": items.hands,

}

class Player(object):

    def __init__(self, saved_room, health, name=False):
        self.saved_room = saved_room
        self.health = health
        self.name = name

    def add_to_inventory(self, newItem):

        """Inventory checks to make sure
        the player does not have more than 7 items"""

        if len(player_inventory) == 7:
            return map.message_pop_up("""You already have the maximum of 7 items in your inventory,
            looks like you will need to get rid of an item to get {}""".format(newItem))

        else:
            player_inventory[newItem.name] = newItem
            print(dedent("""Nice {} has been added to your inventory!""".format(newItem.name)))

    def add_to_player_health(self, health_addition):

        """Calculating player health
        additions depending the food"""

        if self.health == 100:
            return print(dedent("You are at full health you do not need nourishment from a {}!".format(health_addition)))

        else:
            # Add the health addition
            self.health += health_addition

            if self.health > 100:
                self.health = 100

            return print(dedent("Your health is now {}".format(self.health)))

    # TODO: Make sure to increase and decrease weapon quality each attack.
    def attack(self, weapon, victim):

        # Checking if weapon broke / 1 out of 20 chance if not hands as weapon
        if weapon.quality == 0 or range(1, 20) == 12 and weapon.name != 'hands':
            print(dedent("Oh no looks like {}'s {} broke!!".format(self.name, weapon.name)))
            # TODO: Have a my_weapon argument where values change from default.

        # One in one twenty chance player or enemy will deal double damage.
        if randint(1, 10) == 4:
            victim.health -= (weapon.damage * 2)
            print("Oh no double damage!")
            print("{}'s health is down to {} because of an attack by {} with {} as their weapon.".format(victim.name, victim.health, self.name, weapon.name))

        else:
            victim.health -= weapon.damage
            print(dedent("{}'s health is down to {} because of an attack by {} with {} as their weapon".format(victim.name, victim.health, self.name, weapon.name)))
        # TODO: Right now it prints with enemy attack aswell make so it only
        # prints with the user.
        if map.user == victim:
            print(dedent("""
            Looks like {} attacked you. What will you do?

            A. Attack back using a weapon from your inventory.

            B. Try to escape.
            """.format(self.name)))
        else:
            print('...')


    def attack_choice(self, user_choice, enemy, enemy_weapon):
        # Checking users choice (To limit if/else clogging map.py)
        if 'A' in user_choice:
            return "What weapon do you want to use?"

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
