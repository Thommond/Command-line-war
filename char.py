from random import randint
from textwrap import dedent
import map
import items

class Player(object):
    """The player class manages all methods and attributes with
    the main character the user is playing."""

    def __init__(self, saved_room, next_room, health, name=False):
        self.saved_room = saved_room
        self.next_room = next_room
        self.health = health
        self.name = name

    # What the player currently is "holding"
    player_inventory = {
        "rations": items.rations.quantity,
        "rifle": items.rifle.quality,
        "hands": items.hands.quality,
    }

    def add_to_inventory(self, newItem):

        """Inventory checks to make sure
        (hands do not count thats why 7)
        the player does not have more than 7 items"""

        if len(self.player_inventory) >= 8:
            print("""You already have the maximum of 7 items in your inventory,
            looks like you will need to get rid of an item to get {}""".format(newItem.name))

            print("Would you like to get rid of an item to add the {} to your inventory?".format(newItem.name))

            if 'yes' in choice:
                dropping = player_inventory.drop()
                print(dedent('Okay, {} was removed from your inventory.'.format(item_name)))

            elif 'no' in choice:
                print(dedent('Okay redirecting you back to shop.'))
                return False

            else:
                print(dedent('Seems like you did not make a valid choice, aborting ...'))
                return False

        else:

            if newItem.type == "food":
                self.player_inventory[newItem.name] = newItem.health_addition
            elif newItem.type == "weapon":
                self.player_inventory[newItem.name] = newItem.quality

            print(dedent("""
            ##############################################
            Nice, the {} has been added to your inventory!
            """.format(newItem.name)))

    def check_inventory(self):

        invent_val = [i for i in self.player_inventory.values()]
        invent_name = [i for i in self.player_inventory.keys()]


        print(dedent("""
        Below are the contents of your inventory!!!
        ______________________________________________________________
        Name         | If weapon or item then 'Quality' and if food 'Quantity'
        """))

        for val in range(0, len(invent_name)):

            print(dedent("""
            #################################################
            #{}                 ## {}
            #################################################
            """.format(invent_name[val], invent_val[val])))



    def drop(self, validated=False):

        if validated == False:
            valid_item = items.find_item(map.user)

            if valid_item:

                item = self.get_player_item_val(valid_item.name, map.user)

                if item:
                    self.player_inventory.pop(valid_item.name)
                    print(dedent('The {} has been removed from your inventory.'.format(valid_item.name)))
                else:
                    map.message_pop_up(dedent('Not a valid item, try again.'))
                    return item
            else:
                map.message_pop_up(dedent('Not an item, try again.'))
                return valid_item
        else:
            self.player_inventory.pop(valid_item.name)
            print(dedent('The {} has been removed from your inventory.'.format(valid_item.name)))



    def add_to_player_health(self):

        """Calculating player health
        additions depending the food"""

        if self.health == 100:
            return print(dedent("You are at full health you do not need nourishment."))

        else:

            valid_food = items.find_item(map.user, desired_type="food")

            if valid_food:
                food = map.user.get_player_item_val(valid_food.name, map.user)

                if food:

                    if food == 1:

                        dropping = player_inventory.drop(validated=True)

                    elif food > 1:
                        self.health += valid_food.health_add
                        food -= 1

                    if self.health > 100:
                       self.health = 100

            return print(dedent("Your health is now {}".format(self.health)))

    def attack(self, weapon, victim):

        if map.user != victim:
            weap_quality = self.get_player_item_val(weapon.name, map.user)

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
            # IDEA: Should there be limit on flee?
            if randint(1, 4) == 3:
                return False
            else:
                return "Well looks like your escape attempt failed."
        else:
            return "Please choose either 'A' or 'B'"

    def get_player_item_val(self, choice_of_item, user):

        """This function only is called after the validation by find_item
        This function retrieves the val in player_inventory."""

        for key in user.player_inventory:

            if choice_of_item == key:
                return user.player_inventory[key]

        return False


class Enemy(Player):

    """Enemies are characters the player battles, they clash with
    weapons, and math."""

    def __init__(self, health, name, boss=False):
        super().__init__(self, health, health, name)
