# To make all the stats
class Stat(object):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

# for our player


class PlayerStat(Stat):
    def __init__(self, name, points):
        self.name = name
        self.points = points

    # for player health


class PlayerHealth(Stat):
    def __init__(self, name, health):
        self.name = name
        self.health = health

# for items like a rifle which the player uses and not is


class Item(Stat):
    def __init__(self, name, amount):

        self.amount = amount

    def intial_check(self, amount):
        self.amount = amount
        # need to prevent people from typing in any value they want for their stats


# creating an instance
# the below will impact the choices of the player depending on their stats.
# they can recieve warnings, get killed, be prevented from a choice and more
# depending on their stats
gas_mask = Item('gas mask', True)

gun = Item('rifle', True)

rations = Item('rations', 10)

health = PlayerHealth('health', 100)

swiftness = PlayerStat('swiftness', 0)

luck = PlayerStat('luck', 0)

strength = PlayerStat('Strength', 0)

intelligence = PlayerStat('Intelligence', 0)

charisma = PlayerStat('Charisma', 0)

rank = PlayerStat('Pvt', 0)

# for future enemies with their own stats


class Enemies(object):
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health
