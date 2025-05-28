#this files creates a random game which has a structure that allows iterated elimination of dominated strategies

import random

def random_game():

    Utilities=range(30)

    while True:
        a1, b1, c1 = random.sample(Utilities,3)

        if a1 < b1 and c1 < b1:
            break

    while True:
        a2, b2, c2 = random.sample(Utilities, 3)

        if a2 < b2 and c2 < b2:
            break

    while True:
        a3, b3, c3 = random.sample(Utilities, 3)

        if a3 < b3 < c3:
            break

    # now the utility values for the rowplayer

    while True:
        x1, y1, z1 = random.sample(Utilities, 3)

        if z1 < x1 < y1:
            break

    while True:
        x2, y2, z2 = random.sample(Utilities, 3)

        if x2 < z2 and y2 < z2:
            break

    while True:
        x3, y3, z3 = random.sample(Utilities, 3)

        if y3 < x3 and z3 < x3:
            break

    #now we have all the variables for the matrix

    return  [
        [[x1, c1], [x2, a1], [x3, b1]],
        [[y1, c2], [y2, a2], [y3, b2]],
        [[z1, c3], [z2, a3], [z3, b3]]
    ]



def List_of_games(Number_of_Games):
    Game_List=[]

    for i in range(Number_of_Games):
        Game_List.append(random_game())
    print(Game_List)
    return Game_List


