page = 0
pages = ["You are sleeping. Do you want to wake up?\n0 for Yes, 1 for No\n", "You are awake. You immediately regret this decision. where do you go?\n0 to go Outside, 1 to get food from the Kitchen\n",
         "You're just going to keep sleeping? I don't blame you to be honest. Sure, you can just keep sleeping\n0 to continue\n", "lazy end,",
         "You are outside. Where do you go?\n0 to go to the village, 1 to go to the forest\n", "after preparing food for yourself, you now have food.\nwhere do you go now?\n0 for Back to sleep, 1 for Outside\n",
         "You walk down the path to a nearby village\non the way, you walk past an old man who lives in the outskirts of the village.\nthe old man beckons to you, wha tdo you do?\n0 to approach, 1 to ignore, 2 to split his skull open with an axe.\n",
         "you walk to the edge of the forest, and find an axe lodged in a fallen log, where do you go?\n0 to walk along the edge of the forest to the mountain, 1 to go deeper into the forest\n2 to walk the other way along the edge to the lake, 3 to go back the way you came and walk to the village\n"
         ,"you walk toward the old man, he takes you into his house and leads you into his basement.\n0 to continue\n","you ignore the old man and walk to the village.\n0 to continue\n","you drive the axe into his head and he dies.\nhe struggles and you are injured in the fight.\n0 to continue\n","you notice you are standing on a trapdoor, but its too late, the old man pulls a lever and you drop into a big meat grinder!\nBYE BYE\n0 to continue\n"
         ,"you are at the village, \n0 to go the the shady alleyway, 1 to go to the funny looking tower, 2 to go to the store\n","at mountain\n","deep forest\n","at lake\n","in old man home, you rob his house and find a strange ceremonial dagger\n0 to continue\n","meat grinder ending","You walk through the alleyway and find a starving man by the side of the road, he asks for food\n0 to give food, 1 to ignore\n","You climb the tower and find a botle of some kind of medicine\nthere is nothing else to do\n0 to continue\n","you are in the store, what do you buy?","In the store you see policemen in the store, they appear to bve investigating a murder\nthey see you and they know what you have done.\n0 to accept your fate, 1 to kill them with an axe\n"
         ,"arrested end","you slaughter the policemen with your trusty axe\nkilling people with your axe is actually quite fun\n0 to flee to the forest, 1 to keep having a fun time:)\n","You steal a sword from the shop and flee to the forest\n0 to continue\n","you run around town butchering people with your axe!\nwhat fun!\n0 to continue\n","mass murder end","he thanks you for your food and leads you down the alley to a shady building\n0 to continue\n","he screams and lunges at you, ripping out your internal organs.\n#ripbozo\n0 to continue\n","eviscerated end","shady building"]
answers = [[1, 2], [4, 5], [3], [], [6, 7], [2, 4], [8, 9, 10], [13, 14, 15, 6], [11], [12], [16], [17], [18, 19, 20], [], [], [], [12], [], [27, 28], [], [], [22, 23], [], [24, 25], [7], [26], [], [30], [29]]
injury = 0
answer = -1
strAnswer = ""
items = ["","a brain"]
harm = [0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
consequenceList = {10:20, 24:6}
actions = []
consequences = {20:21, 6:7}
itemLocations = {5:"food", 7:"axe", 16:"dagger", 24:"sword", 19:"medicine"}
requirements = ["","a brain","","","","","","","","","axe","","","","","","","","","","","","","axe","","","","food","","","","","","",""]
injuryReq = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,0,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
endings = {3:"'lazy'",17:"'meat grinder'", 22:"'arrested'", 26:"'mass murderer'", 29:"'eviscerated'"}
while page not in endings:
    while True:
        if page in actions:
            page = consequences[page]
            print("Previous actions have caught up with you.")
        strAnswer = str(input(pages[page]))
        try:
            answer = int(strAnswer)
            if answer + 1 <= len(answers[page]):
                if requirements[answers[page][answer]] in items:
                    if injury <= injuryReq[answers[page][answer]]:
                        break
                    else:
                        injury += 2
                        print(f"You are too injured to do this, and have become even more injured in your attempt {10 - injury}/10")
                        if injury >= 10:
                            break
                else:
                    print(f"sorry, you need {requirements[answers[page][answer]]} to perform that action.")
            else:
                print("that wasn't an option")
        except ValueError:
            if strAnswer == "inv":
                print("Inventory contains:")
                for i in range(1,len(items)):
                    print(items[i])
            else:
                print("Invalid input. Please either input 'inv' to display current inventory, or one of the suggested numbers to progress the game")
    page = answers[page][answer]
    if page in consequenceList:
        actions.append(consequenceList[page])
    if harm[page] != 0:
        injury += harm[page]
        print(f"this action has injured you. {10 - injury}/10")
    if page in itemLocations:
        items.append(itemLocations[page])
        print(f"{itemLocations[page]} obtained!")
    if injury >= 10:
        print("You fucking died. L.")
        break
else:
    print(f"wow! you win! you get the {endings[page]} ending!")
