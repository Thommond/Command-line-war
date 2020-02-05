

class GameEngine():
    def __init__(self):
        self.room_map = room_map

    def start(self):
        current_room = self.room_map.first_room()
        last_room = self.room_map.next_room('Completed')

        while current_room != last_room:
            next_room_name = current_room.enter()
            current_room = self.room_map.next_room(next_room_name)

        current_room.enter()


class Mapper(object):

    rooms = {
        "level one intro": LevelOneIntro(),  # start of level one
        "sgt's office": SgtsOffice(),
        "welcome base camp": WelcomeBaseCamp(),
        "Minor training": MinorTraining(),
        "Path to war": PathtoWar(),
        "ship": Ship(),
        "completed level one": CompletedOne(),  # End of level one Base camp

        "arrival at normandy": NormandyBeach(),  # start of level two
        "hell on beach": NormandyBeachHell(),
        "quick and easy": NormandySafePlace(),
        "damn machine gunner": DamnMachineGunner(),
        "ambush": AmbushFoxHole(),  # two branch off this one
        "captured": Captured(),
        "torcher": Torcher(),  # three  branch off this one
        "a friend": Friend(),  # starts first branch
        "rescued": Rescued(),
        "muddy": Muddy(),  # end of branch
        "clever solder": Clever(),  # start of branch two
        "escaped and free": EscapedFree(),
        "enemy lines": EnemyLines(),
        "evation": Evation(),  # this one is the other
        "stay quiet": StayQuiet(),
        "Attic": Attic(),
        "rats": Rats(),
        "the road": Road()
        "to paris": ToParis(),  # end of level two


        "completed": Completed(),  # completed the game
        "death": Death()  # dead mavn
        # start level two here!
    }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Mapper.rooms.get(room_name)
        return val

    def first_room(self):
        return self.next_room(self.start_room)
