import random
from Strategy import *



#Utility_after_each_round=[0,0,0,0]  # here the utility of the individuals will added: the first element is the utility of all
                                     # level 0 individuals and so on, this will later determine the population of the next generation

# Definition of the class for the object
class Individual:
    def __init__(self, level):
        self.level = level

    def get_level(self):
        return self.level

    def cost_function(self,a,b):
        k=self.level
        return a*k**b

    def Play(self, opponent, game, Utility_after_each_round,Thinking_Costs,a,b, Smart_Lvl0):

        Utility_of_game = Strategy_columnplayer(self.level,opponent.get_level(), game, Smart_Lvl0)

        Utility_after_each_round[self.level] += Utility_of_game[0]
        Utility_after_each_round[opponent.get_level()] += Utility_of_game[1]

        if Thinking_Costs==True:
            Utility_after_each_round[self.level] -= self.cost_function(a,b)
            Utility_after_each_round[opponent.get_level()]-= opponent.cost_function(a,b)

        #print(Utility_after_each_round)
        # #if liked you can print out the utility distribution after each play of every pair

def Population(level_counts):
    # Number of objects for each level
    #level_counts = [15, 25, 35, 25]

    # List to store objects
    object_list = []

    # Iterate over the number of objects for each level
    for level, count in enumerate(level_counts):
        # Create the specified number of objects for each level and add them to the list
        for _ in range(count):
            obj = Individual(level)
            object_list.append(obj)

    # Shuffle the list to ensure the objects are not sorted by level
    random.shuffle(object_list)

    # Example: Output the level of each object in the list
    #for obj in object_list:
        #print("Level:", obj.level)

    return object_list
# returns a list with objects - the individuals in the population
#print(Population([25,25,25,25]))
