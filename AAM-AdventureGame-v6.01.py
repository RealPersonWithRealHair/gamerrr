page = 0
# the pages list contains the writing in the story
pages = ["You are sleeping. Do you want to wake up?\n0 for Yes, 1 for No\n",
         "You are awake. You immediately regret this decision. where do you go?\n"
         "0 to go Outside, 1 to get food from the Kitchen\n",
         "You're just going to keep sleeping? I don't blame you to be honest. Sure, you can just keep sleeping\n"
         "0 to continue\n",
         "lazy end,", "You are outside. Where do you go?\n0 to go to the village, 1 to go to the forest\n",
         "after preparing food for yourself, you now have food.\nwhere do you go now?\n"
         "0 for Back to sleep, 1 for Outside\n",
         "You walk down the path to a nearby village\n"
         "on the way, you walk past an old man who lives in the outskirts of the village.\n"
         "the old man beckons to you, wha tdo you do?\n"
         "0 to approach, 1 to ignore, 2 to split his skull open with an axe.\n",
         "you walk to the edge of the forest, and find an axe lodged in a fallen log, where do you go?\n"
         "0 to walk along the edge of the forest to the mountain, 1 to go deeper into the forest\n"
         "2 to walk the other way along the edge to the lake, 3 to go back the way you came and walk to the village\n",
         "you walk toward the old man, he takes you into his house and leads you into his basement.\n0 to continue\n",
         "you ignore the old man and walk to the village.\n0 to continue\n",
         "you drive the axe into his head and he dies.\n"
         "he struggles and you are injured in the fight.\n0 to continue\n",
         "you notice you are standing on a trapdoor, but its too late\n"
         "the old man pulls a lever and you drop into a big meat grinder!\nBYE BYE\n0 to continue\n",
         "you are at the village, \n"
         "0 to go the the shady alleyway, 1 to go to the funny looking tower, "
         "2 to go to the store, 3 to return to the forest\n",
         "You are at the mountain, 0 to climb it, 1 to leave\n",
         "deep forest\n",
         "you are at the lake.\nyou decide to do some fishing\n0 to continue\n",
         "in old man home, you rob his house and find a strange ceremonial dagger\n0 to continue\n",
         "meat grinder ending",
         "You walk through the alleyway and find a starving man by the side of the road, he asks for food\n"
         "0 to give food, 1 to ignore\n",
         "You climb the tower and find a bottle of some kind of medicine\nthere is nothing else to do\n0 to continue\n",
         "you are in the store, what do you buy?\n0 to buy a sword, 1 to leave because you are poor\n",
         "In the store you see policemen in the store, they appear to bve investigating a murder\n"
         "they see you and they know what you have done.\n0 to accept your fate, 1 to kill them with an axe\n",
         "arrested end",
         "you slaughter the policemen with your trusty axe\n"
         "killing people with your axe is actually quite fun\n0 to flee to the forest, 1 to keep having a fun time:)\n",
         "You steal a sword from the shop and flee to the forest\n0 to continue\n",
         "you run around town butchering people with your axe!\nwhat fun!\n0 to continue\n",
         "mass murder end",
         "he thanks you for your food and leads you down the alley to a shady building\n0 to continue\n",
         "he screams and lunges at you, ripping out your internal organs.\n#ripbozo\n0 to continue\n",
         "eviscerated end",
         "You reach a dark and shady building, inside are some strange cultists, "
         "they beckon to you and then gesture to an altar.\n0 to follow them, 1 to flee\n",
         "they take out a large knife and stab you, blood splatters over the altar, "
         "they then chase you out, all the way to the forest\n0 to continue\n",
         "they chase you and stab you repeatedly with big knives\n",
         "you have had enough fishing for now and walk to the village\n"
         "on your way there a man walks up to you and demands to have your fish\n"
         "0 to give the fish, 1 to not give the fish\n",
         "he thanks you for the fish and gives you some money\n0 to continue\n",
         "he screams 'FIIIIIISHHHHHH' and tears out your lungs\n0 to continue",
         "FIIIIIIISH end", "you buy a sword and leave\n0 to continue\n",
         "the lake is blood red (why is the lake red :(((? )\n"
         "a horrific cephalopod-like beast rises from the depths, \n"
         "it is huge, and if you wish to fight, an axe will not suffice\n0 accept your fate, 1 to fight\n",
         "you are torn to bits by the great beast.\n#ripbozo\n0 to continue",
         "you fight the monster, it is a tough fight but you eventually win\n"
         "maybe you could make some calamari rings or something\n0 to continue\n",
         "cephalopod activities end", "kill squid end",
         "you eventually near the top of the mountain, you find an odd altar, but you can keep climbing to the peak\n"
         "0 to use the altar, 1 to keep climbing\n",
         "you raise your dagger and impale yourself. it hurts.\n"
         "the altar flashes red and you are temporarily blinded\n0 to continue\n",
         "it's cold. \n0 to continue\n", "hypothermia end",
         "a towering stone beast now stands before you, you cannot flee and you are already on the verge of death\n"
         "0 to surrender to fate, 1 to fight with your sword, 2 to fight with your axe\n",
         "the golem crushes your skull, \n0 to continue\n",
         "the sword cannon cut the stone, and is to light to break it, the golem crushes your skull, \n0 to continue",
         "the axe is heavy enough to break the stone, this has a chance of working, "
         "but you are badly hurt, \n0 to continue\n", "stoned end",
         "the golem raises it's fist, \n0 to dodge, 1 to counter with an axe strike\n",
         "you slip, and are brutally killed\n0 to continue",
         "you chip the golem's arm, progress is being made\nit charges at you, \n"
         "0 to stand your ground, 1 to sidestep and counter\n",
         "more stone is crushed. the fight is nearing its end\nthe golem leaps into the air\n0 to throw your axe, 1 to"
         " get away\n", "the golem crashes into the ground as the impact makes it start to crumble, 0 to finish it\n",
         "you finally shatter the stone monstrosity\n0 to continue", "golem killed end"
         ]
