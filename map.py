from sys import exit  # importing neccessities
from textwrap import dedent
import map
import items
import char


class Room(object):  # a parent of all rooms

    def enter(self):
        print(dedent("""Sorry this level is still under construction. We
        apoligize for any inconvience we have caused you. Have a good day! """))
        exit(1)


class Death(Room):  # child of room go hear when you are killed in the game
    def enter(self):
        print("You died a soldiers death that is all that matters.")
        exit(1)


class Discharged(Room):  # child of room go hear when you have been dismissed in the game
    def enter(self):
        print("You have been discharged you are pathetic!")
        exit(1)


class LevelOneIntro(Room):  # child of room first room of the entire game
    def enter(self):
        print(dedent("""
        Welcome! soldier what is your name?
        """))

        name = input("# ")

        if name == 'Brian':
            return "completed"

        else:

            print(f"Okay, {name} you have been drafted!")
            print(dedent("""Your family is worried sick. World war
            two is raging across europe, you turned 18 just
            weeks ago. The military needs extra troops on the
            ground agaist the Nazi's. The Nazi's have infested
            Europe like a cockroch colony. You will be assigned
            to Unit 179. """))

            print(dedent('Any thoughts before we move on?'))

            thoughts = input('# ')

            if (thoughts != ''):
                print(dedent('Good thing no one cares'))
                return "sgt's_office"

            else:
                print('What? Please enter some thoughts.')
                return 'level_one_intro'


class SgtsOffice(Room):  # selecting the stats of the game in this room
    def enter(self):
        print(dedent("""Hey, you come on in! You have
        been drafted and their is a few things we have to
        settle before we can give you a deployment date.


        1. We need to get you some stats. Your stats are out
        of 100 pts each.

        2. You get to choose begining pt values for your stats.
        The begining values are equal to 30. Which means you can
        have a total of 30 pts of your stats. The stats include
        Strength, Swiftness, Charisma, intelligence, and Luck.

        3. You are not inviciable. You have a health of 100. Which
        means through out the game you can loose health and gain
        it back depending on the situation. So choose carefully. Also
        some enemies have health too.

        4. You have a couple of things to take care of. We will give
        you 10 sets of rations, 1 rifle and 1 map. Don't lose those
        things. You may be offered somethings along the way, I would
        not take them but it is up to you.

        5. Your goal is to fight the good fight. Make it out in one
        peice and home to your family.

        Yeah, I know that was a lot did you get it all?
        """))

        choice = input()

        if choice == 'yes':
            return "sgt's_office_stats"


class SgtsOfficeStats(Room):

    def enter(self):
        char.strength.amount = 0
        char.swiftness.amount = 0
        char.charisma.amount = 0
        char.intelligence.amount = 0
        char.luck.amount = 0

        print(dedent("So It is time to choose your stats!"))

        if char.luck.amount + char.strength.amount + char.intelligence.amount + char.swiftness.amount + char.charisma.amount > 30:
            print(dedent("""You sly dog!!! I see you tried to enter more than a total
            of 30 points! Don't do that again Okay! """))

            choice = input("# ")

            print('Good Try again!')

            return "sgt's_office_stats"

        else:

            print(dedent(f"""Okay, so you want {char.strength.amount} strength, {char.swiftness.amount} swiftness,
            {char.charisma.amount} charisma, {char.intelligence.amount} intelligence , and
            {char.luck.amount} luck. Is that final? """))

            choice = input("# ")

            if choice == "yes":
                return 'welcome_base_camp'

            elif choice == "All":
                print(dedent("""Okay sounds good to me! Your stats are now 100, but if you are not smart you
                could still loose some points."""))
                char.strength.amount = 100
                char.charisma.amount = 100
                char.intelligence.amount = 100
                char.swiftness.amount = 100
                char.luck.amount = 100

                return 'welcome_base_camp'

            else:
                print(dedent('What? you say yes if yes and no to try again.'))
                return "sgt's_office_stats"


