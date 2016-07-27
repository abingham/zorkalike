# This is a version of the original zorkalike.py with the addition of a simple
# inventory system. Two dictionaries - room_inventories and player_inventory -
# keep track of where things are.

from sys import exit

# This dictionary maps room names to their current inventory. The different
# room functions may modify the values in here (and add things to the player
# inventory) based on different choices.
room_inventories = {
    'gold': 500,
}

# This is the player inventory. Different room functions may modify it based on
# player choices.
player_inventory = {
    'gold': 0,
    'items': []
}

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input(">")

    # Here we use exception handling to try converting "choice" into an
    # integer. If the conversion fails, it throws an exception of type
    # ValueError which we catch and handle.
    try:
        how_much = int(choice)
    except ValueError:
        dead("Man, learn to type a number.")

    if how_much > room_inventories['gold']:
        print "There's not that much good in the room! Try again, moron."
        gold_room()
    elif how_much < 50:
        print "Nice, you're not greedy, you win!"

        # Update the player inventory
        player_inventory['gold'] += how_much

        # Reduce the room inventory.
        room_inventories['gold'] -= how_much
        exit(0)
    # elif choice == "count the gold":
        count = 1
        while count < 501:
            print(count)
            count = count + 1
    elif choice == "inventory":
        print player_inventory
    else:
        dead("You greedy bastard!")


# This is a test room to debug the inventory functions

def tool_room():
    print "You walk into a room with a table in the middle."
    print "On the table are 4 tools. A screwdriver, a hammer, pliers, and a saw."
    screwdriver_taken = False
    hammer_taken = False
    pliers_taken = False
    saw_taken = False

    while True:
        choice = raw_input(">")

        if choice == "take screwdriver" and not screwdriver_taken:
            player_inventory['items'].append('screwdriver')
            screwdriver_taken = True
            print "You pick up the screwdriver."
        elif choice == "drop screwdriver" and screwdriver_taken:
            player_inventory['items'].remove('screwdriver')
            screwdriver_taken = False
            print "You drop the screwdriver back on the table."
        elif choice == "take hammer" and not hammer_taken:
            player_inventory['items'].append('hammer')
            hammer_taken = True
            print "You pick up the hammer."
        elif choice == "drop hammer" and hammer_taken:
            player_inventory['items'].remove('hammer')
            hammer_taken = False
            print "You drop the hammer back on the table."
        elif choice == "take pliers" and not pliers_taken:
            player_inventory['items'].append('pliers')
            pliers_taken = True
            print "You pick up the pliers."
        elif choice == "drop pliers" and pliers_taken:
            player_inventory['items'].remove('pliers')
            pliers_taken = False
            print "You drop the pliers back on the table."
        elif choice == "take saw" and not saw_taken:
            player_inventory['items'].append('saw')
            saw_taken = True
            print "You pick up the saw."
        elif choice == "drop saw" and saw_taken:
            player_inventory['items'].remove('saw')
            saw_taken = False
            print "You drop the saw back on the table."
        elif choice == "inventory":
            print player_inventory
        elif choice == "use hammer" and hammer_taken:
            print "You hammer your little heart out and pass out from the exertion."
            player_inventory['items'].remove('hammer')
            print "\nPOOF!\n"
            start()
        elif choice == "use screwdriver" and screwdriver_taken:
            print "You use the screwdriver to open the lock to the room you came from."
            player_inventory['items'].remove('screwdriver')
            cthulhu_room()
        elif choice == "use pliers" and pliers_taken:
            print "You're doing great with those pliers, keep it up!"
            player_inventory['items'].remove('pliers')
            print "\nPOOF\n"
            gold_room()
        elif choice == "use saw" and saw_taken:
            print "You saw the legs off the table and learn to juggle. Good job!"
            player_inventory['items'].remove('saw')
            saw_taken = False
            print "\nPOOF!\n"
            herring_pit()
        else:
            print "Choose a tool from the table, tool."

def herring_pit():
    print """This room has a deep pit running the width of the room. The pit is
filled with hungry herrings. On the ground in front of you is a long board.
There is a door on the wall across the pit."""
    board_taken = False
    board_across = False

    while True:
        choice = raw_input(">")

        if choice == "back":
            start()
        elif choice == "take board":
            player_inventory['items'].append('board')
            board_taken = True
        elif choice == "jump across pit":
            dead("Those are some hungry herrings! (your last thoughts as the herrings eat you)")
        elif choice == "put board across pit" and board_taken:
            print "You place the board across the pit and walk to the other side."
            print "You are now standing in front of the door on the other side of the pit."

            board_across = True
            board_taken = False
        elif choice == "turn around" and board_across:
            dead("You lose your balance while turning around and fall into the pit. The herrings lose their appetite at smelling your stench and you all die of starvation.")
        elif choice == "open door" and board_across:
            food_room()
        elif choice == "inventory":
            print player_inventory
        else:
            dead("You forget what you are doing and start holding your breath for as long as you can.")

def food_room():
    print "You enter a room and the door locks behind you."
    print "In the middle of the room is a table with 5 plates."
    print "On each plate there is a different meal."

    while True:
        choice = raw_input(">")

        if "first plate" in choice:
            print "Grilled Octopus"
        elif "second plate" in choice:
            print "Caviar"
        elif "third plate" in choice:
            print "Chocolate Cake"
        elif "fourth plate" in choice:
            print "Bear Claw pastry"
        elif "fifth plate" in choice:
            print "Macaroni and Cheese"
        elif choice == "eat Grilled Octopus":
            print "It's a bit chewy, but super yummy!"
            print "\nPOOF!\n"
            cthulhu_room()
        elif choice == "eat Caviar":
            "It tastes like the sweat off a herring used to fell a tree."
            print "\nPOOF!\n"
            herring_pit()
        elif choice == "eat Chocolate Cake":
            print "I love chocolate at the beginning of anything I do."
            print "\nPOOF!\n"
            start()
        elif choice == "eat Bear Claw pastry":
            print "This would better if it didn't contain whole bear claws."
            print "\nPOOF\n"
            bear_room()
        elif choice == "eat Macaroni and Cheese":
            print "Mmmmm, food of the gods...."
            print "\nPOOF!\n"
            gold_room()
        elif choice == "inventory":
            print player_inventory
        else:
            print "It all looks so good that you can't decide...."
            cthulhu_room()


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input(">")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it."

            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        elif choice == "inventory":
            print player_inventory
        else:
            print "I have no idea what that even means."

def cthulhu_room():
    print "Here you see the great, evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "In your head you hear, \"What is the answer to Life, the Universe, and Everything?\""
    print "Do you answer the question, eat your own head, or flee?"
    cthulhu_moved = False

    while True:

        choice = raw_input(">")

        if "flee" in choice:
            start()
        elif "head" in choice:
            dead("Well, that was tasty.")
        elif choice == "42" and not cthulhu_moved:
            print "\"You have chosen.....wisely. You may pass.\""
            print "Chtulhu moves to the side and reveals a door."
            cthulhu_moved = True
        elif choice == "inventory":
            print player_inventory
        elif choice == "open door" and cthulhu_moved:
            tool_room()

        else:
            cthulhu_room()

def dead(why):
    print why, "Try again!"
    print 'Current inventory: %s' % player_inventory
    exit (0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left and ahead."
    print "Which one do you take?"

    choice = raw_input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "ahead":
        herring_pit()
    elif choice == "inventory":
        print player_inventory
    else:
        dead("You stumble around the room until you starve.")

start()
