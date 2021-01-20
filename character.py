class Character:
    name = "character"
    winphrase = "default"
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def alive(self):
        be_alive = self.health > 0
        if be_alive:
            return True
        else:
            return False

    def attack(self, enemy):
        # attacking method
        enemy.health -= self.power
        print("%s does %d damage to the %s." % (self.name, self.power, enemy.name))
        if enemy.health <= 0:
            print(self.winphrase)   

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))
        print()









# class Hero(Character):
#     def __init__(self, name, health, power):
#         super().__init__(name, health, power)

# class Goblin(Character):
#     def __init__(self, name, health, power):
#         super().__init__(name, health, power)



