from sys import exit  # importing neccessities
from textwrap import dedent
from random import randint
from char import Player, Enemy
import items

####################################
#### Map Class is at the bottom####
####################################

user = Player("level_one_intro", "sgt's_office", 100)
error = False

# For error handling to catch users attention

def message_pop_up(message=dedent("Please select an option below and type in the terminal.")):
    print(dedent("""
    ######## IMPORTANT ########
    ###########################
    ###########################
    {}
    ###########################
    ###########################
    """.format(message)))

# Merges all attack methods from Player into each and every battle.
def battles(enemy, enemy_weapon, message):

    error = False
    while enemy.health > 0 and user.health > 0:

        enemy.attack(enemy_weapon, user)

        choice = input('# ')

        user_choices = user.attack_choice(choice)

        if user_choices == None:
            error = True
            message_pop_up(dedent("""Due to your choice of neither A or B the room was
            reset, sorry for your inconvience. """))
            break

        if user_choices != False:
            print(user_choices)

        if user_choices == False:

            escaped = "You have escaped {}".format(enemy.name)
            break

        if 'What' in user_choices:

            item_name = input('# ')

            if items.find_item(user, item_name, "weapon") == False:
                message_pop_up(dedent(
                """
                Looks like that is not a weapon or it is not
                in your inventory.
                """))

            else:
                item = items.find_item(user, item_name, "weapon")
                print(dedent('Your item choice is {}'.format(item.name)))
                user.attack(item, enemy)

    # Going through outcomes of the battle based on importance
    if error:
        print(dedent('Looks like there was an error.'))
        return user.saved_room
    if user.health <= 0:
        return 'death'
    elif enemy.health <= 0:
        print(dedent(message))
        return False
    elif escaped:
        print(escaped)
        return user.next_room
    else:
        message_pop_up(dedent("""Error notify the creator of this issue. In the mean time sorry
        for your inconvience."""))


###                                ###
###  Possible Endings to the game  ###
###                                ###

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
            ending_scene = """fought near the effiel tower, you took a few hits
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

        A. Bartering stand and Repairs.
        Note: (Option above has full list of items.)

        B. Inventory related.

        C. Quit the game (Note: No progress will be save.).

        D. Back to game.

        """))

        choice = input('# ')

        if 'A' in choice:
            return "shop"

        elif 'B' in choice:
            return "inventory"

        elif 'C' in choice:
            return "quit"

        elif 'D' in choice:
            return user.saved_room

        else:
            message_pop_up()
            return "menu_enter"

# Quiting has to be an option (I guess)
class Quit(Room):

    def enter(self):

        message_pop_up(dedent("""
        Are you sure you want to quit? You made it so far! Remember
        no progress will be saved. (Type yes to quit and no to go back to menu.)"""))

        choice = input("# ")

        if 'yes' in choice:
            print(dedent("Good bye."))
            exit(0)
        if 'no' in choice:
            print(dedent('Redirecting back to menu......'))
            return 'menu_enter'
        else:
            message_pop_up()
            return 'quit'

class Shop(Room):
    def enter(self):

        print(dedent("""
        #####################################################################
        Welcome to the American depot soldier, or
        what they call jimmy's bartering stand. I can repair weapons, trade,
        and much more. What do you need?

        A. Repair an item.

        B. Buy an item

        C. Sell an item

        D. List all items in game.

        E. Back to menu

        """))

        choice = input("# ")

        if 'A' in choice:
            repair = items.repair_items(user)
            return 'menu_enter'

        elif 'B' in choice:
            buy = items.buy_items()
            return "menu_enter"
        elif 'C' in choice:
            items.sell_items()
            return 'menu_enter'
        elif 'D' in choice:
            items.list_items()
            return 'menu_enter'

        elif 'E' in choice:
            return "menu_enter"

        else:
            message_pop_up()
            return "shop"

class Inventory(Room):

    """Displaying the inventory and other
    actions related to invetory here."""

    def enter(self):
        print(dedent("""
        Please choose an option for your inventory.

        A. Check what is in your inventory.

        B. Drop an item in your inventory.

        C. Back to the main menu.

        """))

        choice = input('# ')

        if 'A' in choice:
            user.check_inventory()
            return 'menu_enter'
        elif 'B' in choice:
            user.drop()
            return 'menu_enter'
        elif 'C' in choice:
            return 'menu_enter'
        else:
            message_pop_up()

