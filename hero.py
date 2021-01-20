from character import Character
from goblin import Goblin

class Hero(Character):
    name = "Hero"
    def __init__(self, health = 100, power = 2):
        super().__init__(health, power)
        self.winphrase = "The goblin is dead."


    def attackz(self, enemy):
        # attacking method
        enemy.health -= self.power
        print("%s does %d damage to the %s." % (self.name, self.power, enemy.name))
        if enemy.health <= 0:
            print("You can't kill a zombie")    

    


# class Hero:
#     def __init__(self, health = 10, power = 5):
#         self.health = health
#         self.power = power

#     def attack(self, goblin):
#         # Hero attacks goblin
#         goblin.health -= self.health
#         print("You do %d damage to the goblin." % self.power)
#         if goblin.health <= 0:
#             print("The goblin is dead.")
    
#     def alive(self):
#         be_alive = self.health > 0
#         return be_alive

#     def print_status(self):
#         print("You have %d health and %d power." % (self.health, self.power))
#         print()



        