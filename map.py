from sys import exit  # importing neccessities
from textwrap import dedent
import items
import char


class Room(object):
    """Parent of all room objects and used for underconstruction features."""

    def enter(self):
        print(dedent("""Sorry this level is still under construction. We
        apoligize for any inconvience we have caused you. Have a good day! """))
        exit(1)

class Endings(Room):
     """All ending scenarios in one class as methods"""

     def death():
        print("You died a soldiers death that is all that matters.")
        exit(1)

     def discharged():
        print(dedent("""You got discharged from the military!!
        You got caught breaking the rules and you loose the privlage to serve."""))
        exit(1)

     def completed_game():

        if randint(1, 10) == 3:
            ending_scene = """get shot by a crafty german sniper on the way back to base camp. Your
            cold dead corpse never leaves the french country side. Your wife will never know if you
            are KIA or POW.

            THE END"""

        elif randint(1, 10) == 2:
            ending_scene = """your last battle was fought near the effiel tower, you took a few hits
            and are now listed as medically warrented to go home. You will finally get to see your baby
            boy.

            THE END"""

        elif randint(1, 10) == 7:
            ending_scene = """battle almost a year longer until all german's are gone of the
            country side and you meet with Russian forces. You love your family, but you fight
            for your country. After you are dismissed from duty and given a reward, your wife notifies
            you of divorce.

            THE END"""
        else:
            ending_scene = """are sent home with gratitude and pride. Finally your fight is over
            and your family only had to wait for 3 months."""

        print(dedent("""You have been through it all. You prepared for war, played some
        games and got the nerves. You have stormed the beachs of France, battled men and
        helped men. And after all your struggles and all your efforts you {}""".format(ending_scene)))


class Battle(object):
    """Battles class manages each attack for each battle of the game."""

    def attack(attacker_name, attackers_weapon_damage, victims_health, victims_name):

        # One in one twenty chance player or enemy will deal double damage.
        if randint(1, 20) == 11:
            victims_health - (attackers_weapon_damage * 2)
        else:
            victims_health - attackers_weapon_damage

        print("{}'s health is down to {} because of an attack by {}.'".format(victims_name, victims_health, attackers_name ))

class Menu(object):

    def enter(self):
        print(dedent("""

        Welcome to the menu! How can I help you soldier?

        A. Rules and regulations

        B. Bartering stand and Repairs

        C. Inventory

        D. Quit the game (Note: No progress will be saved.)

        """))

        choice = input('# ')

        if 'A' in choice:
            return "menu_rules"
        if 'B' in choice:
            return "shop"
        if 'C' in choice:
            return "inventory_check"
        if 'D' in choice:
            return "quit"
        else:
            return "menu_enter"

    def shopping(self):
        print(dedent("""Welcome to the American depot soldier, or
        what they call jimmy's bartering stand. I can repair weapons, trade,
        and much more. What do you need?
        """))

    def inventory_checking(self, inventory_of_player):
        print(dedent("""Time to take a look in my bag. I have {}""".format(inventory_of_player)))

    def rules(self):
        print(dedent("""So here is the recap about some game rules.

        1. You are only allowed 7 item in your inventory, and food is included, but
        quantity of each item is not limited.

        2. You can shop in the store and rations are used as currency.

        3. Each weapon does damage and that will be displayed on each weapon.

        4. Every item has it's ration value so you can sell it to the shop for
        rations if you need an item.

        5. Once you make a choice you cannot go back unless you replay, so choose
        wisely.

        Notes: (Not rules but helpful info) Say "yes" to continue to tips or "no"
        to exit rules and go back to menu.
        """))

        choice = input('# ')

        if 'yes' in choice:
            print(dedent(
            """
            Here is some helpful info...

            1. Battles are math so always keep an eye on
            weapon damage, quality of the weapon and other inventory.

            2. Some things are randomized so do not be afraid to take a chance.

            3. Remember if you beat the game or not progress will not be saved.
            """
            ))

            return 'menu_enter'

        else:
            return 'menu_enter'

    def where_is_player(current_room_in_player_history):
        """Menu can be returned anywhere buy we need to keep track of where players room in the game is,
        this method communicates with user (Player instance) and menu_options (Menu instance)"""
        location_of_player = {

        }
        # Returning the index value which will be a string map can use to go back to the room they were at.
        for index in location_of_player:
            if current_room_in_player_history == index.keys():
                return index.values()


class LevelOneIntro(Room):  # child of room first room of the entire game
    def enter(self):
        print(dedent("""
        Welcome! soldier what is your name?
        """))

        choice = input('# ')

        user = Player(choice)

        if user.name == 'Brian':
            return "completed"

        else:

            print(dedent("Okay, {} you have been drafted!".format(user.name)))
            print(dedent("""Your family is worried sick. World war
            two is raging across europe, you turned 18 just
            weeks ago. The military needs extra troops on the
            ground agaist the Nazi's. The Nazi's have infested
            Europe like a cockroch colony. You will be assigned
            to Unit 179. """))

            print(dedent('Any thoughts before we move on?'))

            thoughts = input('# ')

            print(dedent("Okay, well you will now be sent to sgt's office for info and assignment."))

            return "sgt's_office"

