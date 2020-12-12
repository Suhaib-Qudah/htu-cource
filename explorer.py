from game_character import GameCharacter
import random
class Explorer(GameCharacter):

    def __init__(self, name, health, attack_max, magic):

        super().__init__(name, health, attack_max, magic)

        print(f"Commander '{self.name}' at your service.")

    def find_gold(self,num1,num2):  
        random_map = random.randint(1,5)
        map1=[['X', 'X', '$', '$'],
             ['$', '$', 'X', 'X'],
             ['X', 'X', '$', 'X'],
             ['$', 'X', 'X', '$'],]
        map2=[['X', 'X', '$', '$'],
              ['$', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X'],
              ['$', 'X', 'X', '$'],]
        map3=[['X', '$', '$', '$'],
              ['$', '$', '$', 'X'],
              ['$', 'X', '$', 'X'],
              ['$', 'X', 'X', '$'],]
        map4=[['X', '$', '$', '$'],
              ['$', '$', 'X', 'X'],
              ['X', 'X', '$', 'X'],
              ['$', 'X', 'X', '$'],]      
        print(random_map)
        if(random_map == 1):
             print(map1)
             map = map1
        elif(random_map == 2):
             print(map2)
             map = map2
        elif(random_map == 3):
             print(map3)
             map = map3
        elif(random_map == 4):
             print(map4)
             map = map4
        else:
             print(map3)
             map = map3
        if(map[int(num1)][int(num2)]=="$"):
            print(f"Congratulations, You earn 100$ of gold")
            return True
        else:
            print(f"Sorry, you open an empty treasure box. \n try again next round")
            return False

pass



