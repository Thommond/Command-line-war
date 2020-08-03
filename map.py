from sys import exit  # importing neccessities
from textwrap import dedent
from random import randint
from char import Player, Enemy
import items


####################################
#### Map Class is at the bottom ####
####################################

user = Player("level_one_intro", 100)

# Useful global functions

def message_pop_up(message):
    print(dedent("""
    ######## IMPORTANT ########
    ###########################
    ###########################
    {}
    ###########################
    ###########################
    """.format(message)))


###                            ###
###  Ending rooms to the game  ###
###                            ###

class Room(object):
    """Parent of all room objects and used for underconstruction features."""

    def enter(self):

        print(dedent("""
        Sorry this level is still under construction. We
        apoligize for any inconvience we have caused you. Have a good day!
        """))
        exit(1)

class Death(Room):

    def enter(self):

        print("You died a soldiers death that is all that matters.")
        exit(1)

class Discharged(Room):

    def enter(self):

        print(dedent("""
        You got discharged from the military!!
        You got caught breaking the rules and you loose the privlage to serve.
        """))
        exit(1)

class Completed():

    def enter(self):

        rando = randint(1, 10)

        if rando == 3:
            ending_scene = """get shot by a crafty german sniper on the way back to base camp. Your
            cold dead corpse never leaves the french country side. Your wife will never know if you
            are KIA or POW.

            THE END"""

        elif rando == 2:
            ending_scene = """your last battle was fought near the effiel tower, you took a few hits
            and are now listed as medically warrented to go home. You will finally get to see your baby
            boy.

            THE END"""

        elif rando == 7:
            ending_scene = """battle almost a year longer until all german's are gone of the
            country side and you meet with Russian forces. You love your family, but you fight
            for your country. After you are dismissed from duty and given a reward, your wife notifies
            you of divorce.

            THE END"""
        else:
            ending_scene = """are sent home with gratitude and pride. Finally your fight is over
            and your family only had to wait for 3 months."""

        print(dedent("""
        You have been through it all. You prepared for war, played some
        games and got the nerves. You have stormed the beachs of France, battled men and
        helped men. And after all your struggles and all your efforts you {}""".format(ending_scene)))
        exit(1)

########################
## Menu Options rooms ##
########################

class Menu(Room):

    def enter(self):
        print(dedent("""
        #####################################################################
        Welcome to the menu! How can I help you soldier?

        A. Rules and regulations

        B. Bartering stand and Repairs

        C. Inventory

        D. Quit the game (Note: No progress will be save.)

        E. Back to game

        """))

        choice = input('# ')

        if 'A' in choice:
            return 'menu_rules'

        elif 'B' in choice:
            return "shop"

        elif 'C' in choice:
            return "inventory_check"

        elif 'D' in choice:
            return "quit"

        elif 'E' in choice:

            return user.saved_room

        else:
            message_pop_up(" You have to choose from the letters to get an option")
            return "menu_enter"


class Shop(Room):
    def enter(self):

        print(dedent("""
        #####################################################################
        Welcome to the American depot soldier, or
        what they call jimmy's bartering stand. I can repair weapons, trade,
        and much more. What do you need?

        A. Repair an item.

        B. Buy a item

        C. Sell items for rations

        D. Back to menu

        """))

        choice = input("# ")

        if 'A' in choice:
            print(dedent('Okay what weapon do you need repaired?'))
            # TODO: make a repair room
            return 'room'
        elif 'B' in choice:
            print(dedent('Okay what item would you like to buy?'))
            # TODO: make a store room
            return 'room'
        elif 'C' in choice:
            print(dedent('Okay, what item or items would you like to sell?'))
            # TODO: Make a sell room
            return 'room'
        elif 'D' in choice:
            print(dedent('Redirecting back to menu.'))
            return "menu_enter"

        else:
            message_pop_up("""
            Please choose an option.
            """)
            return "shop"


class Inventory(Room):
    """Tells users there inventory at the requested time."""

    def enter(self):
        inventory = ", ".join(user.player_inventory.keys())
        print(dedent("""
        #####################################################################
        Time to take a look in my bag. I have a {} and thats it.""".format(inventory)))

        return "menu_enter"

class Rules(Room):
    """Displays the rules of the game."""
    def enter(self):

        print(dedent("""
        #####################################################################
        So here is the recap about some game rules.

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
            #####################################################################
            Here is some helpful info...

            1. Battles are math so always keep an eye on
            weapon damage, quality of the weapon and other inventory.

            2. Some things are randomized so do not be afraid to take a chance.

            3. Remember if you beat the game or not progress will not be saved.

            (Note: type yes to read the rules again, if you do not want to then simply press enter.)
            """
            ))
            choice = input("# ")

            if 'yes' in choice:

                return 'menu_rules'

            else:
                return 'menu_enter'


        else:
            print("Okay, thanks for reading the rules, you are now back at menu.")
            return 'menu_enter'

