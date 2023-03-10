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
    
match_making()

### Ayth einai i geniki idea gia to epomeno erotima me ta matchmakings apo tin 17-128 8esi...
### Alla o kodikas 8a bgei terastios.... ###
###Prospa8o na do pos 8a to kano se Function/Class se sindiasmo me ena for/while loop ###
### Unfinished!! ###


#MAtch_Making_from_7_teams
import random
team1 = ['name11', 'name12', 'name13', 'name14', 'name15', 'name16', 'name17', 'name18', 'name19', 'name110', 'name111', 'name112', 'name113', 'name114', 'name115', 'name116']
team2 = ['name21', 'name22', 'name23', 'name24', 'name25', 'name26', 'name27', 'name28', 'name29', 'name210', 'name211', 'name212', 'name213', 'name214', 'name215', 'name216']
team3 = ['name31', 'name32', 'name33', 'name34', 'name35', 'name36', 'name37', 'name38', 'name39', 'name310', 'name311', 'name312', 'name313', 'name314', 'name315', 'name316']
team4 = ['name41', 'name42', 'name43', 'name44', 'name45', 'name46', 'name47', 'name48', 'name49', 'name410', 'name411', 'name412', 'name413', 'name414', 'name415', 'name416']
team5 = ['name51', 'name52', 'name53', 'name54', 'name55', 'name56', 'name57', 'name58', 'name59', 'name510', 'name511', 'name512', 'name513', 'name514', 'name515', 'name516']
team6 = ['name61', 'name62', 'name63', 'name64', 'name65', 'name66', 'name67', 'name68', 'name69', 'name610', 'name611', 'name612', 'name613', 'name614', 'name615', 'name616']
team7 = ['name71', 'name72', 'name73', 'name74', 'name75', 'name76', 'name77', 'name78', 'name79', 'name710', 'name711', 'name712', 'name713', 'name714', 'name715', 'name716']

match_making1 =[]
match_making2 =[]
match_making3 =[]
match_making4 =[]
match_making5 =[]
match_making6 =[]
match_making7 =[]

all_teams =[team1, team2, team3, team4, team5,team6,team7]
for team in range(len(all_teams)):
    
name1 = random.sample(team1,1)
name2 = random.sample(team2,1)
match_making1.append(name1)
match_making1.append(name2)

team1.remove(name1[0])
team2.remove(name2[0])

print(match_making1)
print(team1)
print(team2)








