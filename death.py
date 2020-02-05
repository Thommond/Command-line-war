# This file will hold all the death scenes of the game
from Rooms import Room
deaths = {
    "Tank": Tank(),
    "Rifle": Rifle(),
    "Disease": Disease(),
    "Starvation": Starvation(),
    "Drown": Drown(),
    "Discharged": Discharged(),
    "Stupid": Stupid()
}


class Death(Room):
    def __init__(self, name, message):
        self.name = name
        self. message = message


Tank = Death('Tank', '')

# I can make death variables which I can call and print
