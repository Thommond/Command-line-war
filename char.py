# To make all the stats
class Stat(object):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


health = Stat('health', 100)

swiftness = Stat('swiftness', 0)

luck = Stat('luck', 0)

strength = Stat('Strength', 0)

intelligence = Stat('Intelligence', 0)

charisma = Stat('Charisma', 0)

rank = Stat('Pvt', 0)