class Quit(Room):

    def enter(self):

        message_pop_up("""
        Are you sure you want to quit? You made it so far! Remember
        no progress will be saved. (Type yes to quit and no to go back to menu.)""")

        choice = input("# ")

        if 'yes' in choice:
            print(dedent("Good bye."))
            exit(0)
        if 'no' in choice:
            print(dedent('Redirecting back to menu......'))
            return 'menu_enter'
        else:
            print(dedent('To quit please type "yes" into the terminal'))
            return 'quit'

#########################
## End of Menu options ##
#########################


## Start of play through rooms! ##
#--------------------------------#


class LevelOneIntro(Room):  # child of room first room of the entire game
    def enter(self):
        print(dedent("""
        Welcome! soldier what is your name?
        """))

        user.name = input('# ')

        if user.name == 'Brian':
            return "completed"

        else:

            print(dedent("Okay, {} you have been drafted!".format(user.name)))
            print(dedent("""
            Your family is worried sick. World war
            two is raging across europe, you turned 18 just
            weeks ago. The military needs extra troops on the
            ground agaist the Nazi's. The Nazi's have infested
            Europe like a cockroch colony. You will be assigned
            to Unit 179.
            """))

            return "sgt's_office"

class SgtsOffice(Room):
    def enter(self):

        """Introduction to the game. Telling the rules to the player
        so they get the jist. (That is why it is quite lengthy)"""

        user.saved_room = "sgt's_office"

        print(dedent("""
        Welcome soldier I am here to give you the ropes.
        (Enter to continue)
        """))

        input('# ')

        print(dedent("""
        First things first, you want to make it out alive and safe home to your family.
        """))

        input('# ')

        print(dedent("""
        Number two is you have 100 starting health, overtime your health will go down due to
        exhaustion and battles.
        """))

        input('# ')

        print(dedent("""
        You start with 10 rations that is basic food, they give you a little boost of health, 10 health
        points to be exact. You can possibly find more food, and other health items on the way so be looking out!
        """))

        input('# ')

        print(dedent("""
        You also start with a basic american rifle, and you can get other guns and accessories later if you are
        smart. You start out like every soldier. Just a thing of note each weapon deals a certian amount of
        damage to opponents and other things like doors or items. To find out your weapons damage, quality or possibly
        ammo just go to your menu. You can also find out your health, info about the enemies types you meant, and
        more at the Menu.
        """))

        input('# ')

        print(dedent("""
        To get to menu you can simply text "menu" in the command line then choose where in the menu you would like to
        go by texting that option. The menu option is avaliable at the begining of each room before you make a choice.
        """))

        input('# ')

        print(dedent("""
        For more info you can go to the Rules portion of the menu.
        """))

        input('# ')

        print(dedent("""
        Yeah, I know that was a lot did you get it all?
        (Type yes to continue)
        """))

        choice = input('# ')

        if 'menu' in choice:
            return 'menu_enter'

        if 'yes' in choice:

            return "path_to_war"

        else:
            print(dedent("hey that's not right say 'yes' to contine or 'menu to go to the menu'"))

            return "sgt's_office"

