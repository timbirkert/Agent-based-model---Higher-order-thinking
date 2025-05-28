#Game1= [
 #   [[10, 15], [6, 27], [12, 30]],
  #  [[20, 18], [16, 15], [8, 24]],
   # [[6, 15], [18, 9], [10, 12]]
#]
import random

def Strategy_rowplayer(rowplayer_level,Game, Smart_Lvl0): #this function defines the strategy of the rowplayer it always returns one row of the matrix
    if rowplayer_level==0 and Smart_Lvl0 == False:
        return random.choice(Game)
    if rowplayer_level==0 and Smart_Lvl0 == True:
        return MaxExpUtil_Row(Game)
    if rowplayer_level==1:
        return random.choice(Game)
    if rowplayer_level==2:
        return random.choice(Game[:2])
    if rowplayer_level == 3:
        return random.choice(Game[:2])
    if rowplayer_level == 4:
            return Game[0]


def Strategy_columnplayer(rowplayer_level, columnplayer_level,Game, Smart_Lvl0): #this function defines the strategy of the column-player, it always returns the (utility of the) strategy combination of both players
    Row_strategie=Strategy_rowplayer(rowplayer_level,Game, Smart_Lvl0)
    if columnplayer_level==0 and Smart_Lvl0 == False:
        return random.choice(Row_strategie)
    if columnplayer_level==0 and Smart_Lvl0 == True:
        return MaxExpUtil_Column(Game, Row_strategie)
    if columnplayer_level==1:
        return random.choice([Row_strategie[0], Row_strategie[-1]])
    if columnplayer_level==2:
        return random.choice([Row_strategie[0], Row_strategie[-1]])
    if columnplayer_level == 3:
        return Row_strategie[2]
    if columnplayer_level == 4:
        return Row_strategie[2]

#given the levels of the players they play a certain strategy or randomize if they are indifferent between two or more strategies
#these two function first select which strategie the rowplayer will choose and then which strategy the columplayer will choose

#print(Strategy_columnplayer(3,2,Game1))

def MaxExpUtil_Row(Game):
    Util_0=Game[0][0][0]+Game[0][1][0]+Game[0][2][0]
    Util_1=Game[1][0][0]+Game[1][1][0]+Game[1][2][0]
    Util_2=Game[2][0][0]+Game[2][1][0]+Game[2][2][0]

    if Util_0 >= Util_1 and Util_0 >= Util_2:
        return Game[0]

    if Util_1 >= Util_0 and Util_1 >= Util_2:
        return Game[1]

    if Util_2 >= Util_1 and Util_2 >= Util_0:
        return Game[2]


def MaxExpUtil_Column(Game, Row_strategie):
    Util_0 = Game[0][0][1] + Game[1][0][1] + Game[2][0][1]
    Util_1 = Game[0][1][1] + Game[1][1][1] + Game[2][1][1]
    Util_2 = Game[0][2][1] + Game[1][2][1] + Game[2][2][1]

    if Util_0 >= Util_1 and Util_0 >= Util_2:
        return Row_strategie[0]

    if Util_1 >= Util_0 and Util_1 >= Util_2:
        return Row_strategie[1]

    if Util_2 >= Util_1 and Util_2 >= Util_0:
        return Row_strategie[2]