#########################
## Start of game rooms ##
#########################

class LevelOneIntro(Room):
    def enter(self):
        print(dedent("""
        Welcome! soldier what is your name?
        """))

        user.name = input('# ')

        if user.name == 'Brian':
            user.add_to_inventory(items.bazooka)

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

        """Reminder for users to read the rules before playing."""

        user.saved_room = "sgt's_office"
        user.next_room = "path_to_war"

        print(dedent("""
        Welcome soldier I am a reminder here to tell you the
        make sure to read the Rules.md file!

        Did you read the rules and your ready to play??

        A. yes

        B. No

        """))

        choice = input('# ')

        if 'C' in choice:
            return 'menu_enter'
        elif 'A' in choice:
            return "path_to_war"
        elif 'B' in choice:
            message_pop_up('Go read the Rules.md file!')
            exit(0)
        else:
            message_pop_up()
            return "sgt's_office"

class WarPath(Room):
    """ You get to choose your last recreational activity as a soldier before
    storming the beachs at normandy, France."""

    def enter(self):

        user.saved_room = 'path_to_war'
        user.next_room = 'ship'

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

            if randint(1, 4) == 3:
                print(dedent("""
                You played some poker, you won a thing or two, but got carried away. In the final round
                you bet it all. You fell right into the bluff of a fellow private and lost it all. You lost 7 rations."""))
                items.rations.quantity -= 7
                print(dedent("You now have only {} rations.".format(items.rations.quantity)))

            elif randint(1, 4) == 1:
                print(dedent("""
                You did pretty good for poker, you played fair and gained 5 rations"""))
                items.rations.quantity += 5
                print(dedent("You now have {} rations.".format(items.rations.quantity)))

            elif randint(1, 100) == 33:
                print(dedent("""
                Uh Oh! Your sgt caught you playing poker under the table,
                the group blames you. You are in big trouble."""))

                return 'discharged'

            elif randint(1, 3) == 2:
                print(dedent("""
                Wow!!! Looks like you were in an all stakes game with a bazooka
                gunner. You won it all! You now have a bazooka in you midst."""))

                user.add_to_inventory(items.bazooka)

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
            message_pop_up()
            return 'path_to_war'

        return  'ship'

class Ship(Room):
    """On the 3 day trip to normandy beach final training and
    preperation before storming the beachs."""
    def enter(self):

        user.saved_room = 'ship'
        user.next_room = 'arrival_at_normandy'

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
        
        """))

        choice = input('# ')

        ship_mate = Enemy(5, "Jimmy")

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

            print(dedent("Your health is now {}".format(user.health)))

        elif 'B' in choice:
            print(dedent(
            """
            You say "Hey, Jimmy". You kick his shin and he falls to the ground.
            Everyone looks at you. Jimmy stares with rage.
            """
            ))

            play = battles(
            ship_mate, items.hands, """
            Everyone looks at Jimmy's dead corpse. They all start
            charging at you, and pin you to the floor. "You don't kill our own men!!!" some one screamed.
            """
            )

            if play != False:
                return play
            else:
                return 'discharged'




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
            two glocks. You say "Hey, kyle I know we are not suppose to have those, but I
            can forget about it if there is one for me and you."
            """
            ))

            input('# ')

            print(dedent(
            """
            "Okay, {} I will give you one. But hush up these guns are not invented yet."
            """.format(user.name)))

            user.add_to_inventory(items.glock)

            print(dedent('You now have a {} in your inventory.'.format(items.glock.name)))

        else:
            message_pop_up()
            return 'ship'

        return "arrival_at_normandy"

class NormandyBeach(Room):
    """First landing at france. Our player has to navigate through
    decisions of death."""

    def enter(self):

        user.saved_room = 'arrival_at_normandy'

        return 'room'


class Map(object):

    rooms = {
        "room": Room(),

        # Menu options
        "menu_enter": Menu(),
        "inventory": Inventory(),
        "shop": Shop(),
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
        # "murika" Murika() #Ending
    }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.rooms.get(room_name)
        return val

    def first_room(self):
        return self.next_room(self.start_room)
