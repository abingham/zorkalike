from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def math_room():
    print "Still working on this place."
    start()

def herring_pit():
    print """This room has a deep pit running the width of the room. The pit is
filled with hungry herrings. On the ground in front of you is a long board.
There is a door on the wall across the pit."""
    board_across = False

    while True:
        choice = raw_input(">")

        if choice == "back":
            start()
        elif choice == "jump across pit":
            dead("Those are some hungry herrings! (your last thoughts as the herrings eat you)")
        elif choice == "put board across pit":
            print "You place the board across the pit and walk to the other side."
            print "You are now standing in front of the door on the other side of the pit."

            board_across = True
        elif choice == "turn around" and board_across:
            dead("You lose your balance while turning around and fall into the pit. The herrings lose their appetite at smelling your stench and you all die of starvation.")
        elif choice == "open door" and board_across:
            food_room()
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
        elif choice == "open door" and cthulhu_moved:
            math_room()

        else:
            cthulhu_room()

def dead(why):
    print why, "Try again!"
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
    else:
        dead("You stumble around the room until you starve.")

start()