class WarPath(Room):
    """ You get to choose your last recreational activity as a soldier before
    storming the beachs at normandy, France."""

    def enter(self):

        user.saved_room = 'path_to_war'

        print(dedent(
        """
        Everything is in it's place, you are off to war. In one short day you and all
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

        if 'menu' in choice:

            return 'menu_enter'

        elif 'A' in choice:
            # Random opportunity's in poker ordered by most likely to least likely
            rando = randint(1, 4)
            if rando == 3:
                print(dedent("""
                You played some poker, you won a thing or two, but got carried away. In the final round
                you bet it all. You fell right into the bluff of a fellow private and lost it all. You lost 7 rations."""))
                items.rations.quantity -= 7
                print(dedent("You now have only {} rations.".format(items.rations.quantity)))

            elif rando == 1:
                print(dedent("""
                You did pretty good for poker, you played fair and gained 5 rations"""))
                items.rations.quantity += 5
                print(dedent("You now have {} rations.".format(items.rations.quantity)))

            elif randint(1, 100) == 33:
                print(dedent("""
                Uh Oh! Your sgt caught you playing poker under the table,
                the group blames you. You are in big trouble."""))

                return 'discharged'

            elif randint(1, 1000) == 378:
                print(dedent("""
                Wow!!! Looks like you were in an all stakes game with a bazooka
                gunner. You won it all! You now have a bazooka in you midst."""))
                # TODO: Add bazooka to inventory

            else:
                print(dedent("""
                Your not to good at poker, you lost 2 rations for a bad round then you
                called it a night."""))
                items.rations.quantity -= 2
                print(dedent("You now have only {} rations".format(items.rations.quantity)))

        elif 'B' in choice:

            print(dedent("""
            You talked a bit and had fun talking shop with the Sgt, but you
            took it a bit to far. You said some things you wish you didn't to Sgt and he took
            a ration away."""))

            items.rations.quantity -= 1

        elif 'C' in choice:
            print(dedent("""
            You curl up on your bed and deciede to relax for the next few hours. Your
            rest was quiet and comfortable. You are ready for battle."""))


        elif 'D' in choice:
            print(dedent("""
            You shoot almost five bullets right on the nose of the bullseye. The troop
            was so impress some gave you a few bullets. Your quality of your rifle was increased by 10 quality
            points."""))

            items.rifle.quality += 10
            print(dedent(
            "Your rifles quality is now {}, great choice.".format(items.rifle.quality)
            ))
        else:
            message_pop_up('Please select a choice from the letters.')
            return 'path_to_war'

        return  'ship'

class Ship(Room):
    """On the 3 day trip to normandy beach final training and
    preperation before storming the beachs."""
    def enter(self):

        user.saved_room = 'ship'

        print(dedent("""
        You and all your troop are loaded on to a ship labeled the USS great leap. For a 3 day journey
        to Nazi occupied France. You are training on deck, going through drills and wishing you were home.
        But, you have a duty and that is to America.
        """))

        input('# ')

        print(dedent("""
        You are walking up the stairs from your room, to the deck to catch a glimpse of the
        sky. However, you hear some ruckus on the deck. Seems like some of you fellow army men
        are in a fight!!
        """))
        print(dedent("""
        "I will fucken kill you, you god damn ration theif" shouted Timothy.
        """))

        input('# ')

        print(dedent("""
        "Yeah, I did not steal your rations you damn tweeker. Fuck off before I
        lay a punch on ya." said Jimmy
        """))

        input('# ')

        print(dedent("""
        "You lying sack of shit!" said Timothy with rage in his vains.
        """))

        input('# ')

        print(dedent("""
        "Alright, thats it..." said Jimmy
        """))

        print(dedent("""
        "Jimmy lays a punch and then Timothy. The fight starts to get rough.
        What will you do?

        A. Try to stop Jimmy by talking sense to the crowd.

        B. Stand up for Timothy and fight Jimmy.

        C. Watch the fight to see who wins.

        D. Go back to your room.
        "
        """))

        choice = input('# ')

        ship_mate = Enemy(10, "Jimmy")

        if 'menu' in choice:
            return 'menu_enter'

        elif 'eat' in choice:
            pass

        elif 'A' in choice:
            print(dedent("""
            You had the crowds attention for a a little while, but Jimmy did
            not want to listen to your words. He knocked you out cold. You loose 10
            health.
            """))

            user.health -= 10

        elif 'B' in choice:
            print(dedent(
            """
            You say "Hey, Jimmy". You kick his shin and he falls to the ground.
            Everyone looks at you. Jimmy stares with rage.
            """
            ))

            while ship_mate.health or user.health != 0:

                ship_mate.attack(items.hands, user)

                choice = input('# ')

                user.attack_choice(choice, ship_mate, item.hands)

                choice = input('# ')

                is_it_an_item? =  items.find_item(choice)

        elif 'C' in choice:
            print(dedent("""
            You take a seat on the side of the deck and watch Jimmy completly pound
            on Timothys face. Everyone else left in a hurry when they saw sgt. But you
            stayed. Your sgt's response is...
            """))

            input('# ')

            return 'discharged'

        elif 'D' in choice:

            print(dedent(
            """
            You hurry back to your room. Just in time to catch Kyle in action, harboring
            two glocks. You say "Hey, kyle I know we are not suppose to have those looks
            like there is one for me and you."
            """
            ))

            input('# ')

            print(dedent(
            """
            "Okay, {} I will give you one. But hush up these guns are not invented yet."
            """))

            user.player_inventory["glock"] = items.glock

        return "arrival_at_normandy"

class NormandyBeach(Room):
    """First landing at france. Our player has to navigate through
    decisions of death."""

    def enter(self):

        user.saved_room = 'arrival_at_normandy'

        return 'room'


##########################################
#### Map Class runs through all rooms ####
####^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^######

class Map(object):

    rooms = {
        "room": Room(),

        # Menu options
        "menu_enter": Menu(),
        "menu_rules": Rules(),
        "shop": Shop(),
        "inventory_check": Inventory(),
        "quit": Quit(),

        # Types of endings to the game.
        "completed": Completed(),
        "death": Death(),
        "discharged": Discharged(),

        "level_one_intro": LevelOneIntro(),
        "sgt's_office": SgtsOffice(),
        "path_to_war": WarPath(),
        "ship": Ship(),
        "arrival_at_normandy": NormandyBeach(),
        # "hell_on_beach": NormandyBeachHell(),
        # "quick_and_easy": NormandySafePlace(),
        # "damn_machine_gunner": DamnMachineGunner(), # a battle
        # "ambush": AmbushFoxHole(), # a battle
        # "captured": Captured(),
        # "torcher": Torcher(), # a possible battle
        # "afriend": Friend(),
        # "rescued": Rescued(), # a battle
        # "muddy": Muddy(),
        # "clever_soldier": Clever(),
        # "escaped_and_free": EscapedFree(),
        # "enemy_lines": EnemyLines(), # a battle
        # "evation": Evation(),
        # "stay_quiet": StayQuiet(), # possible battle
        # "attic": Attic(),
        # "rats": Rats(),
        # "the_road": Road(), # boss battle
        # "to_paris": ToParis(),
        # ending here for now
    }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.rooms.get(room_name)
        return val

    def first_room(self):
        return self.next_room(self.start_room)
