page = 0
pages = ["You are sleeping. Do you want to wake up?\n0 for Yes, 1 for No\n", "You are awake. You immediately regret this decision. where do you go?\n0 for Outside, 1 for Kitchen\n",
         "You're just going to keep sleeping? I don't blame you to be honest. Sure, you can just keep sleeping\n0 to continue\n", "lazy end,",
         "You are outside", "after preparing food for yourself, you now have food.\nwhere do you go now?\n0 for Back to sleep, 1 for Outside\n"]
answers = [[1, 2], [4, 5], [3], [], [], [2, 4]]
answer = -1
items = ["a brain",""]
itemLocations = {5:"food"}
requirements = ["","a brain","","","","","","","","",""]
endings = {3:"'lazy'"}
while page not in endings:
    while True:
        try:
            answer = int(input(pages[page]))
            if answer + 1 <= len(answers[page]):
                if requirements[answers[page][answer]] in items:
                    break
                else:
                    print(f"sorry, you need {requirements[answers[page][answer]]} to perform that action.")
            else:
                print("that wasn't an option")
        except ValueError:
            print("Good behavior would be greatly preferable here")
    page = answers[page][answer]
    if page in itemLocations:
        items.append(itemLocations[page])
        print(f"{itemLocations[page]} obtained!")
print(f"wow! you win! you get the {endings[page]} ending!")
