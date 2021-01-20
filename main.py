from hero import Hero
from goblin import Goblin
from zombie import Zombie

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    my_hero = Hero()
    goblin = Goblin()
    zombie = Zombie()


    while (goblin.alive() or zombie.alive()) and my_hero.alive(): #
        my_hero.print_status()
        goblin.print_status()
        zombie.print_status()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. fight zombie")
        print("4. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            my_hero.attack(goblin)
        elif user_input == "2":
            pass

        elif user_input == "3":
            #hero attacks zombie
            my_hero.attackz(zombie)
        elif user_input == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if (goblin.health > 0) and (zombie.health > 0):
            zombie.attack(my_hero)
            # Goblin/zombie attacks hero
            goblin.attack(my_hero)
main()
