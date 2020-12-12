import random
from game_character import GameCharacter
from explorer import Explorer
from medic import Medic
from warrior import Warrior

count = 1
player_1 = []
player_2= []
c = str
gold = int
gold2 = int

def new_players():
    global player_2,player_1
    #Intiate the players and take the necessary data......  
    for i in range(2):
        print(f"Hello player {i+1}. Please Enter the following data to start the game")
        warrior = input("Please enter the name of the warrior.\n")
        medic = input("please enter the name of your medic\n")
        explorer = input("please enter the name of your explorer\n")
        heal=random.randint(50,100)
        magic=random.randint(50,85)
        attack_max=random.randint(50,85)
        warrior_man = Warrior(warrior,100,attack_max+15, magic+15)
        medic_man = Medic(medic,100,heal,magic)
        explorer_man = Explorer(explorer, 100 , attack_max, magic )
        if(i==0):
            player_1.append(warrior_man)  
            player_1.append(medic_man)  
            player_1.append(explorer_man)
        else:
            player_2.append(warrior_man)  
            player_2.append(medic_man)  
            player_2.append(explorer_man)
        print(f"_________________Your data saved successfully____________________")
    pass

def game_round(turn):
    global count,c,player_1,player_2
    print(f"Round >>> {count}")
    count+=count
    if(turn%2 == 1):
        print(f"Team 1, which character do you wish to choose for this round")
        print(f" 0 - Warrior \n 1 - Medic Man \n 2 - Explorer")
        c = input(f"please choose one of these numbers(0,1,2).\n")
        while not (str(c) == '0' or str(c) == '1' or str(c) == '2'):
            c = input(f"please choose one of these numbers(0,1,2).\n")
        pass
    if(c =='0'):
        warrior_choices(player_1,player_2)
    elif(c=='1'):
        medic_choices(player_1,player_2)
    else:
        explorer_choices(player_1,player_2)

def warrior_choices(you,opposite):
    print(f"You have chosen a warrior to play this round")
    choose = input(f" Warrior can do the following choose one please: \n 0 - Attack - Attack an enemy character \n 1 - Cast spell - Casts a spell on an enemy character \n 2 - Buy armor - Buy armor for a member of the team \n 3 - Share intelligence - Share intelligence with Explorer \n 4 - Another Action - Do something useful \n")
    while not (str(choose) == '0' or str(choose) == '1' or str(choose) == '2' or str(choose) == '3' or str(choose) == '4'):
        choose = input(f"please choose one of these numbers(0,1,2).\n")
        pass
    warrior_actions(choose,you,opposite)
    pass

def warrior_actions(action,you,opposite):
    global c
    print(f"You have been chosen {action} to play this round.")
    chosen = int
    while not (str(chosen) == '0' or str(chosen) == '1' or str(chosen) == '2'):
            chosen = input("please choose 1 of your enemies member \n 0 - Warrior \n 1 - Medic man \n 2 - Explorer")
            pass
    if(int(action)==0):
        you[int(c)].attack(opposite[int(chosen)])
    elif(int(action)==1):
        you[int(c)].cast_spell_on(opposite[int(chosen)])
    elif(int(action)==2):
        you[int(c)].buy_armor(you[int(chosen)])
    c = 500
    pass

def medic_choices(you,opposite):
    global c 
    print(f"You have chosen a medic man to play this round of the game")
    choose = str
    while not (str(choose) == '0' or str(choose) == '2'):
        choose = input(f"Please Choose 0 for Worrier or 2 for Explorer. he will heal them\n")
        pass
    medic_actions(choose,you,opposite)
    pass

def medic_actions(action,you,opposite):
    global c
    print
    if(int(action)==0):
        you[int(c)].heal(you[int(action)])
    c = 500
    pass

def explorer_choices(you,opposite):
    global c 
    print(f"You have chosen a explorer to play this round")
    print(f"The Explorer character helps other characters find gold which gives them better strength. \n")
    num1 = int
    num2 = int
    while not (str(num1) == '0' or str(num1) == '1' or str(num1) == '2' or str(num1) == '3'):
            num1 = input("please choose number between 0 - 3\n")
            pass
    while not (str(num2) == '0' or str(num2) == '1' or str(num2) == '2' or str(num2) == '3'):
            num2 = input("please choose number between 0 - 3\n")
            pass
    you[int(c)].find_gold(int(num1), int(num2))
    pass

        

   
#Start the game....
new_players()
game_round(count)

