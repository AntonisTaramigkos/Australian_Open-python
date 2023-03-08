#Australian Open
import random

players_list1 = []

aopen_top_16 = {"Rafael Nadal":("Spain",1),
"Casper Ruud":("Norway",2),
"Stefanos Tsitsipas":("Greece",3),
"Novak Djokovic":("Serbia",4),
"Andrey Rublev":("Russia",5),
"Felix Auger-Aliassime":("Canada",6),
"Daniil Medvedev":("Russia",7),
"Taylor Fritz":("United States of America",8),
"Holger Rune":("Denmark",9),
"Hubert Hurkacz":("Poland",10),
"Cameron Norrie":("United Kingdom",11),
"Alexander Zverev":("Germany",12),
"Matteo Berrettini":("Italy",13),
"Pablo Carreno Busta":("Spain",14),
"Jannik Sinner":("Italy",15),
"Frances Tiafoe":("United States of America",16)}

#playerClass
class Players():
    def __init__(self,name,country,world_ranking) :
        self.name = name
        self.country = country
        self.world_ranking = world_ranking
        pass

    def __repr__(self) -> str:
        return "{:<25}  {:<15}  {:>10.1f}".format(self.name, self.country, self.world_ranking)
        pass

#Match Making#
#From a List/Dict or SQL db we add the players in the a list
#the with a radom choose we add them in a new list Match_Making
#then we take the duos and with a print we shaw the pairs
def match_making():
    players_list = list(aopen_top_16.keys())
    
    print(players_list)
    couples = []

    while len(players_list1) > 1:
        # randomly select two names from the list
        names = random.sample(players_list, 2)

        # remove the selected names from the list
        players_list.remove(names[0])
        players_list.remove(names[1])

        # add the pair of names to the couples list
        couples.append((names[0], names[1]))

        # if there is one name left in the list, add it to the last couple
        if len(players_list) == 1:
            couples[-1] += (players_list[0],)
        for couples in couples:
    print(couples)    
    
match_making()

# player1 = Players("Roger Federer", "Switzerland", 5.0)
# player2 = Players("Antonis Taramigkos","Greece", 10)

# print the player's information
# print(player1)
# print(player2)
# match_making()





