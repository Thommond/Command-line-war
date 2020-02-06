from sys import exit
from textwrap import dedent
import items


class Room(object):

    def enter(self):
        print("This is the start of creating many rooms")
        exit(1)


class Death(Room):
    def enter(self):
        print("You died a soliders death that is all that matters.")
        exit(1)


class Discharged(Room):
    def enter(self):
        print("You have been discharged you are pathetic!")
        exit(1)


class LevelOneIntro(Room):
    def enter(self):
        print(dedent("""
        Welcome! Solder what is your name?
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


class SgtsOffice(Room):
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
        """))

        print(dedent("So It is time to choose your stats!"))

        print("""So Strength is first. Please enter the value. It has to be more than five.
        an equal to thirty in the end""")

        items.strength.points += int(input("# "))

        print("Next is Swiftness. Rules apply always.")

        items.swiftness.points += int(input("# "))

        print("Now is Charisma.")

        items.charisma.points += int(input("# "))

        print("Time for intelligence.")

        items.intelligence.points += int(input("# "))

        print('Last but not least it is time for Luck.')

        items.luck.points += int(input("# "))

        if items.luck.points + items.strength.points + items.intelligence.points + items.swiftness.points + items.charisma.points > 30:
            print(dedent("""You sly dog!!! I see you tried to enter more than a total
            of 30 points! Try again!"""))
            return "sgt's office"

        else:

            print(dedent(f"""Okay, so you want {items.strength.points} strength, {items.swiftness.points} swiftness,
            {items.charisma.points} charisma, {items.intelligence.points} intelligence , and
            {items.luck.points} luck. Is that final? """))

            choice = input("# ")

            if choice == "yes":
                return 'welcome_base_camp'

            elif choice == "All":
                print("Okay sounds good to me! Your stats are now 100 for good.")
                items.strength.points = 100
                items.charisma.points = 100
                items.intelligence.points = 100
                items.swiftness.points = 100
                items.luck.points = 100

                return 'welcome_base_camp'

            else:
                print('What? you say yes if yes and no to try again.')
                return "sgt's_office"


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
            print("""Okay solder 8 weeks will be over in no time. You will
            have plenty of friends and plenty of skills when we are done.""")

            return 'Minor_training'

        elif choice == 'B':
            gun = items.Item('sniper', True)
            print(dedent("""Oh, we are kind of short on snipers so looks like your getting shipped
            in a week instead."""))

            return 'Path_to_war'

        elif choice == 'C':
            gun = items.Item('machine gun', True)
            print(dedent("""Okay, so you like to shoot lots of bullets I can respect that.
            We will not need to keep you to long but you will need the extra training. """))

            items.luck.points += 5

            return 'Minor_training'

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
        at the latest.

        """))

        if items.swiftness.points >= 20:
            print("""Oh, wow you were one of the first done. I think you
            would be a great rifle men.

            You may last more than a week boy, I wish you luck when is your
            deployment date?""")

            choice = input("# ")

            print(dedent("""Oh, I see well son I am going to give you
            some extra rations for your travels. You will need em. Everyone gets
            10 rations, one weapon, one gernade and the cloths on their back. You get
            15 don't disappoint me son, make it home..."""))

            items.rations.amount += 5

        else:

            print(dedent("""Well at least you were average. So here is
                your neccessities 10 rations, and 1 gernade"""))

            print(dedent("""So now that is done an over with time to move on.
                to strength training.

                What type of strength training would you like to do?

                A.Just listen to your sgt

                B.Do strength training but longer than usual.

                C.Avoid strength training.
                """
                         ))

            choice = input("# ")

            if choice == 'A' and items.strength.points >= 15:
                print(dedent("""
                    "Wow! You are quite the pull up master 40 in one
                    go. I think you excel in this field buddy. Your my
                    new favorite. Haaaaa" said the sgt.

                    """))

                items.charisma.points += 5

                items.luck.points += 5

                print(dedent("""Well you are ahead of the game so now lets get
                    into some wits. Germans will test you to the limits even the
                    those who are not solders.

                    If a german asks you "Du bist ein wasser hatean?" what do
                    you say?

                    A. Stay quiet

                    B. Answer: NINE!

                    C. Answer: Ja.

                    D. Answer: Halte Clappa! """))

                choice = input("# ")

                if choice == "NINE!":
                    items.charisma.points += 5
                    items.intelligence.points += 5

                    print(dedent("""Smart man you must know a little german.
                        I asked if you hated water. Now germans will be a bit
                        less forgiving if some one was to answer the wrong answer.

                        Now, enough of this your deployment date is soon so I need you
                        to make one last choice. Just for the fun of it.

                        What is the most purchased car of 2019?


                        A. Jeep Wrangler

                        B. Hummer odessey

                        C. Toyota Camery

                        D. Nissan Ultima """))

                    choice = input("# ")

                    if choice == 'A':
                        print(dedent("""Great vehicle but not a best seller, good guess though. It's
                            okay this is not actually part of you evation."""))

                        return 'Path_to_war'

                    elif choice == 'B':
                        print(("""You pathtic baffoon! Hummer stoped all manufacuring since 2009.
                                Just because your answer you have been discharged. """))

                        return 'discharged'

                    elif choice == 'C':
                        print(dedent(
                            "Well done! You know your triva. It is time for deployment."))

                        return 'Path_to_war'

                    elif choice == 'D':
                        print(dedent("""Well Nissan has never had a good best seller. It was a
                            great guess but no not it. At least you tried. You can say your
                            sgt had a sence of humour unlike most of my peers."""))

                        return 'Path_to_war'

                    else:
                        print(dedent("""You are not as bright as I though you were. There is only
                        four answers a, b, c, and d. So choose one of them solider!"""))

                        return 'Minor_training'

            elif choice == 'B':
                print(dedent("""Nice, you are my new favorite."""))

                items.charisma.points += 5
                items.strength.points += 10
                print(dedent("""Well you are ahead of the game so now lets get
                    into some wits. Germans will test you to the limits even the
                    those who are not solders.

                    If a german asks you "Du bist ein wasser hatean?" what do
                    you say?

                    A. Stay quiet

                    B. Answer: NINE!

                    C. Answer: Ja.

                    D. Answer: Halte Clappa! """))

                choice = input("# ")

                if choice == "NINE!":
                    items.charisma.points += 5
                    items.intelligence.points += 5

                    print(dedent("""Smart man you must know a little german.
                        I asked if you hated water. Now germans will be a bit
                        less forgiving if some one was to answer the wrong answer.

                        Now, enough of this your deployment date is soon so I need you
                        to make one last choice. Just for the fun of it.

                        What is the most purchased car of 2019?


                        A. Jeep Wrangler

                        B. Hummer odessey

                        C. Toyota Camery

                        D. Nissan Ultima """))

                    choice = input("# ")

                    if choice == 'A':
                        print(dedent("""Great vehicle but not a best seller, good guess though. It's
                            okay this is not actually part of you evation."""))

                        return 'Path_to_war'

                    elif choice == 'B':
                        print(("""You pathtic baffoon! Hummer stoped all manufacuring since 2009.
                                Just because your answer you have been discharged. """))

                        return 'discharged'

                    elif choice == 'C':
                        print(dedent(
                            "Well done! You know your triva. It is time for deployment."))

                        return 'Path_to_war'

                    elif choice == 'D':
                        print(dedent("""Well Nissan has never had a good best seller. It was a
                            great guess but no not it. At least you tried. You can say your
                            sgt had a sence of humour unlike most of my peers."""))

                        return 'Path_to_war'

                    else:
                        print(dedent("""You are not as bright as I though you were. There is only
                        four answers a, b, c, and d. So choose one of them solider!"""))

                        return 'Minor_training'

            elif choice == 'C':
                print(dedent("""Well, Your lazy as hell I can't have a
                solider like that."""))
                return 'discharged'

                print(dedent("""Well you are ahead of the game so now lets get
                    into some wits. Germans will test you to the limits even the
                    those who are not solders.

                    If a german asks you "Du bist ein wasser hatean?" what do
                    you say?

                    A. Stay quiet

                    B. Answer: NINE!

                    C. Answer: Ja.

                    D. Answer: Halte Clappa! """))

                choice = input("# ")

                if choice == "NINE!":
                    items.charisma.points += 5
                    items.intelligence.points += 5

                    print(dedent("""Smart man you must know a little german.
                        I asked if you hated water. Now germans will be a bit
                        less forgiving if some one was to answer the wrong answer.

                        Now, enough of this your deployment date is soon so I need you
                        to make one last choice. Just for the fun of it.

                        What is the most purchased car of 2019?


                        A. Jeep Wrangler

                        B. Hummer odessey

                        C. Toyota Camery

                        D. Nissan Ultima """))

                    choice = input("# ")

                    if choice == 'A':
                        print(dedent("""Great vehicle but not a best seller, good guess though. It's
                            okay this is not actually part of you evation."""))

                        return 'Path_to_war'

                    elif choice == 'B':
                        print(("""You pathtic baffoon! Hummer stoped all manufacuring since 2009.
                                Just because your answer you have been discharged. """))

                        return 'discharged'

                    elif choice == 'C':
                        print(dedent(
                            "Well done! You know your triva. It is time for deployment."))

                        return 'Path_to_war'

                    elif choice == 'D':
                        print(dedent("""Well Nissan has never had a good best seller. It was a
                            great guess but no not it. At least you tried. You can say your
                            sgt had a sence of humour unlike most of my peers."""))

                        return 'Path_to_war'

                    else:
                        print(dedent("""You are not as bright as I though you were. There is only
                        four answers a, b, c, and d. So choose one of them solider!"""))

                        return 'Minor_training'


