from sys import dedent
from game import *


class room(object):

    def enter(self):
        print("This is the start of creating many rooms")
        exit(1)


class LevelOneIntro(room):
    def enter(self):
        print(dedent("""
        Welcome! Solder what is your name?
        """))

        name = input("# ")

        if name = 'brian' or 'Brian':
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
            print('What?')


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
        

        3.
        """))
