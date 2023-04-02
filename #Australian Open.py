#Austalian_Open

import random
  

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

top_players_list1 = []
top_players_list = list(aopen_top_16.keys())
# print("TOP PLAYERLIST:",top_players_list)


team0 = top_players_list
team1 = ['name11', 'name12', 'name13', 'name14', 'name15', 'name16', 'name17', 'name18', 'name19', 'name110', 'name111', 'name112', 'name113', 'name114', 'name115', 'name116']
team2 = ['name21', 'name22', 'name23', 'name24', 'name25', 'name26', 'name27', 'name28', 'name29', 'name210', 'name211', 'name212', 'name213', 'name214', 'name215', 'name216']
team3 = ['name31', 'name32', 'name33', 'name34', 'name35', 'name36', 'name37', 'name38', 'name39', 'name310', 'name311', 'name312', 'name313', 'name314', 'name315', 'name316']
team4 = ['name41', 'name42', 'name43', 'name44', 'name45', 'name46', 'name47', 'name48', 'name49', 'name410', 'name411', 'name412', 'name413', 'name414', 'name415', 'name416']
team5 = ['name51', 'name52', 'name53', 'name54', 'name55', 'name56', 'name57', 'name58', 'name59', 'name510', 'name511', 'name512', 'name513', 'name514', 'name515', 'name516']
team6 = ['name61', 'name62', 'name63', 'name64', 'name65', 'name66', 'name67', 'name68', 'name69', 'name610', 'name611', 'name612', 'name613', 'name614', 'name615', 'name616']
team7 = ['name71', 'name72', 'name73', 'name74', 'name75', 'name76', 'name77', 'name78', 'name79', 'name710', 'name711', 'name712', 'name713', 'name714', 'name715', 'name716']



def omiloi(all_teams):
    match_making = []
    for i in range(8):
        match = []
        for team in all_teams:
            name = random.sample(team, 1)[0]
            match.append(name)
            team.remove(name)
        match_making.append(match)
    return match_making



all_teams = [team0, team1, team2, team3, team4, team5, team6, team7]

match_making = omiloi(all_teams)

def make_matches(match_making, match_index):
    omilos_couples = []
    omilos_couples.extend(match_making[match_index])
    print(omilos_couples)
    couples = []
    
    while len(omilos_couples) > 1:
        # randomly select two names from the list
        names = random.sample(omilos_couples, 2)

        # remove the selected names from the list
        omilos_couples.remove(names[0])
        omilos_couples.remove(names[1])

        # add the pair of names to the couples list
        couples.append((names[0], names[1]))

        
    for couple in couples:
         print(couple)    
    # print(couples)

#make_matches(match_making, 2)

for num in range(8):
    print(make_matches(match_making ,num))

print(match_making)

#Edo exo ftaxei to def poy 8a bgazei toys winners apo ta zeygaria
#Akoma den xero an xreiazete na to metrepso se Class
#Basika prepei na doyme genikotera ton kodika an 8elei na metatrepe kati se Class
#o Kodikas den einai olokliromenos doulebei prosorna me import ton dedomenon 
#prepei na ton ftiaxo etsi oste na pairne ta apotelesma apoto match_makng isos me mia 
#global metablti to Couples?!


def winners(): #Edo me kapoion tropo prepei na balo parametro to index apo ka8e couple
    couples = [('name49', 'Felix Auger-Aliassime'), ('name37', 'name616'), ('name12', 'name516'), ('name213', 'name714')] # tin lista tin pira copy paste apo to apotelesma tis colsole
    winners_list = []
    
    for couple in range(len(couples)):
        winner = random.sample(couples[couple], 1)# to samole exei 2 orismata tin lista pou 8a parei to stixio kai ton ari8mo ton stixion
        winners_list.append(winner[0])
        print(f"Στο μάτς με αντιπάλους τον {couples[couple][0]} και τον {couples[couple][1]}  νικητής ενα ο {winner[0]}")
    
    winners_str = ", ".join(winners_list)
    print("Νικητές του ομίλου:", winners_str)

winners()

