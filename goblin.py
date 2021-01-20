from character import Character
class Goblin(Character):
    name = "Goblin"
    def __init__(self, health = 60, power = 2):
        super().__init__(health, power)
        self.winphrase = "You are dead."











    # def alive(self):
    #     be_alive = self.health > 0 
    #     return be_alive
    
    # def print_status(self):
    #     print("The goblin has %d health and %d power." % (self.health, self.power))
    #     print()