class SgtsOffice(Room):  # selecting the stats of the game in this room
    def enter(self):
        print(dedent("""
        Welcome soldier I am here to give you the ropes.

        First things first, you want to make it out alive and safe home to your family.

        Number two is you have 100 starting health, overtime your health will go down due to
        exhaustion and battles.

        You start with 10 rations that is basic food, they give you a little boost of health, 10 health
        points to be exact. You can possibly find more food, and other health items on the way so be looking out!

        You also start with a basic american rifle, and you can get other guns and accessories later if you are
        smart. You start out like every soldier. Just a thing of note each weapon deals a certian amount of
        damage to opponents and other things like doors or items. To find out your weapons damage, quality or possibly
        ammo just go to your menu. You can also find out your health, info about the enemies types you meant, and
        more at the Menu.

        To get to menu you can simply text "Menu" in the command line then choose where in the menu you would like to
        go by texting that option.

        For more info you can go to the Sgt tips portion of the menu.

        Yeah, I know that was a lot did you get it all?
        """)) # TODO: Add menu, and all additions to menu so users can always access.

        choice = input('# ')

        if choice == 'yes':
            return "path_to_war"

        else:
            print(dedent("hey that's not right say 'yes' "))

            return "sgt's_office"

class WarPath(object):
    """ You get to choose your last recreational activity as a soldier before
    storming the beachs at normandy, France."""

    def enter(self):
        print(dedent(
        """Everything is in it's place, you are of to war. In one short day you and all
        your fellow soldiers will be loaded on to ship and headed for the invastion on normandy.

        You see a few things around your barracks, a group men playing cards, your sgt and others
        talking ops, your cozy bed and the range.

        What do you want to do for your last day in America?

        A. Play some cards

        B. Talk ops with Sgt

        C. Get some more rest

        D. Get more rifle practice.
        """
        ))

        choice = input('# ')

        if 'A' in choice:
            # Random opportunity's in poker ordered by most likely to least likely
            if randint(1, 4) == 3:
                print(dedent("""You played some poker, you won a thing or two, but got carried away. In the final round
                you bet it all. You fell right into the bluff of a fellow private and lost it all. You lost 7 rations."""))

            elif randint(1, 4) == 1:
                print(dedent("""You did pretty good for poker, you played fair and gained 5 rations"""))

            elif randint(1, 100) == 33:
                print(dedent("""Uh Oh! Your sgt caught you playing poker under the table,
                the group blames you. You are in big trouble."""))
                return 'discharged'

            elif randint(1, 1000) == 378:
                print(dedent("""Wow!!! Looks like you were in an all stakes game with a bazooka
                gunner. You won it all! You now have a bazooka in you midst."""))

            else:
                print(dedent("""your not to good at poker, you lost 2 rations for a bad round then you
                called it a night."""))

        elif 'B' in choice:

            print(dedent("""You talked a bit and had fun talking shop with the Sgt, but you
            took it a bit to far. You said some things you wish you didn't to Sgt and he took
            a ration away."""))

            char.rations

        elif 'C' in choice:
            print(dedent("""You curl up on your bed and deciede to relax for the next few hours. Your
            rest was quiet and comfortable. You are ready for battle."""))

        elif 'D' in choice:
            print(dedent("""You shoot almost five bullets right on the nose of the bullseye. The troop
            was so impress some gave you a few bullets. Your quality of your rifle was increased by 10 quality
            points."""))

        return  'ship'

class Ship(object):
    """On the 3 day trip to normandy beach final training and
    preperation before storming the beachs."""
    def enter(self):
        print(dedent("""
        All of you and your troop are loaded on to a ship labeled the USS great leap. For a 3 day journey
        to Nazi occupied France.

        """))




class Map(object):  # all rooms in the game and communicates with the engine for the game functionality

    types_of_endings = Endings()

    menu_options = Menu()

    rooms = {
        # For underconstruction peices of the game
        "room": Room(),

        # Start of level one
        "level_one_intro": LevelOneIntro(),
        "sgt's_office": SgtsOffice(),
        "path_to_war": WarPath(),
        "ship": Ship(),
        # "arrival at normandy": NormandyBeach(),
        # "hell_on_beach": NormandyBeachHell(),
        # "quick_and_easy": NormandySafePlace(),
        # "completed_level_one": CompletedOne(),  # End of level one

        # start of level two (currently under construction) they are here for the
        # names to be remebered for later construction
        #   \
        #    "damn_machine_gunner": DamnMachineGunner(),
        #    "ambush": AmbushFoxHole(),
        #    "captured": Captured(),
        #    "torcher": Torcher(),
        #    "afriend": Friend(),
        #    "rescued": Rescued(),
        #    "muddy": Muddy(),
        #    "clever_soldier": Clever(),
        #    "escaped_and_free": EscapedFree(),
        #    "enemy_lines": EnemyLines(),
        #    "evation": Evation(),
        #    "stay_quiet": StayQuiet(),
        #    "attic": Attic(),
        #    "rats": Rats(),
        #    "the_road": Road(),
        #    "to_paris": ToParis(),  # end of level two

        # Menu options
        "menu_enter": menu_options.enter(),
        "menu_rules": menu_options.rules(),
        "shop": menu_options.shopping(),
        "inventory_check": menu_options.inventory_checking(",".join(char.character.player_inventory.keys())),
        "quit": menu_options.quiting(),

        # Types of endings to the game.
        "completed": types_of_endings.completed(),
        "death": types_of_endings.death(),
        "discharged": types_of_endings.discharged()
    }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.rooms.get(room_name)
        return val

    def first_room(self):
        return self.next_room(self.start_room)
