import map
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
    enemies and various other tasks."""

    def __init__(self, damage, name, quality, ration_rate, type=False):
        self.damage = damage
        super().__init__(name, quality, ration_rate, type)

    def check_quality(item):

        """Notifies player of their weapons quality
        status and passes values to battle in the player class."""

        if item.quality == None:
            return "This item does not have a quality."

        elif item.quality == 0:
            return 'Your weapon is broke!!'

        elif item.quality < 3:
            return """Quality is {} remember to either repair or
            replace your weapons soon!""".format(weapon.quality)

        else:
            return """Looks like your weapon is a-okay.
            Your weapon quality is {}""".format(item.quality)


class Foods(Items):

    """Food heals or gives extra abilites to a player."""

    def __init__(self, health_add, quantity, name, ration_rate, type=False):
        self.health_add = health_add
        self.quantity = quantity
        super().__init__(name, ration_rate, ration_rate, type)

#   Weapons
rifle = Weapons(2.5, "rifle", 20, 4, "weapon")

hands = Weapons(.5, "hands", 100, 0, "weapon")

german_sniper = Weapons(10, "sniper", 12, 20, "weapon")

mp40 = Weapons(5, "mp40", 18, 17, "weapon")

glock = Weapons(3, "glock", 30, 10, "weapon")

german_pistol = Weapons(4, "g-pistol", 25, 10, "weapon")

machine_gun = Weapons(5, "machine_gun", 15, 12, "weapon")

bazooka = Weapons(25, "bazooka", 5, 100, "weapon")

grenade = Weapons(30, "grenade", 1, 25, "weapon")

shot_gun = Weapons(20, "shot_gun", 12, 20, "weapon")

# Food
rations = Foods(5, 10, "rations", 1, "food")

chocolate = Foods(20, 1, "chocolate", 5, "food")

meth = Foods(30, 1, "meth", 7, "food")


list_of_items = {
    "weapons": {

    "bazooka": bazooka,
    "german_pistol": german_pistol,
    "glock": glock,
    "hands": hands,
    "machine_gun": machine_gun,
    "rifle": rifle,
    "sniper": german_sniper,
    "grenade": grenade,
    "shot_gun": shot_gun,

    },

    "food": {

    "choc": chocolate,
    "rations": rations,
    "meth": meth

    }
};

def find_item(user, name=False, desired_type=False, buying=False):

    """Loops through all items to make sure p
    layer string input is an actual item from the game.
    And checks if they have that item in the inventory.
    Finally returns the item if it matches the desired type."""

    if not name:
        print(dedent("""
        What is the items name?
        """))

        item_name = input('# ')

    else:
        item_name = name

    if not desired_type:

        print(dedent("""
        What type of item is this?

        Note: (Type out full anwser not letter.)

        A. weapon

        B. food
        """))

        item_type = input('# ')
    else:
        item_type = desired_type

    for category in list_of_items.values():
            for item in category.values():
                if item.name in item_name:

                    if buying != True:
                        if item.type in item_type:
                            if item.name in user.player_inventory:
                                return item
                    else:
                        if item.type in item_type:
                            return item


    return False

def repair_items(user):

    """Updating the users weapon or
    items to restore to default."""

    item = find_item(user)

    if item == False:
        print(dedent('Looks like that is not an item, or it is not in your inventory.'))

    elif item.type == "food" or item.name == "hands":
        map.message_pop_up(dedent("""
        This item cannot be repaired this
        usually means you selected a food or your hands.
        """))

    else:

        cost = int(item.ration_rate / 4)
        print(dedent("""
        So you want to repair the {}, for {}?
        (Type yes to continue)
        """.format(item.name, cost)))

        choice = input('# ')

        if 'y' in choice:
            rations = map.user.get_player_item_val("rations", user)
            player_item = map.user.get_player_item_val(item.name, user)

            if rations >= cost:
                rations -= cost
                player_item = item.quality
                print(dedent("""
                Your {} has been repaired at cost of {} and
                now has a quality of {}. You have now have {}
                rations.
                """.format(item.name, cost, item.quality, rations)))

            else:
                print(dedent('Sorry you do not have enough rations.'))

        elif 'n' in choice:
            print(dedent('Okay, going back to shop.'))

        else:
            map.message_pop_up(dedent("""
            Please choose to repair
            or not repair your weapon.
            """))

def buy_items():

    print(dedent(
    """
    If you do not know name and type of item then type 'list'.
    (Expand terminal list is big!)

    other wise press enter to continue
    """
    ))

    choice = input('# ')

    if 'list' in choice:
        list_items()

    item = find_item(map.user, buying=True)

    if item:
        rations = map.user.get_player_item_val('rations', map.user)
        in_invent = map.user.get_player_item_val(item.name, map.user)

    else:
        print(dedent('Make sure to type in proper item name and type.'))
        return False

    if in_invent is not False:
        print(dedent("""
        That weapon is already in your inventory you cant have two!
        """))
        return False

    print(dedent("""
    You would like to buy the {} for
    {} rations?
    """.format(item.name, item.ration_rate)))

    choice = input('# ')

    if 'y' in choice:

        if rations >= item.ration_rate:
            rations -= item.ration_rate
            transaction = map.user.add_to_inventory(item)
            print(dedent("""
            Purchase success! You now have the {}
            in your inventory. You now have {} rations.
            """.format(item.name, rations)))

        else:
            print(dedent("""
            Looks like you do not have enough rations!
            """))
            return False

def sell_items():
    valid_item = find_item(map.user)
    rations = map.user.get_player_item_val('rations', map.user)
    if valid_item:
        item = map.user.get_player_item_val(valid_item.name, map.user)
        if item:
            map.user.player_inventory.pop(valid_item.name)
            rations += valid_item.ration_rate / 2
            print(dedent("""
            The {} has been sold successfully!
            You now have a total of {} rations.
            """.format(valid_item.name, rations.quantity)))
        else:
            map.message_pop_up(dedent('Not a valid item, try again.'))
            return False
    else:
        map.message_pop_up(dedent('Not a valid item, try again.'))



def list_items():

    print(dedent('Warning! This list will be large, type enter to continue'))


    choice = input('# ')

    print(dedent("""
                #                       #
    Type        #      item             #
    #####################################
    """))

    for category in list_of_items.values():

        for item in category.values():

            print(dedent("""
            ##############################
            {}        #{}
            ##############################
            """.format(item.type, item.name)))
    yes = True

    while yes:

        print(dedent("""
        Would you like to look into the details of an item?

        Press enter for yes and type 'no' if not
        """))

        choice = input('# ')

        if 'no' in choice:
            break

        item_choice = find_item(map.user, buying=True)

        if item_choice:

            if item_choice.type == 'weapon':

                print(dedent("""

                Details of the {}
                ########################
                Damage  | {}
                ########################
                Quality | {}
                ########################
                Ration_rate | {}

                """.format(item_choice.name, item_choice.damage,
                item_choice.quality, item_choice.ration_rate)))

            elif item_choice.type == 'food':

                print(dedent("""

                Details of the {}
                ########################
                Quality | {}
                ########################
                Ration_rate | {}

                """.format(item_choice.name,
                item_choice.quality, item_choice.ration_rate)))

        else:
            print(dedent('That is not an item or you mistyped a piece of info. Feel free to try again.'))