class PathToWar(Room):
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
            return 'Ship'

        elif choice == 'B':
            print(dedent("""Good choice afterall our first
            wave is filled to the brim"""))
            items.intelligence.points += 5
            return 'Ship'

        elif choice == 'C':
            print("""Looks like we have ourselves a coward
            it is second deployment for you!""")
            items.charisma.points -= 5
            return 'Ship'


class Ship(Room):
    def enter(self):
        print("""You can see the beaches, the day is lovely clear and bright.
        However you start to hear the gun fire the screams in the distance. Your
        legs start to shake uncontrolably, you don't know what to do. You look at your
        commanding officer he signals the ship captian for all engines ahead. You hear
        the sgt scream "Alright boy's this is make or break!!". The boat is almost yards
        from the beach now the door opens...
        """)
        return 'Completed'


class CompletedOne(Room):
    def enter(self):
        print("""Congrats You completed your first level!
        So in celebration you get to add 10 more points to your
        total count of stats! So what will it be?

        A. strength  B.charisma  C.swiftness

        D.luck  E. intellignece

        Remeber you only get to choose two!

        Make sure to answer like Ex:  A and B
        """)

        print(dedent("""So Strength is first. Please enter the value. It has to be more than five.
        an equal to ten in addition to your stats at the end"""))

        strength_add = int(input("# "))

        items.strength.points += strength_add
        print('Next is Swiftness. Rules apply always.')

        swiftness_add = int(input("# "))

        items.swiftness.points += swiftness_add

        print("Now is Charisma.")

        charisma_add = int(input("# "))

        items.charisma.points += charisma_add

        print("Time for intelligence.")

        intelligence_add = int(input("# "))

        items.intelligence.points += intelligence_add

        print('Last but not least it is time for Luck.')

        luck_add == int(input("# "))

        items.luck.points += luck_add

        if luck_add + intelligenc_add + swiftness_add + strength_add + charisma_add > 10:
            print(dedent("""No you can't have more than 10 points to add to your stats
            you greedy bastard!"""))

        else:
            print("Anything else before we move on?")

            answer == input("#")

            if answer == 'All':
                print("Oh, your to cool.")
                return 'Completed'

            else:
                print(dedent("""Nope not a combo kid try again!"""))
                return 'CompletedOne'


