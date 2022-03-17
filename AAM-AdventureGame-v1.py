page = 0
pages = ["You are sleeping. Do you want to wake up?\n0 for Yes, 1 for No\n", "You are awake. You immediately regret this decision. where do you go?\n0 to go Outside, 1 to get food from the Kitchen\n",
         "You're just going to keep sleeping? I don't blame you to be honest. Sure, you can just keep sleeping\n0 to continue\n", "lazy end,",
         "You are outside", "after preparing food for yourself, you now have food.\nwhere do you go now?\n0 for Back to sleep, 1 for Outside\n"]
answers = [[1, 2], [4, 5], [3], [], [], [2, 4]]
injury = 0
answer = -1
items = ["a brain",""]
harm = [0,0,0,0,0,0,0,0,0,0,0,0,0]
actions = []
consequences = []
itemLocations = {5:"food"}
requirements = ["","a brain","","","","","","","","",""]
injuryReq = [10,10,10,10,10,10,10,10,10,10,10]
endings = {3:"'lazy'"}
while page not in endings:
    while True:
        if page in actions:
            page = consequences[page]
        try:
            answer = int(input(pages[page]))
            if answer + 1 <= len(answers[page]):
                if requirements[answers[page][answer]] in items:
                    if injury >= injuryReq[answers[page][answer]]:
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
            print("Good behavior would be greatly preferable here")
    page = answers[page][answer]
    if harm[page] != 0:
        injury += harm[page]
        print(f"this action has injured you {10 - injury}/10")
    if page in itemLocations:
        items.append(itemLocations[page])
        print(f"{itemLocations[page]} obtained!")
    if injury >= 10:
        print("You fucking died. L.")
        break
else:
    print(f"wow! you win! you get the {endings[page]} ending!")