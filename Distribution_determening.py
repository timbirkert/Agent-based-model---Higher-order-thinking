def new_distribution(Utility_after_last_round,Sum_of_Individuals):
    Sum=sum(Utility_after_last_round)

    # here the percentile-distribution of level 0, dependent on its former utiliy is determined

    A0 = Utility_after_last_round[0] / Sum
    A1 = Utility_after_last_round[1] / Sum
    A2 = Utility_after_last_round[2] / Sum
    A3 = Utility_after_last_round[3] / Sum
    A4 = Utility_after_last_round[4] / Sum

    L=[A0,A1,A2,A3,A4]
    L=[round(x * Sum_of_Individuals) for x in L] #rounds and multiplies the percentiles with 100
    #L.append(Sum_of_Individuals-sum(L)) #makes sure that  the values always add up to 100
    return L