class NormandyBeach(Room):
    def enter(self):
        pass


class NormandyBeachHell(Room):
    def enter(self):
        pass


class NormandySafePlace(Room):
    def enter(self):
        pass


class DamnMachineGunner(Room):
    def enter(self):
        pass


class AmbushFoxHole(Room):
    def enter(self):
        pass


class Evation(Room):
    def enter(self):
        pass


class Captured(Room):
    def enter(self):
        pass


class StayQuiet(Room):
    def enter(self):
        pass


class Torcher(Room):
    def enter(self):
        pass


class Friend(Room):
    def enter(self):
        pass


class Rescued(Room):
    def enter(self):
        pass


class Muddy(Room):
    def enter(self):
        pass


class Clever(Room):
    def enter(self):
        pass


class EscapedFree(Room):
    def enter(self):
        pass


class EnemyLines(Room):
    def enter(self):
        pass


class StayQuiet(Room):
    def enter(self):
        pass


class Attic(Room):
    def enter(self):
        pass


class Rats(Room):
    def enter(self):
        pass


class Road(Room):
    def enter(self):
        pass


class ToParis(Room):
    def enter(self):
        pass


class Completed(Room):  # end game except for bonus rounnd
    def enter(self):
        print("Well you beat the game! Thank great!")

        print("Any last words before we end?")

        choice = input("# ")

        if choice == 'All':  # or if all stats are 100
            print("You get to go to a bonus round!")
            return 'Atomic_Jepoardy'

        else:
            print("""Well at least you finished the game.
            Go home now solder your service is over.""")
            exit(1)


class Atomic_Jepoardy(Room):  # bonus round

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
            print(dedent("Let us begin!"))

            print(dedent(Board))

            print("Sorry not completed yet still under construction!")
            exit(1)


class Map(object):

    rooms = {
        "level_one_intro": LevelOneIntro(),  # start of level one
        "sgt's_office": SgtsOffice(),
        "welcome_base_camp": WelcomeBaseCamp(),
        "Minor_training": MinorTraining(),
        "Path_to_war": PathToWar(),
        "Ship": Ship(),
        "completed_level_one": CompletedOne(),  # End of level one Base camp

        "arrival at normandy": NormandyBeach(),  # start of level two
        "hell_on_beach": NormandyBeachHell(),
        "quick_and_easy": NormandySafePlace(),
        "damn_machine_gunner": DamnMachineGunner(),
        "ambush": AmbushFoxHole(),  # two branch off this one
        "captured": Captured(),
        "torcher": Torcher(),  # three  branch off this one
        "afriend": Friend(),  # starts first branch
        "rescued": Rescued(),
        "muddy": Muddy(),  # end of branch
        "clever_solder": Clever(),  # start of branch two
        "escaped_and_free": EscapedFree(),
        "enemy_lines": EnemyLines(),
        "evation": Evation(),  # this one is the other
        "stay_quiet": StayQuiet(),
        "Attic": Attic(),
        "rats": Rats(),
        "the_road": Road(),
        "to_paris": ToParis(),  # end of level two


        "completed": Completed(),   # completed the game
        "Atomic_Jepoardy": Atomic_Jepoardy(),  # bonus round

        "Death": Death(),
        "discharged": Discharged()
    }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.rooms.get(room_name)
        return val

    def first_room(self):
        return self.next_room(self.start_room)
