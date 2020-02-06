
class GameEngine(object):  # run the game
    def __init__(self, room_map):
        self.room_map = room_map

    def start(self):
        current_room = self.room_map.first_room()
        last_room = self.room_map.next_room('Completed')

        while current_room != last_room:
            next_room_name = current_room.enter()
            current_room = self.room_map.next_room(next_room_name)

        current_room.enter()
