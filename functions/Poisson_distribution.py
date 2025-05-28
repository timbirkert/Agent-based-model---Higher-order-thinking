import numpy as np

def First_Generation_Distribution(Number_Individuals, lambd):
    # Ziehe x Mal aus der Liste range(0, 3) mit Poisson-Verteilung
    draws = np.random.poisson(lambd, Number_Individuals)

    List_of_levels=draws.tolist()
    print(List_of_levels)
    Level_4plus=len(List_of_levels)-(List_of_levels.count(0)+List_of_levels.count(1)+List_of_levels.count(2)+List_of_levels.count(3))

    return [List_of_levels.count(0),List_of_levels.count(1),List_of_levels.count(2),List_of_levels.count(3),Level_4plus]

