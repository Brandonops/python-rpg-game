from character import Character
class Goblin(Character):
    def __init__(self, health = 6, power = 2):
        super().__init__(health, power)

    def attack(self, hero):
        # Goblin attacks hero
        hero.health -= self.power
        print("The goblin does %d damage to you." % self.power)
        if hero.health <= 0:
            print("You are dead.")
        








    # def alive(self):
    #     be_alive = self.health > 0 
    #     return be_alive
    
    # def print_status(self):
    #     print("The goblin has %d health and %d power." % (self.health, self.power))
    #     print()
