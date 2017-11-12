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
There are meats, vegetables, and an abundance of drinks and desserts.
The CABINETS are locked, but you easily find the key.
A small paring KNIFE sits on the countertop.
AHEAD, you see a large stone face, a Moai.
""",
"""
At its feet, you pet bunnies and drop off your goods as an offering to the great Nui!
The face, Nui, tells you that the bunnies are named
TIMMY, ALPHIE, and DOODLEBUG.""",
"""
----------
YAY! You collected stuff and freed the bunnies!
"""
]

error = ['''
Your answer was invalid.
Currently, you must restart the game,
we will be adding a restart feature soon.
''', """Thank you for playing""", """You've reached the end of the game."""]

items = {
    'frog' : ["""You have found a frog.\nIt doesn't like you,\nbut you put it in your pocket anyway"""],
    'staff' : ["""A staff sits beside the altar,calling your name. \nYou pick it up and are immediately reminded of an old man \nyou once called a bad name because of his cane. \nYou feel regret, as  you should."""] ,
    'small commander' : ["""You find a small figurine of a war leader, \na commander, if you will.\nHe is clothed in a loin cloth and is carrying\na smaller version of a staff, his fist held high.\nYou put him in your pocket, never to be seen again.\nHis people miss him. They're lost without him.\nYou should feel bad."""],
    'glowing cube' : ["""The glowing cube calls to you in a strange languag\nthat sounds like a series of numbers\nYou cannot understand the cube\nbut it seems like it's from the future\nYou steal it because what else are you going to do with it?""" ],
    'drum' : []"""You found a drum. Just a drum.\nYou hit the top of it and it makes noise.\nWoo.\nYou might start a dance party, or a hippie convention.\nWho knows?"""],
    'knife' : ["""You find a small knife on the counter of the kitchen.\nIt appears to have been used to cut up vegetables,\nbut could be used in a very small knife fight,\nor for cutting food.\nBetter be careful.\nDon't run with it."""],
    'treats' : ["""The cabinet contains treats,\nobviously meant for a small animal of some kind.\nBetter take some, never know what you'll need to bribe."""],
    'Timmy' : ["""Timmy has one flopped over ear\nHe also really likes treats\nBetter give him some treats."""],
    'Alfie' : ["""Alfie has one flopped over ear\nand is almost a mirror image of his brother, Timmy\nDoes Alfie like treats, too?"""],
    'Doodle' : ["""Doodle is very much larger than the boys\nand is twice as sassy\nBribery is encouraged."""]}

# RoomDataStructure
# 0 = roomdescription
# 1 = roomchoicesint
# 2 = roomchoicesdict

housekeeping = [roomdescriptions[0], 1, {'YES' : 'outside', 'NO' : 'housekeeping'}]

outside = [roomdescriptions[1], 4, {'POND' : 'frog', 'OPEN' : 'entryway', 'BACK' : 'housekeeping', 'AHEAD' : 'entryway' }]

entryway = [roomdescriptions[2], 5, { 'ARCH': 'office', 'ALTAR' : 'staff', 'TABLE' : 'small commander', 'AHEAD': 'kitchen', 'BACK' : 'outside'}]

office = [roomdescriptions[3], 4, {'BOX' : 'glowing cube', 'DRUM' : 'drum', 'FORWARD' : 'kitchen', 'BACK' : 'entryway'}]

kitchen = [roomdescriptions[4], 4, {'CABINETS': 'treats', 'KNIFE': 'knife', 'AHEAD' : 'tikialtar', 'BACK' : 'office'}]

tikialtar = [roomdescriptions[5], 0, {'DOODLEBUG' : 'Doodle', 'TIMMY' : 'Timmy', 'ALPHIE' : 'Alfie', 'BACK' : 'kitchen'}]

roommap = {'housekeeping': housekeeping,
           'outside' : outside,
           'entryway' : entryway,
           'office' : office,
           'kitchen' : kitchen,
           'tikialtar' : tikialtar
           }
