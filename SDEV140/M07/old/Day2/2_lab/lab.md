# Lab

-----

> Create EPIC fighting terminal game thing

```python
import random


class Creature:
    alive = True
    full_health = 100
    full_damage = 50
    full_accuracy = 75

    accuracy = 0
    damage = 0
    health = 0

    name = 'nill'

    def __init__(self, creature_name, base_damage, base_health, base_accuracy):
        self.full_damage = base_damage
        self.full_health = base_health
        self.full_accuracy = base_accuracy

        self.damage = self.full_damage
        self.health = self.full_health
        self.accuracy = self.full_accuracy

        self.name = creature_name

    def change_health(self, amount):
        self.health += amount

        if self.health <= 0:
            self.alive = False
        elif self.health > self.full_health:
            self.health = self.full_health

        return self.alive

    def attack(self, other_creature : 'Creature'):
        if self.accuracy_check():
            other_creature.change_health(self.damage * -1)
            print(f"{self.name}'s Attack HIT for {self.damage} points to {other_creature.name}!")
        else:
            print(f"{self.name}'s Attack MISSED")

    def accuracy_check(self):
        random_value = random.randrange(100)
        return random_value <= self.accuracy

    def __str__(self):
        return f'{self.name}\tHP:{self.health}/{self.full_health}'



class Player(Creature):
    restoration_full = 20
    restoration = restoration_full

    def __init__(self, user_name):
        super().__init__(user_name, 15, 100, 80)

    def heal(self):
        self.change_health(self.restoration)
        print(f"You healed for {self.restoration} points")

    def get_move(self, other_creature):
        while True:
            move = input('Heal Or Attack? (H or A): ').upper()
            if move == 'H':
                self.heal()
                break
            elif move == 'A':
                self.attack(other_creature)
                break
            else:
                print("PLEASE ENTER VALID MOVE")


class Box(Creature):
    def __init__(self):
        super().__init__('Box', 30, 30, 50)

class BigRat(Creature):
    def __init__(self):
        super().__init__('Big Rat', 15, 60, 75)


def get_new_creature():
    random_val = random.randrange(10)
    if random_val > 5:
        return BigRat()
    else:
        return Box()


def main():
    print("WELCOME TO FIGHTER GAME THING")
    user_name = input('What is your name: ')
    player = Player(user_name)
    waves_survived = 0
    new_creature = True
    encounter = Creature('nil', 0, 0, 0)

    while player.alive:
        if new_creature:
            encounter = get_new_creature()
            print(f'YOU HAVE ENCOUNTERED A {encounter.name}')
            new_creature = False

        print("\n\n==========================================================")
        print(f"||\t{str(player)}\t|\\/\\/\\/|\t{str(encounter)}\t||")
        print("==========================================================")
        player.get_move(encounter)

        if encounter.alive:
            encounter.attack(player)
        else:
            waves_survived += 1
            print("__________________________________")
            print(f"YOU DEFEATED {encounter.name}")
            print("----------------------------------\n")
            end_in = input('End game? (yes or no): ').upper()
            if end_in == 'YES' or end_in == "Y":
                break
            new_creature = True
    else:
        print("YOU DIED BOZO")



    print(f"You survived {waves_survived} waves of enemies")





if __name__ == "__main__":
    main()
```