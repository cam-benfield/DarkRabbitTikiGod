import game_data_v1

roomdescriptions = ["""
Welcome to the Lair of the Dark Rabbit Tiki God.
You will be exploring the lair and helping those who need your assistance.

Your instructions are as follows:
\tYou will encounter strange items, people, and creatures.
\tYour choices will be highlighted by being entirely capitalized.
\tYou must input the choice as it is typed.
\tIf there are no choices, type 'yes' or 'no'.
\tYou must remember that your choices do affect a real character
\tand may result in their mortality.

Do you understand?
""",
"""
You awaken in a clearing.
What appears to be a Polynesian home stretches out before you.
You come upon a grey wooden door
with a tiki carved in the front of it.
A small POND is to your right.
Do you OPEN the door or go BACK?
""",
"""
You enter a dark room with an ARCH to your right.
In the arch, you hear the whirring of profane rituals
intended to reveal the future.
Along the wall just ahead,
there is an ALTAR to the gods of the land.
To your left, there is a TABLE surrounded by shelves
upon shelves of small armies, intended to bring success in war.
Just AHEAD, you see a hallway that leads into darkness.
Where would you like to go?
""",
"""
The whirring that was heard upon entering gets louder.
You see a wooden BOX glowing in the distance.
As an offering to the box, there is a small DRUM
in a circle on the floor.
You inspect the room and find nothing else of consequence.
Ahead, you see a hallway that seems to lead to another room.
Do you go FORWARD or BACK?
""",
"""
You enter a room that seems to be used as a kitchen of sorts.
There are TREATS, meats, vegetables, and an abundance of drinks and desserts.
A small paring KNIFE sits on the countertop.
""",
"""
"""
]

error = ['''
Your answer was invalid.
Currently, you must restart the game,
we will be adding a restart feature soon.
''', """Thank you for playing"""]

items = ['frog', 'staff', 'small commander', 'glowing cube', 'drum', 'knife', 'treats']

# RoomDataStructure
# 0 = roomdescription
# 1 = roomchoicesint
# 2 = roomchoicesdict

housekeeping = [roomdescriptions[0], 1, {'YES' : 'outside', 'NO' : 'housekeeping'}]

outside = [roomdescriptions[1], 4, {'POND' : 'frog', 'OPEN' : 'entryway', 'BACK' : 'housekeeping', 'AHEAD' : 'entryway' }]

entryway = [roomdescriptions[2], 5, { 'ARCH': 'office', 'ALTAR' : 'staff', 'TABLE' : 'small commander', 'AHEAD': 'kitchen', 'BACK' : 'outside'}]

office = [roomdescriptions[3], 4, {'BOX' : 'glowing cube', 'DRUM' : 'drum', 'FORWARD' : 'kitchen', 'BACK' : 'entryway'}]

kitchen = [roomdescriptions[4], 4, {'TREATS': 'treats', 'KNIFE': 'knife', 'AHEAD' : 'tikialtar' 'BACK' : 'office'}]

tikialtar = [roomdescriptions[5], 0, {}]



rooms = {'housekeeping' : 'outside',
         'outside' : 'entryway',
         'entryway' : 'office',
         'office' : 'kitchen',
         'kitchen' : 'tikialtar'
         }

roommap = {'housekeeping': housekeeping,
           'outside' : outside,
           'entryway' : entryway,
           'office' : office,
           'kitchen' : kitchen,
           'tikialtar' : tikialtar
           }
