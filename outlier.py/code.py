import random as rd
import matplotlib.pyplot as mplt
import pandas as pd

namesList = [
    "James",
    "Icardi",
    "Rivero",
    "Rafa",
    "John",
    "David"
]

nameDf = pd.DataFrame({'names': namesList})

def gift():
    personGives = namesList.copy()
    personGets = namesList.copy()
    random_permutation = rd.sample(personGets, len(personGets))
    couples = list(zip(personGives, random_permutation))

    # Check for self-gifts and reassign if necessary
    for i, (giver, receiver) in enumerate(couples):
        if giver == receiver:
            # Swap receiver with the next person in the list
            if i < len(couples) - 1:
                receiver = couples[i+1][1]
                couples[i] = (giver, receiver)
                couples[i+1] = (couples[i+1][0], giver)
            else:
                # If we're at the end of the list, swap with the first person
                receiver = couples[0][1]
                couples[i] = (giver, receiver)
                couples[0] = (couples[0][0], giver)

    for giver, receiver in couples:
        print(f"{giver} will give a gift to: {receiver}")

    return couples

couples = gift()

mplt.figure(figsize=(10, 6))
left_x, right_x = -1, 1
y_positions = list(range(len(couples)))

for j, (giver, receiver) in enumerate(couples):
    mplt.text(left_x, y_positions[j], giver, ha='center', va='center', fontweight='bold', color="blue")
    mplt.text(right_x, y_positions[j], receiver, ha='center', va='center', fontweight='bold', color="green")

    mplt.arrow(left_x, y_positions[j], 2, 0, length_includes_head=True, color='red', head_width=0.1)

mplt.xlim(-2, 2)
mplt.axis('off')

mplt.show()