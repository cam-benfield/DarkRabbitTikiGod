import game_rooms_v1

class Room(object):

    def __init__(self, room):
        current_room = room
        self.current_room_check(current_room)

    def current_room_check(self, current_room):
        currentroomdata = game_rooms_v1.roommap[current_room]
        self.print_room_text(currentroomdata)

    def print_room_text(self, current_room_data):
        print current_room_data[0]
        self.room_choices(current_room_data)

    def room_choices(self, current_room_data):
        numofchoices = current_room_data[1]
        if numofchoices > 0:
            choiceoptions = current_room_data[2]
            choice = raw_input('>>').upper()
            nextstep = choiceoptions.get(choice, None)
            if not nextstep:
                print game_rooms_v1.error[0]
            elif nextstep:
                self.next_room_check(nextstep)
        else:
            print error[1]

    def next_room_check(self,nextroom):
        Room(nextroom)




class Character(object):

    def __init__(self):
        self.inventory = []
        self.characterinfo = {}
        self.character_name()

    def character_name(self):
        print "What is your name, young traveler?"
        charactername = raw_input('>> ')
        self.characterinfo['name'] = charactername
        print "Thanks for playing %s" % self.characterinfo['name']
        pass

    def inventory_check(itemcheck):
        if itemcheck.upper() in inventory:
            return True
        else:
            return False

    def inventory_add(itemcheck):
        if itemcheck.upper() in inventory:
            print "You already have this item."
        else:
            pass

    def inventory_print(self):
        for item in inventory:
            print item

def start_game():
    print "game is starting"
    Character()
    Room('housekeeping')
