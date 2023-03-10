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

    while len(players_list) > 1:
        # randomly select two names from the list
        names = random.sample(players_list, 2)

        # remove the selected names from the list
        players_list.remove(names[0])
        players_list.remove(names[1])

        # add the pair of names to the couples list
        couples.append((names[0], names[1]))

        
        for couples in couples:
            print(couples)    
    
# match_making()

####Edo epidi ta exo ftiaxei xexorista exo dosei idies metablites met to proigoumeno fuction!!
#### MHN MPERDEFTITE!!!
#### PS: 8a ta dior8oso me tin proti eukairia !

def make_matches(all_teams):
    match_making = []
    for i in range(7):
        match = []
        for team in all_teams:
            name = random.sample(team, 1)[0]
            match.append(name)
            team.remove(name)
        match_making.append(match)
    return match_making


all_teams = [team1, team2, team3, team4, team5, team6, team7]

match_making = make_matches(all_teams)

print(match_making) ### Prepei na dior8oso tin ektiposi na fainete ka8e nea omada xexorista!!
make_matches(all_teams)






