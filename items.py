
# for items like a rifle which the player uses and not is


class Item(object):
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


# for future enemies with their own stats
