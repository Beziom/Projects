from abc import ABC, abstractmethod

class Creature(object):
    """Basic model for creatures"""

    atributes = []

    def __init__(self, type, name, health, damage, defense, movement_speed):
        self.type = type
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.movement_speed = movement_speed

    def die(self): # chciałbym aby po wywołaniu funkcji obiekt został usunięty/wyczyszcony z apmięci
        print("Postać", self.name, "została zgładzona!")

    def is_alive(self):
        if self.health <= 0:
            self.die()
        else:
            print("Postać", self.name, "typu", self.type, "posiada", self.health, "punktów życia!")
    
    def attack(self, target):
        print(self.name, "atakuje", target.name, "oraz zadaje", self.damage, "obrażeń")
        target.health = target.health -self.damage + target.defense

    def defend(self, damage_taken): #czy robic ten atrybut na zasadzie bloku?
        pass

    @abstractmethod
    def statistic(self):
        pass
 
    @abstractmethod
    def position(self):
        pass

class Demon(Creature):
    """Basic model for creature - Demon"""

    def __init__(self, name, health, damage, defense, movement_speed): # Atrybuty są wpisywane będę myślał żeby zrobić losowy przedział
        super().__init__("Demon", name, health, damage, defense, movement_speed)
        self.atributes = ("Demon", name, health, damage, defense, movement_speed)

    def fireball(self):
        pass

    def statistic(self):
        a = ["Type:", "Name:", "Health:", "Damage:", "Defense:", "Movement_speed:"]
        for i, j in zip(a, self.atributes): # Chciałbym stworzyć żeby były genrowany opisy statystyk
            print(i,j)

Demon1 = Demon("Krzsztof", 350, 35,20,5)
Demon2 = Demon("Andrzej", 350, 35,20,5)
Demon1.is_alive()
print()
Demon1.die()
print()
Demon1.statistic()
print()
print(Demon2.health)
print()
Demon1.attack(Demon2)
print()
print(Demon2.health)
print()
Demon1.attack(Demon2)
print()
print(Demon2.health)