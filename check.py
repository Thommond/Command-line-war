import char

# this class will check if the input from the player is with complience of the listed rules


class StatsCheck(object):
    def __init__(self):
        self.strength = char.strength.amount
        self.charisma = char.charisma.amount
        self.luck = char.luck.amount
        self.swiftness = char.swiftness.amount
        self.intelligence = char.intelligence.amount
        self.amount = amount

    def check(self, stat, amount):
        self.amount = amount
        if stat.strength + stat.charisma + self.luck + stat.swiftness + stat.intelligence == self.amount:
            return True

        else:
            print('what?')
            # value.number_check()

    def number_check(self, stat):
        print("Under construction")
        # if a value is not a number
        # do this