""" the answers list contains the different actions and connects the pages together, each list in the array represents 
a page, and each number represents a page that can be reached from that page
"""
answers = [[1, 2], [4, 5], [3], [], [6, 7], [2, 4], [8, 9, 10], [13, 14, 15, 6], [11], [12], [16], [17],
           [18, 19, 20, 7], [43, 12], [], [33], [12], [], [27, 28], [12], [37, 12], [22, 23], [], [24, 25], [7], [26],
           [], [30], [29], [], [31, 32], [7], [], [34, 35], [12], [36], [], [12], [39, 40], [41], [42], [], [],
           [44, 45], [47], [46], [], [48, 49, 50], [51], [51], [52], [], [53, 54], [51], [48, 55], [51, 56], [57], [58],
           []]
injury = 0
# injury variable is the players health, low injury is equal to high health
answer = -1
strAnswer = ""
items = ["", "a brain"]
# the list that record the player inventory
harm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 10, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# the harm list decides how much the player is injured on each page
consequenceList = {10: 20, 24: 6, 31: 15}
actions = []
consequences = {20: 21, 6: 7, 15: 38}
""" this defines how actions can have long lasting consequences, e.g, the 10: 20 in consequenceList means that if the 
player goes to page 10, the player will face consequences on page 20, and the 20: 21 in consequences means that if that
is activated, the consequence will be being sent to page 21 instead
"""
itemLocations = {5: "food", 7: "axe", 15: "fish", 16: "dagger", 24: "sword", 19: "medicine", 34: "money", 37: "sword"}
# this is where items can be found
requirements = ["", "a brain", "", "", "", "", "", "", "", "", "axe", "", "", "", "", "", "", "", "", "", "", "", "",
                "axe", "", "", "", "food", "", "", "", "", "", "", "fish", "", "", "", "", "", "sword", "", "", "",
                "dagger", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
# this is what inventory items are needed in each page
injuryReq = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 10, 10, 10, 10, 10, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
# this is how much health the player needs for each page
endings = {3: "'lazy'", 17: "'meat grinder'", 22: "'arrested'", 26: "'mass murderer'", 29: "'eviscerated'",
           36: "'FIIIIIIIIIISH'", 41: "'CEPHALOPOD ACTIVITIES'",
           42: "'dead squid'", 46: "'hypothermia'", 51: "'stoned'", 58: "'dead golem'"}
# this ends the game.
print("Welcome to my game! to play, the game will tell you your current situation, and a list "
      "of actions that you can preform.\nYou will enter in the number corresponding to the option you wish to"
      " choose.\nType 'inv' instead of a number to view your all items that you have picked up throughout"
      "the game, this includes ones that have already carried out their purpose.\nNow Begin.")
# this tells the user how to play the game
# the endings list contains each page where the game ends on. if the players current page is one of these the loop ends.
# this loop keeps the game running until the game ends
while page not in endings:
    while True:
        # this checks for consequences of past actions
        if page in actions:
            page = consequences[page]
            print("Previous actions have caught up with you.")
        strAnswer = str(input(pages[page]))
        # this asks the player what they wish to do
        try:
            answer = int(strAnswer)
            if answer + 1 <= len(answers[page]):
                if requirements[answers[page][answer]] in items:
                    if injury <= injuryReq[answers[page][answer]]:
                        break
                    else:
                        injury += 2
                        print(f"You are too injured to do this, and have become"
                              f" even more injured in your attempt {10 - injury}/10")
                        if injury >= 10:
                            break
                # this checks if what they input was allowed, or if the player health is too low
                # it also checks their inventory in case the need a specific item
                else:
                    print(f"sorry, you need {requirements[answers[page][answer]]} to perform that action.")
                    # tells the player what item they need
            else:
                print("that wasn't an option")
        except ValueError:
            if strAnswer == "inv":
                print("Inventory contains:")
                for i in range(1, len(items)):
                    print(items[i])
            # the command that displays player inventory
            else:
                print("Invalid input. Please either input 'inv' "
                      "to display current inventory, or one of the suggested numbers to progress the game")
            # error message
    page = answers[page][answer]
    if page in consequenceList:
        actions.append(consequenceList[page])
    if harm[page] != 0:
        injury += harm[page]
        print(f"this action has injured you. {10 - injury}/10")
    if page in itemLocations:
        if itemLocations[page] not in items:
            items.append(itemLocations[page])
            print(f"{itemLocations[page]} obtained!")
    if injury >= 10:
        print("You fucking died. L.")
        break
    # these change the player health and inventory based ont their page, also record actions with long term consequences
else:
    print(f"wow! you win! you get the {endings[page]} ending!")