class WelcomeBaseCamp(Room):
    def enter(self):
        print(dedent("""Okay so you have your stats and you are
        ready to go. Your deployment date will be 08.08.1941 . You
        are ours for 8 weeks.


        Be for we get started what unit type are you looking to be son?
        You got a couple of choices.

        A. rifle man
        B. Sniper Rifle
        C. machine gunner"""))

        choice = input('# ')

        if choice == 'A':
            gun = items.Item('rifle', True)
            print(dedent("""Okay soldier 8 weeks will be over in no time. You will
            have plenty of friends and plenty of skills when we are done."""))

            return 'minor_training'

        elif choice == 'B':
            gun = items.Item('sniper', True)
            print(dedent("""Oh, we are kind of short on snipers so looks like your getting shipped
            in a week instead."""))

            return 'path_to_war'

        elif choice == 'C':
            gun = items.Item('machine gun', True)
            print(dedent("""Okay, so you like to shoot lots of bullets I can respect that.
            We will not need to keep you to long but you will need the extra training. """))

            char.luck.amount += 5

            return 'minor_training'

        else:
            return 'welcome_base_camp'


class MinorTraining(Room):
    def enter(self):
        print(dedent("""Okay everyone welcome to training!
        Here we will cover the basics of warfare the do's and don'ts of our
        lovely trade. "the crowed laughs". Here the summary folks, weapons combat
        mellee combat, basic first aid, how to properly keep yourself with food
        and water and last but not least social do and don'ts.

        So let's get started then run 10 miles with your pack on. I will give you an hour and a half
        at the latest. *If you have 20 swiftness you will be sent down another path.*

        """))

        if char.swiftness.amount >= 20:
            print(dedent("""Oh, wow you were one of the first done. I think you
            would be a great rifle men.

            You may last more than a week boy, I wish you luck when is your
            deployment date?"""))

            choice = input("# ")

            print(dedent("""Oh, I see well son I am going to give you
            some extra rations for your travels. You will need em. Everyone gets
            10 rations, one weapon, one gernade and the cloths on their back. You get
            15 don't disappoint me son, make it home..."""))

            char.rations.amount += 5

            return 'path_to_war'

        else:

            print(dedent("""Well at least you were average. So here is
                your neccessities 10 rations, and 1 gernade"""))

            print(dedent("""So now that is done an over with time to move on.
                to strength training.

                What type of strength training would you like to do?

                A.Just listen to your sgt;

                B.Do strength training but longer than usual. Requires 15 or more strength!

                C.Avoid strength training.
                """
                         ))

            choice = input("# ")

            if choice == 'A':
                print(dedent("""
                    "Wow! You are quite the pull up master 40 in one
                    go. I think you excel in this field buddy. Your my
                    new favorite. Haaaaa" said the sgt.

                    """))

                char.charisma.amount += 5

                char.luck.amount += 5

                print(dedent("""Well you are ahead of the game so now lets get
                    into some wits. Germans will test you to the limits even the
                    those who are not soldiers.

                    If a german asks you "Du bist ein wasser hatean?" what do
                    you say?

                    A. Stay quiet

                    B. Answer: NINE!

                    C. Answer: Ja.

                    D. Answer: Halte Clappa! """))

                choice = input("# ")
                if choice == "A":
                    print(dedent("""Well you don't have much to say do you? Germans
                    would eat you up for breakfast. However I think the battle field
                    will sure make an impact on you bub."""))

                    return 'path_to_war'

                elif choice == "B":
                    print("""Nice you must know some German! You would be the
                    least suspected overall great job.

                    You have gained 5 charisma points!
                    You have gained 5 intelligence points!
                    """)

                    char.charisma.amount += 5
                    char.intelligence.amount += 5
                    return 'path_to_war'

                elif choice == "C":
                    print("""That would be the clever response. That exactly what they
                    want. I asked you if you hated water no german man in their right mind
                    would say "Ja".

                    You have lost 5 intelligence points.
                    """)
                    char.intelligence.amount -= 5

                elif choice == "D":
                    print("""You are an american I can tell you that. Just enough
                    know how to be stupid. Despite your arrogance I like you soldier.

                    You have lost 5 charisma points.
                    """)
                    char.charisma.amount -= 5
                    return 'path_to_war'

            elif choice == "B":
                print("Okay")
                return 'path_to_war'

            elif choice == "C":
                print("Okay")
                return 'path_to_war'

            else:
                return 'minor_training'


