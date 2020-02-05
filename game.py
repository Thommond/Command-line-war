from sys import exit
from sys import dedent


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
        "completed": Completed()
        # start level two here!
    }

    deaths = {
        "Tank": Tank(),
        "Rifle": Rifle(),
        "Disease": Disease(),
        "Starvation": Starvation(),
        "Drown": Drown()
    }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Mapper.rooms.get(room_name)
        return val

    def death_room(self, death_name):
        val = Mapper.death.get(death_name)

    def first_room(self):
        return self.next_room(self.start_room)
