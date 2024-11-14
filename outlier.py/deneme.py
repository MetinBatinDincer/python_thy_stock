import random as rd

import matplotlib.pyplot as mplt

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
    personGets = namesList.copy()  
    personGives = namesList.copy() 
    couples = []

    for giver in personGives:

        receiver = personGets[rd.randint(0, len(personGets) )]
        couples.append((giver, receiver))
    

    for giver, receiver in couples:
        print(f"{giver} will receive a gift from: {receiver}")
    
    return couples


couples = gift()


mplt.figure(figsize=(10, 6))
left_x, right_x = -1, 1  
y_positions = list(range(len(couples)))  


for j, (giver, receiver) in enumerate(couples):
    mplt.text(left_x, y_positions[j], giver, ha='center', va='center', fontweight='bold', color="blue")
    mplt.text(right_x, y_positions[j], receiver, ha='center', va='center', fontweight='bold', color="green")


    mplt.arrow(left_x + 0.1, y_positions[j],
         length_includes_head=True, color='red')


 
mplt.show()
