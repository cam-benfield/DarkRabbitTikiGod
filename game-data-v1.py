class Room(object):

    def __init__(room):
        current_room = room
        print current_room

    def current_room_check():
        pass

    def print_room_text():
        pass

    def room_choices():
        pass

    def next_room_check():
        pass

class Character(object):

    def __init__():
        inventory = []
        characterinfo = {}
        self.character_name()

    def character_name():
        print "What is your name, young traveler?"
        charactername = raw_input('>> ')
        characterinfo['name'] = charactername
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



    def inventory_print():
        for item in inventory:
            print item
