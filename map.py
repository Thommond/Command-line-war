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
        print(dedent(message))
        return 'death'
    elif enemy.health <= 0:
        print(dedent(message))
        ration = user.get_player_item_val("rations", user)
        rando = randint(1, 4)
        if rando == 1:
            ration += 2
            print("You got two rations from battle.")
        elif rando == 2:
            ration += 10
            print("you got ten rations from battle.")
        elif rando == 3:
            print(dedent("You get nothing from this battle."))
        elif rando == 4:
            ration += 5
            print("You got five ration from battle.")
        return user.next_room
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

        print("""You died a soldiers death that is all that matters.

                                             ____
                              __,---'     `--.__
                           ,-'                ; `.
                          ,'                  `--.`--.
                         ,'                       `._ `-.
                         ;                     ;     `-- ;
                       ,-'-_       _,-~~-.      ,--      `.
                       ;;   `-,;    ,'~`.__    ,;;;    ;  ;
                       ;;    ;,'  ,;;      `,  ;;;     `. ;
                       `:   ,'    `:;     __/  `.;      ; ;
                        ;~~^.   `.   `---'~~    ;;      ; ;
                        `,' `.   `.            .;;;     ;'
                        ,',^. `.  `._    __    `:;     ,'
                        `-' `--'    ~`--'~~`--.  ~    ,'
                       /;`-;_ ; ;. /. /   ; ~~`-.     ;
-._                   ; ;  ; `,;`-;__;---;      `----'
   `--.__             ``-`-;__;:  ;  ;__;
 ...     `--.__                `-- `-'
`--.:::...     `--.__                ____
    `--:::::--.      `--.__    __,--'    `.
        `--:::`;....       `--'       ___  `.
            `--`-:::...     __           )  ;
                  ~`-:::...   `---.      ( ,'
                      ~`-:::::::::`--.   `-.
                          ~`-::::::::`.    ;
                              ~`--:::,'   ,'
                                   ~~`--'~
        """)
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

        C. Eat

        D. Quit the game (Note: No progress will be save.).

        E. Back to game.

        """))

        choice = input('# ')

        if 'A' in choice:
            return "shop"

        elif 'B' in choice:
            return "inventory"

        elif 'C' in choice:
            user.add_to_player_health()
            return 'menu_enter'

        elif 'D' in choice:
            return "quit"

        elif 'E' in choice:
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

        if 'menu' in choice:
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

            elif randint(1, 50) == 33:
                print(dedent("""
                Uh Oh! Your sgt caught you playing poker under the table,
                the group blames you. You are in big trouble."""))

                return 'discharged'

            elif randint(1, 50) == 14:
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
        user.next_room = 'normandy'

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
        Jimmy lays a punch and then Timothy. The fight starts to get rough.
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

        return user.next_room

class NormandyBeach(Room):
    """First landing at france. Our player has to navigate through
    decisions of death."""

    def enter(self):

        user.saved_room = 'normandy'
        user.next_room = 'hell_beach'

        print(dedent("""

        Sgt said

        "GENTAL MEN! ITS TIME TO PROVE YOUR WORTH.

        In fifthteen minutes we will reach the shores of normandy
        for our planned assualt off occupied france. Prepare your
        gear and make peace with your God."
        """))

        input('# ')

        print(dedent("""
        The USS Great Leap finally reaches the point of dock. All your
        fellow soldiers rush in the beach ships. You hop in the ship, packed
        like sardieens the ship struggles to the shore. Just when the front gate opens...
        """))

        input('# ')

        print(dedent("""
        BANG!

        The entire front of the ship is blown to oblivian. An artillary
        blast took out 20 of your peers. Lucky for you, you were in the back
        of the shipand live to die another day. A few others including your
        SGT voided the blast.

        "OKAY YOU SORRY BASTARDS, WE SAW THE FATE OF OUR MEN BUT THAT WILL NOT
        STOP YOU NOW. GET YOUR RIFLES AND CHARGE OR I'LL KILL YOU MYSELF." sgt screamed over the rapid machine gun fire.

        A. Charge in the beach with your peers.

        B. Stay back and give cover fire.

        C. Hide in the water and hope you live.

        D. Scope out the flow of the beach.
        """))

        choice = input('# ')

        if 'menu' in choice:
            return 'menu_enter'

        if 'A' in choice:
            print(dedent("""
            Just like a fresh cadet from New York would you charge the beach.
            However, in 5 seconds you bit the bullet of a mp40. 7 bullets in
            your body falls to the ground in an instant. You slowly bleed out
            until a artillary blast gives you unintentional mersy.
            """))

            return 'death'

        elif 'B' in choice:

            print(dedent("""
            A calculated move you offer your cover fire to protect the rushing cadets.
            Sgt approves you and 15 others to hold the line in prone position. Lucky for
            the cadets you have their back. More than half make it to a guard tower where
            they hold their position.
            """))

            input('# ')

            print(dedent("""
            Quick thinking {}. Have a grenade it
            could come in handy. said Sgt
            """.format(user.name)))

            add_to_inventory("grenade")

            return user.next_room

        elif 'C' in choice:

            print(dedent("""
            Too afraid to face the beach you cowar in the water watching
            your fellow soldiers fight life and limb. Unlucky for you the
            Sgt meant what he said.
            """))

            sgt = Enemy(25, 'Sargent Bowers')

            battles(
            sgt, items.glock,
            """
            Looks like the Sgt was quite a challenge. You ran to a structure
            where it looks like soldiers are held up.
            """
            )

            return user.next_room

        elif 'D' in choice:
            print(dedent("""
            Your eyes skim the beach on the left you see a trailing pile
            of dead bodies along the lines of the barb wire. On your right you spot
            a machine gunner plowing down every soldier attempting to conquer the beach.
            Finally, dead ahead 100 meters you see a small structure and a few soldiers
            holding their ground. Better than nothing...
            """))

            input('# ')

            print(dedent("""
            You dash towards the group, and take
            a hit in the shoulder on the way. You made it... barely.
            """))

            user.health -= 30

            print(dedent("""Your health is now down to {} because you got shot
            in the arm on the way to the structure.""".format(user.health)))

            return user.next_room

        else:
            message_pop_up()
            return user.saved_room

class Hell_beach(object):


    def enter(self):

        user.saved_room = 'hell_beach'
        user.next_room = 'quick'

        print(dedent("""
        Are you okay? a soldier exclaimed.
        """))

        input('# ')

        print(dedent("""
        Well, sorry I asked we don't have time to talk. Two machine
        gunners have us pinned. Only 11 of use left, but I guess 12
        counting you. We are going to storm the left he reloads Every
        7 minutes, for about 30 seconds.
        """))

        input('# ')

        print(dedent("""
        Alright, here goes nothing!

        A. Charge to the left with the rest of the troops.

        B. Sneak to the right to see if you can catch the other gunner by suprise.

        C. Lead the CHARGE

        D. Prone down and fire your weapon at the gunner.

        """))

        choice = input('# ')

        if 'menu' in choice:
            return 'menu_enter'

        if 'A' in choice:

            print(dedent("""
            The men scatter across the beach running towards the left gunner
            and rifle in hand. You seen 5 brother in total get mowed down before
            a brother gets the gunner with a rifle fire. They storm the gunners
            hide out and kill two more and get one prisoner.
            """))

            input('# ')

            print(dedent("""
            Looks like you found 3 rations on the dead bodies. lucky you.
            """))

            rations = user.get_player_item_val("rations", user)

            rations += 3

            print('You now have {} rations'.format(rations))

            return user.next_room

        elif 'B' in choice:
            print(dedent('''
            Everyone charges to the left. You swiftly move to the right to
            confront the right side machine gunner.
            '''))

            input('# ')

            print(dedent('''
            Your about to take the shot when, the gunner spots you and blasts
            to infinity. You never stood a chance.
            '''))

            return 'death'

        elif 'C' in choice:
            print(dedent('''
            You yell, "Hey I will lead the charge".

            Everyone in the troop agrees.
            '''))

            input('# ')

            print(dedent('''
            One, two, three CHARGE!

            Everyone runs with enthusiams towards the
            machine gunner. Four men are mowed down almost
            instantly. But you got in a lucky shot and nailed the
            gunner right on his ass. You all quickly take the
            hideout and get 3 men hostage.
            '''))

            input('# ')

            print(dedent('''
            Hey, brother you did a great job out there a soldier said.

            We all pitched in and for what it is worth we want to give you
            this.
            '''))

            input('# ')

            print(dedent('All the men point at the machine gun and offer it to you.'))
            print(dedent('Do you want the machine gun? (type yes to accept)'))

            choice = input('# ')

            if 'yes' in choice:
                user.add_to_inventory(items.machine_gun)
            else:
                print(dedent('Your loss, a soldier exclaimed.'))

            return user.next_room

        elif 'D' in choice:

            print(dedent('''

            The troops charge and you keep firing at the machine gunners position.
            It keeps him busy for most of the time and only 2 men were lost. They
            take the hideout with shear force and signal you to run towards them.
            '''))

            input('# ')

            print(dedent("""
            You dash across the no mans land and dodge sniper fire. The men cover
            you as much as they can.

            you whisper "thanks guys I owe you one"

            a soldier responds "count us even you had our asses."
            """))

            input('# ')

            print(dedent('"Here dude take this" he hands you a ration.'))

            rations = user.get_player_item_val("rations", user)
            rations += 1

            return user.next_room

        else:
            message_pop_up()
            return user.saved_room


class SafePlace(Room):

    def enter(self):

        user.saved_room = 'quick'
        user.next_room = 'gunner'

        print(dedent("""

        Six brutal hours have passed in the hideout. You and the men sit
        and lick your wounds. Its almost dark and the battle ground has
        finally begun to quiet down.

        A. Stay in the hideout till morning.

        B. Advise a sneak attack on the rest of the enemy troops.

        C. Draw enemy attention.

        D. Retreat back to rubble in the water.
        """))

        choice = input('# ')

        if 'menu' in choice:
            return 'menu_enter'

        if 'A' in choice:

            print(dedent("""
            You and the troops agree to wait out the night in the
            hideout. You hear bits of rifle fire in the night and just
            enough screaming to remember even in your dreams, you are
            not at home you are at war.
            """))

            input('# ')

            print(dedent("""
            You wake up just before sunrise and alert the others. "Hey guys"
            you stated "its almost sun rise we need to make a move".
            """))

            input('# ')

            print(dedent("""
            Whoosh!

            You look at the slit in the hideout and see an incoming...

            "No! Not now" you think.
            """))

            input('# ')

            print(dedent("""
            "Grenade!" You yelled.

            A. Jump on grenade.

            B. Don't jump on grenade.

            """))

            choice = input('# ')

            if 'menu' in choice:
                return 'menu_enter'

            if 'A' in choice:

                print(dedent("""
                You dashed and landed on the grenade. Closing
                your eyes in these last moments you think of your wife and
                how sad she will be alone, all alone.
                """))

                input('# ')

                print(dedent("""
                You open your eyes...

                And...
                And...
                Wait what?
                """))

                print("""
                One of your fellow soldiers comes up to you and says

                "Luck for you and us it was a dud"

                "You showed more bravery than any man I know here take these."

                He handed you 20 rations.
                """)

                rations = user.get_player_item_val('rations', user)
                rations += 20

            else:

                print(dedent('Another soldier dashes and jumps on the grenade'))

                input('# ')

                print(dedent("""Boom!


                The grenade splits the man into pieces shards
                of bone, flesh and metal all over the hideout."""))

                input('# ')

                print(dedent("""

                Ring Ring Ring Ring Ring

                "I can't hear myself think" you screamed
                """))

                input('# ')

                print(dedent("""
                Finally when it all stoped your relucantally realized you are
                the only one who is not dead, or wish they were.
                """))

            return user.next_room

        elif 'B' in choice:

            print(dedent("""
            Hey, Guys we take night to our advantage. Lets attack now
            they think we are down but we can do it. You encouraged the
            troops.
            """))

            input('# ')

            print(dedent("""
            Yeah, I think this could work said the troops.

            So, you all prepare bandage up your wounds and load
            your fire arms. So what is the plan?
            """))

            print(dedent("""
            You whisper "Half of us stay back the remaining half
            slowly charge the gunner while being covered. If all goes
            well then the gunner will focus on what he sees the fire
            troops which will give us a edge."

            They all nod.
            """))

            input('# ')

            print(dedent("""
            What are you all waiting for lets go!

            At first all seems to go well every troop remaining is in
            position, but then.

            Flick
            """))

            input('# ')

            print(dedent("""
            What you and your plan forgot to account for was spot lights!

            The germans can see everyone the machinge gunner practiclly
            enjoys the slaughter.

            You run back to the hideout while your fellow men are killed
            like a dog in the street.
            """))

            return user.next_room

        elif 'C' in choice:

            print(dedent("""
            You scream and wave your hands to get enemy attention.
            """))

            print(dedent("""
            Spot lights turn on and go right on the hideout and from
            this point on the hideout is under constant fire.

            Then you say with a relucantally at "least we did not try to
            attack."
            """))

            return user.next_room

        elif 'D' in choice:

            print(dedent("""
            You panic and tell the men you and them should go back to
            the beach.

            "No that would be suicide." said one soldier.
            """))

            print(dedent("""
            You and one other then run back to the beach and then the lights
            turn on and before you know it spot light are on you. Not long after
            the light turn on you feel bullets rip through your chest. You fall
            to the floor slowly bleed out in misery.
            """))

            return 'death'

        else:
            message_pop_up()
            return user.saved_room

class MachineGun(Room):

    def enter(self):

        user.saved_room = 'gunner'
        user.next_room = 'ambush'

        print(dedent("""
        So we are back where we started and it is mid day.
        Its only a matter of time you thought to yourself.

        You grab your weapon, what now?

        A. Play dead

        B. Keep fire at the enemy lines

        C. Hold tight with weapon in hand

        D. Make one last charge at the gunner.
        """))

        choice = input('# ')

        if 'menu' in choice:
            return 'menu_enter'

        if 'A' in choice:

            print(dedent("""
            You lay in the hideout with other corps and rot and for
            a few hours you say "We will be fine."
            """))

            return user.next_room

        elif 'B' in choice:

            if rand_int(1, 2) == 2:
                print(dedent("""
                You hold ground and even kill the machine gunner quite
                a accomplishment.

                While holding your own you searched your comrades bodies
                and found quite a bounty 6 rations.
                """))
                rations = user.get_player_item_val('rations', user)
                rations += 6

            else:

                print(dedent("""
                During your hold out little did you accound for being
                outnumbered eighteen to one. You did put up a fight, but
                quickly you were...
                """))

            return user.next_room

        elif 'C' in choice:

            print(dedent("""
            You hide in the hideout weapon in hand thinking you are prepared
            for anything But...
            """))

            input('# ')

            print(dedent("""
            Pop! You accidently pulled your own trigger and blasted
            half you head out. Still alive you try to craw and reach your hand to
            a dead soldiers gun. But you never reached it, it took you a full hour
            to bleed to death.
            """))

            return 'death'

        elif 'D' in choice:

            gunner = Enemy(20, 'machine gunner')

            print(dedent("""
            You make a stand and head on the gunner
            from the hide out, just you and him
            """))

            input('# ')

            battles(gunner, items.machine_gun,
            """
            You finally got the battle you were asking for to avenge
            your fellow men. Hopefully it turned out in your favor.
            """)

            return user.next_room

        else:
            message_pop_up()
            return user.saved_room

class Ambush(object):

    def enter(self):

        user.saved_room = 'ambush'
        user.next_room = 'captured'

        print(dedent("""
        AN AMBUSH a soldier cried.
        """))

        input('# ')

        print(dedent("""
        You hear foot steps louder than a thunder and the
        rustling of machinery on a verge of being on top of
        you. "The line must have been pushed back" a soldier
        exclaimed. "we have to get out of here!". A soldier ran
        out of the hide out gun blazing and was shot down cold.
        You said "No one move..."

        A. Instruct surrender.

        B. Hold the hideout.

        C. Push out of the hideout and put up a fight.
        """))

        if 'menu' in choice:
            return 'menu_enter'

        elif 'A' in choice:
            print(dedent("""

            "we have to surrender there is no way out" you said.

            "but, but, we can't surrender to these scum!" a soldier
            screamed.

            "Do you want to die here just to make a point, we can
            fight another day!" you yelled.

            "Okay, Okay"
            """))

            input('# ')

            print(dedent("""

            You pull out a little white cloth an wave it out the window,
            it is a crisp morning so the German troop luckly don't mistake
            your arm for a gun.

            "Hände hoch oder ich schieße!"

            A german soldier instructed to get our attention.

            The german speaker of the group said "he wants us to come
            out with our hands up or he will shoot."
            """))

            input('# ')

            print(dedent("""
            Everyone walks out and almost immediately are stripped of
            weapons and cargo.

            Everyone hops in a truck with a few other rough looking lads.
            """))

            return user.next_room

        elif 'B' in choice:

            print(dedent("""

            "we have to make a plan to hold the fort" you said.

            "But we could be killed there are so many of them" exclaimed a soldier

            "Yeah, better die fighting for our country then captured
            in a german prisoner of war camp."

            Everyone gets into their positions to hold the fort and you
            give the instruction to fire.
            """))

            input('# ')

            print(dedent("""
            In the distance you see...
            """))

            input('# ')

            print(dedent("""
            Tiger!!!!!

            WHOOSH
            """))

            print(dedent("""

                ░░░░░░███████ ]▄▄▄▄▄▄▄▄▃
                ▂▄▅█████████▅▄▃▂
                I███████████████████].
                ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤

            BOOM!

            Little did you know the only option was
            surrender, the germans had a tiger tank
            sighted on that fort since 5am.

            """))

            return 'death'

        elif 'C' in choice:
            print(dedent("""
            "we have to get ready to charge" you said.

            "We have no idea whats in store for us, there
            is no way we should charge did you not witness
            what happened to reg? You know the guy who ran out
            15 minutes ago??"

            Everyone agrees to surrender, but you.

            So, you pull out your gun and start to fire.

            Everyone screamed "NOOO" then...

            """))

            print(dedent("""
            You were sniped to the ground while the rest of the men came
            out with hands up.
            """))

            return 'death'

        else:
            message_pop_up()
            return user.saved_room





class Captured(object):

    def enter(self):
        user.saved_room = 'captured'
        user.next_room = 'torcher'

        print(dedent("""

        On the truck you are given prisoner numbers. Everyone
        on the vehicle is rightfully disappointed and distraught
        at their next step in the fight.

        Rolling on in the muddy fields of france you are headed for
        german heart land.

        "Hey, what is going on?" you asked.

        "Well, we are being put into prisoner of war camps just 100 miles off
        of berlin. At least that is what we hope."

        "What do you mean?" you asked curiously.

        "Well, pal there are rumors that we could be headed
        to work camps, or even death camps"

        "That would be against the convention" you stated.

        "Well, welcome to cold heartless fight of 1944"

        "whats your name?" you asked

        "well I am Jacob Krowter, but people call me Slide"

        "I am {}, so why do they call you Slide, Slide?"

        "Well I slide right out of the enemy hands you see."

        """.format(user.name)))

        input('# ')

        print(dedent("""

        A. Ask Slide and the others to attempt to take the truck.

        B. Wait for the ride and see your fate.

        C. Plea with a German officer to let you go.

        D. Run off the truck as fast as you can.

        """))

        choice = input('# ')

        if 'menu' in choice:
            return 'menu_enter'

        elif 'A' in choice:
            pass
        elif 'B' in choice:
            pass
        elif 'C' in choice:
            pass
        elif 'D' in choice:
            pass

        else:
            message_pop_up()
            return user.saved_room

class Torcher(object):

    def enter(self):
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

        # Rooms of game
        "level_one_intro": LevelOneIntro(),
        "sgt's_office": SgtsOffice(),
        "path_to_war": WarPath(),
        "ship": Ship(),
        "normandy": NormandyBeach(),
        "hell_beach": Hell_beach(),
        "quick": SafePlace(),
        "gunner": MachineGun(),
        "ambush": Ambush(),
        "captured": Captured(),
        "torcher": Torcher(), # a possible battle
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
