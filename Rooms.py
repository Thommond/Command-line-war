from sys import exit
from textwrap import dedent
from items import *
from game import *


class Room(object):

    def enter(self):
        print("This is the start of creating many rooms")
        exit(1)


class LevelOneIntro(room):
    def enter(self):
        print(dedent("""
        Welcome! Solder what is your name?
        """))

        name = input("# ")

        if name == 'brian' or 'Brian':
            return "completed"

        print("Okay, {name} you have been drafted!")
        print(dedent("""Your family is worried sick. World war
        two is raging across europe, you turned 18 just
        weeks ago. The military needs extra troops on the
        ground agaist the Nazi's. The Nazi's have infested
        Europe like a cockroch colony. You will be assigned
        to Unit 179. """))

        print('Any thoughs before we move on?')

        thoughts = input('# ')

        if (thoughts != ''):
            print(dedent('Good thing no one cares'))
            return "sgt's office"

        else:
            print('What? Please enter some thoughts.')


class SgtsOffice(room):
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

        print("So Strength is first. Please enter the value. It has to be more than five.")

        strength += int(input("# "))

        print('Next is Swiftness. Rules apply always.')

        swiftness += int(input("# "))

        print("Now is Charisma.")

        charisma += int(input("# "))

        print("Time for intelligence.")

        intelligence += int(input("# "))

        print('Last but not least it is time for Luck.')

        luck += int(input("# "))

        print(dedent(f"""Okay, so you want {strength} strength, {swiftness} swiftness, {charisma} charisma, {intelligence} intelligence , and
        {luck} luck. Is that final? """))

        choice = input("# ")

        if choice = "yes":
            return 'welcome base camp'

        else:
            print('What? you say yes if yes and no to try again.')
            return "sgt's office"


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
            gun = Item('rifle', True)
            print("""Okay solder 8 weeks will be over in no time. You will
            have plenty of friends and plenty of skills when we are done.""")

            return 'Minor training'

        elif choice == 'B':
            gun = Item('sniper', True)
            print(dedent("""Oh, we are kind of short on snipers so looks like your getting shipped
            in a week instead."""))

            return 'Path to war'

        elif choice == 'C':
            gun = Item('machine gun', True)
            print(dedent("""Okay, so you like to shoot lots of bullets I can respect that.
            We will not need to keep you to long but you will need the extra training. """))

            luck += 5

            return 'Minor training'

        else:
            return 'welcome base camp'


class MinorTraining(Room):
    def enter(self):
        pass


class PathToWar(Room):
    def enter(self):
        pass


class Ship(Room):
    def enter(self):
        pass


class CompletedOne(Room):
    def enter(self):
        pass


class NormandyBeach(Room):
    def enter(self):
        pass


class NormadyBeachHell(Room):
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
