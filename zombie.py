from character import Character
class Zombie(Character):
    name = "Zombie"
    def __init__(self, health = 4, power = 5):
        super().__init__(health, power)
        self.winphrase = "Zombie wins hehe."
    
    def alive(self):
        return True
    