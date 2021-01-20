class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def alive(self):
        be_alive = self.health > 0
        return be_alive

    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))
        print()




# class Hero(Character):
#     def __init__(self, name, health, power):
#         super().__init__(name, health, power)

# class Goblin(Character):
#     def __init__(self, name, health, power):
#         super().__init__(name, health, power)