class WarPath(Room):
    def enter(self):
        print(dedent("""Okay, Your deployment date is here!

        You will will get on see and to the invasion of normandy!

        Good luck! Oh, wait one more thing...
        """))

        print(dedent("""Would you like to be

        A. First wave into the beaches?

        B. Second wave into the beaches?

        C. Last into the beaches?"""))

        choice = input("# ")

        if choice == 'A':
            print(dedent("""Brave and strong I like you my friend
            however, I just saw we are full with the first wave we will put you
            in the second"""))
            return 'ship'

        elif choice == 'B':
            print(dedent("""Good choice afterall our first
            wave is filled to the brim"""))
            char.intelligence.amount += 5
            return 'ship'

        elif choice == 'C':
            print("""Looks like we have ourselves a coward
            it is second deployment for you!""")
            char.charisma.amount -= 5
            return 'ship'


class Ship(Room):
    def enter(self):
        print(dedent("""You can see the beaches, the day is lovely clear and bright.
        However you start to hear the gun fire the screams in the distance. Your
        legs start to shake uncontrolably, you don't know what to do. You look at your
        commanding officer he signals the ship captian for all engines ahead. You hear
        the sgt scream "Alright boy's this is make or break!!". The boat is almost yards
        from the beach now the door opens...
        """))
        return 'completed'


class CompletedOne(Room):
    def enter(self):
        print(dedent("""Congrats You completed your first level!
        So in celebration you get to add 10 more points to your
        total count of stats! So what will it be?

        A. strength  B.charisma  C.swiftness

        D.luck  E. intellignece

        Remeber you only get to choose two!

        Make sure to answer like Ex:  A and B
        """))

        print(dedent("""So Strength is first. Please enter the value. It has to be more than five.
        an equal to ten in addition to your stats at the end"""))

        if luck_add + intelligence_add + swiftness_add + strength_add + charisma_add > 10:
            print(dedent(f"""No you can't have more than {amount} points to add to your stats
            you greedy bastard! I warned you earlier you are now discharged!"""))

            return 'discharged'

        else:
            print(dedent("Anything else before we move on?"))

            answer = input("# ")

            if answer == 'All':
                print(dedent("Oh, your too cool."))
                return 'completed'

            else:
                print(dedent("""Nope not a combo kid try again!"""))
                return 'completed_level_one'


class Completed(Room):  # end game except for bonus round
    def enter(self):
        print(dedent("Well you beat the game! Thats great!"))

        print(dedent("Any last words before we end?"))

        choice = input("# ")

        if choice == 'All':  # or if all stats are 100
            print("You get to go to a bonus round!")
            return 'atomic_jepoardy'

        else:
            print("""Well at least you finished the game.
            Go home now soldier your service is over.""")
            exit(1)


class Jepoardy(Room):  # bonus round

    Board = """

        Important People | Countries | Dates
            200          |  200      | 200
            400          |  400      | 400
            600          |  600      | 600

    """

    def enter(self):
        print(dedent(
            """This will take up a lot of space make sure you have a full size screen! Okay?"""))

        choice == input("# ")

        if choice == 'Okay':

            return 'room'

            print(dedent("Let us begin!"))

            print(dedent(Board))

        else:
            print(dedent("What? Just say Okay !"))
            return 'atomic_jepoardy'


class Map(object):  # all rooms in the game and communicates with the engine for the game functionality

    rooms = {
        "room": Room(),  # used to warn player of construction and parent of all other rooms
        "level_one_intro": LevelOneIntro(),  # start of level one
        "sgt's_office": SgtsOffice(),
        "sgt's_office_stats": SgtsOfficeStats(),
        "welcome_base_camp": WelcomeBaseCamp(),
        "minor_training": MinorTraining(),
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
        "stats_of_player": StatsOfPlayer(),
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
