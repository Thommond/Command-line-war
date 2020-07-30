from sys import exit  # importing neccessities
from textwrap import dedent
import items
import char


class Room(object):  # a parent of all rooms

    def enter(self):
        print(dedent("""Sorry this level is still under construction. We
        apoligize for any inconvience we have caused you. Have a good day! """))
        exit(1)


class Death(Room):  # when you are killed in the game
    def enter(self):
        print("You died a soldiers death that is all that matters.")
        exit(1)

class Battle(Object):
    """Battles class manages each attack for each battle of the game."""

    def attack(attacker_name, attackers_weapon_damage, victims_health, victims_name):

        # One in one hundred chance player or enemy will deal double damage.
        if randint(1, 100) == 54:
            victims_health - (attackers_weapon_damage * 2)
        else:
            victims_health - attackers_weapon_damage


        print("{}'s health is down to {} because of an attack by {}.'".format(victims_name, victims_health, attackers_name ))

class LevelOneIntro(Room):  # child of room first room of the entire game
    def enter(self):
        print(dedent("""
        Welcome! soldier what is your name?
        """))
        user = char.Player(input('# '))

        if user.name == 'Brian':
            return "completed"

        else:

            print(dedent(f"Okay, {} you have been drafted!".format(user.name)))
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
            print("hey that's not right say 'yes' ")

            return "sgt's_office"

class War_path(object):
    """docstring for War_path."""

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
            # Random  options for loosing 5 ration, gaining 20 extra bullets, and getting some chocholate.
        if 'B' in choice:
            # You loose a ration for talking back to sgt.
        if 'C' in choice:
            # You loose nothing and gain nothing.
        if 'D' in choice:
            # You gain 20 extra bullets because men at the range were so impressed.



class Map(object):  # all rooms in the game and communicates with the engine for the game functionality

    rooms = {
        "room": Room(),  # used to warn player of construction and parent of all other rooms
        "level_one_intro": LevelOneIntro(),  # start of level one
        "sgt's_office": SgtsOffice(),
        "sgt's_office_stats": SgtsOfficeStats(),
        "path_to_war": WarPath(),
        "ship": Ship(),
        "completed_level_one": CompletedOne(),  # End of level one

        # start of level two (currently under construction) they are here for the
        # names to be remebered for later construction
        #    "arrival at normandy": NormandyBeach(),
        #    "hell_on_beach": NormandyBeachHell(),
        #    "quick_and_easy": NormandySafePlace(),
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
        "completed": Completed(),   # completed the game
        "atomic_jepoardy": Jepoardy(),  # bonus round

        "death": Death(),  # dead
        "discharged": Discharged()  # dead in the game but different name
    }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.rooms.get(room_name)
        return val

    def first_room(self):
        return self.next_room(self.start_room)
