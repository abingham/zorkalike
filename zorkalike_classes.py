"""This is an implementation of a zork-esque game using classes to implement
major elements of the game.

This is just a rough sketch, and there is a lot of space for improvement and
experimentation. For example:
* More dynamic/flexible room connection
* Allow rooms to block doors until certain actions are taken or criteria are
  met (e.g. a player has a specific object in their inventory).
* Support some notion of winning or completion that doesn't involve dying.

"""

class Room(object):
    def __init__(self,
                 description,
                 contents=None):
        # An interesting modification would be to use a dict mapping direction
        # names to rooms rather than hard-coding north, south, east, and west.
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.description = description
        self.contents = dict(contents) if contents else None

    def process_command(self, command, player):
        """Process room-specific commands.

        This is called if the command is not recognized by the standard command
        processor. It returns true of the command is handled by the room, or
        False otherwise.

        By default this function does nothing. Use subclasses to add special
        command handling.
        """
        return False

a
class LlamaRoom(Room):
    """This is a subclass of Room which contains some llamas.
    """
    def __init__(self, count):
        super(LlamaRoom, self).__init__(
            '',
            contents={'llama': count})
        self._update_description()

    def _update_description(self):
        self.description = \
            'This room is filled with %s serene llamas.' % self.contents['llama']

    def process_command(self, command, player):
        if command == 'pet llama':
            if self.contents['llama'] < 1:
                print('Unfortunately there are no llamas to pet.')
            else:
                print('The llama looks pleased and then gallops off, its mission in this dimension completed.')
                self.contents['llama'] -= 1
                self._update_description()
            return True

        return False


class BearRoom(Room):
    """A room containing a bear.
    """
    def __init__(self):
        super(BearRoom, self).__init__(
            'This rooms contains a grumpy looking bear.',
            contents={'bear': 1})

    def process_command(self, command, player):
        if command == 'pet bear':
            print('The bear is not impressed and re-enacts "The Revenant" on you.')
            player.alive = False
            return True
        return False


class Player(object):
    def __init__(self):
        self.inventory = {}
        self.alive = True


class Game(object):
    def __init__(self, current_room, player):
        self.current_room = current_room
        self.player = player


def process_standard_commands(command, game):
    """Process commands which are common to all rooms.

    This includes things like following directions, checking inventory, exiting
    the game, etc.

    Returns true if the command is recognized and processed. Otherwise, returns
    false.

    """
    if command == 'north':
        room = game.current_room.north
        if room:
            game.current_room = room
        else:
            print('There is no room to the north')
    elif command == 'south':
        room = game.current_room.south
        if room:
            game.current_room = room
        else:
            print('There is no room to the south')
    elif command == 'east':
        room = game.current_room.east
        if room:
            game.current_room = room
        else:
            print('There is no room to the east')
    elif command == 'west':
        room = game.current_room.west
        if room:
            game.current_room = room
        else:
            print('There is no room to the east')
    elif command == 'description':
        print(game.current_room.description)
    elif command == 'inventory':
        print('Inventory %s' % game.player.inventory)
    elif command == 'quit':
        game.player.alive = False
    else:
        # unrecognized command
        return False

    return True


def print_room_details(room):
    """Print the details of the current room.
    """
    print(room.description)
    if room.north:
        print('There is a door to the north.')
    if room.east:
        print('There is a door to the east.')
    if room.south:
        print('There is a door to the south.')
    if room.west:
        print('There is a door the west.')


def main_loop(game):
    """Process commands from the user until they die.
    """
    while True:
        if not game.player.alive:
            print('You are dead.')
            return

        print('')
        print_room_details(game.current_room)
        command = raw_input('> ')
        handled = process_standard_commands(command, game) \
            or game.current_room.process_command(command, game.player)
        if not handled:
            print('unrecognized command!')


def make_game():
    """Construct a game object.
    """
    start_room = Room('You are in a dark room.')
    llama_room = LlamaRoom(42)
    bear_room = BearRoom()

    # Right now we have to manually make sure that room connect reasonably,
    # i.e. that going north from one room means you can go south from the
    # other. A useful modification would be to add functions which "connect"
    # rooms, e.g. connect_rooms(room_a, room_b, 'south') or something like
    # that.
    start_room.north = llama_room
    llama_room.south = start_room

    start_room.east = bear_room
    bear_room.west = start_room

    game = Game(start_room, Player())
    return game

# Create a game and start processing commands.
main_loop(make_game())
