from DarkRabbitTikiGod import game_rooms_v1

class Character(object):

    def character_name(self): # Creates Character Name - For future use
        print("What is your name, young traveler?")
        charactername = input('>> ')
        self.characterinfo['name'] = charactername
        print("Thanks for playing %s" % self.characterinfo['name'])

    def inventory_check(self, itemcheck): # UNUSED - future dev needed
        if itemcheck in self.inventory:
            return True
            print("You have %s in your inventory." % itemcheck)
        else:
            return False
            print("You do not have the needed item in your inventory.")
            self.inventory_print()

    def inventory_add(self, itemcheck): # Checks items in inventory, then adds items that are not in inventory
        if itemcheck in self.inventory:
            print("You already have this item.")
        else:
            self.inventory.append(itemcheck)
            print("-" * 20)
            itemdata = game_rooms_v1.items[itemcheck]
            print(itemdata[0])
            self.inventory.sort()
            print("You have added %s to your inventory." % itemcheck)
            self.inventory_print()

    def inventory_print(self): # Prints inventory
        print("You now have the following in your inventory:")
        for item in self.inventory:
            print(item)

    def game_pause(self):
        print("Press ENTER to continue the game.")
        input('ENTER')

class Room(Character):

    def __init__(self, room):
        current_room = room
        self.inventory = []
        self.characterinfo = {}
        charname = self.characterinfo.get('name', None)
        if not charname:
            self.character_name()
        self.current_room_check(current_room)

    def current_room_check(self, current_room):
        currentroomdata = game_rooms_v1.roommap[current_room]
        self.print_room_text(currentroomdata)

    def print_room_text(self, current_room_data):
        print(current_room_data[0])
        self.room_choices(current_room_data)

    def room_choices(self, current_room_data):
        numofchoices = current_room_data[1]
        if numofchoices > 0:
            choiceoptions = current_room_data[2]
            for key, value in list(game_rooms_v1.standardchoices.items()):
                choiceoptions[key] = value

            choice = input('>>').upper()

            nextstep = choiceoptions.get(choice, None)

            if not nextstep:
                print(game_rooms_v1.error[0])
                self.print_room_text(current_room_data)
            elif nextstep in game_rooms_v1.items:
                self.inventory_add(nextstep)
                self.print_room_text(current_room_data)
            elif 'inventory' in nextstep:
                self.inventory_print()
                self.game_pause()
                self.print_room_text(current_room_data)
            elif 'exit' in nextstep:
                exit(1)
            elif nextstep:
                self.next_room_check(nextstep)
        else:
            print(game_rooms_v1.error[1])

    def next_room_check(self,nextroom):
        self.current_room_check(nextroom)

def start_game():
    room = Room('housekeeping')
