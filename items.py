
# for items like a rifle which the player uses and not is


class Item(object):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


        # creating an instance of the item class for Items such as rifle
gas_mask = Item('gas mask', True)

gun = Item('rifle', True)

rations = Item('rations', 10)
