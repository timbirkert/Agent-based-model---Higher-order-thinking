from Population import *
from Distribution_determening import new_distribution
from Plot import *
from Poisson_distribution import First_Generation_Distribution
from Game_creater import *
import numpy as np

#population distribution in the first generation
Lambda=1.61
Number_Individuals=200
if True:
    Distribution=First_Generation_Distribution(Number_Individuals, Lambda) #poisson distribution
else:
    Distribution=[0,10,0,10,0]  #manual distribution #manual poisson: [45,58,53,26,18]

Generations= 30
Number_of_Games= 30
Thinking_Costs=True
Smart_Lvl0=True
#Parameter der Kostenfunktion: C(k): a * k**b
a=1.2
b=1

Starting_Distribution=new_distribution(Distribution, Number_Individuals)  #saving starting distribution for calculation of
                                                                    #average growth later

for i in range(Generations):

    Utility_after_each_round = [0, 0, 0, 0, 0]
    Population_this_round = Population(Distribution)
    Game_List=List_of_games(Number_of_Games)

    #everybody plays against everybody, every game

    for index, agent in enumerate(Population_this_round):
        for opponent in Population_this_round[index+1:]:
            for game in Game_List:
                agent.Play(opponent,game, Utility_after_each_round, Thinking_Costs,a,b, Smart_Lvl0)




    print('Generation: ', str(i))
    print("Utility in generation " , str(i) ,": ", Utility_after_each_round)

    Distribution= new_distribution(Utility_after_each_round, Number_Individuals)
    data_dict(Distribution)

    print("Distribution in generation: " , str(i+1) , ": ", Distribution)
    print("----------------------------------------------------")


    if i == Generations-1:
        Absolute_Growth = np.array(Distribution) - np.array(Starting_Distribution)
        Relative_Growth = Absolute_Growth / np.array(Starting_Distribution)
        Relative_Growth_per_10_Generations = Relative_Growth * (10 / Generations)

        print(Starting_Distribution)
        print("Absolute Growth: ", Absolute_Growth)
        print("Relative Growth in percent:", Relative_Growth)
        print("Relative Growth per 10 Generations: ", Relative_Growth_per_10_Generations)


print("Proportion of all individuals during ", str(Generations)," generations: " , calculate_area_proportions(D))
plot_function(D,Generations)
plot_line_chart(D, Generations)

