import random
class Creature(object):
    """Basic model for creatures"""
    total = 0

    @staticmethod
    def status():
        print("Overall number of Creatues is", Creature.total)

    def __init__(self, type:str, name:str, health:int, damage:int, defense:int, movement_speed:int):
        """Function inits primary atributes for new creature

        Args:
            type (str): Describes creature's race
            name (str): Creature's unique name
            health (int): Points which desrbibe how much damage creature can take
            damage (int): Number of health point which will be decresed from target
            defense (int): How many damage creature will absorb
            movement_speed (int): Number of spaces which creature can step on in 1 tour
        """                      
        self.type = type
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.movement_speed = movement_speed
        self.is_alive = True
        Creature.total += 1

    def dead(self):
        """Status that Creature cannot make any actions due to health points are 0"""        
        print("Creature", self.name, "has been killed!")
        self.is_alive = False

    def alive(self):
        """Method which shows status of current health point"""        
        if self.health <= 0:
            self.dead()
        else:
            print("Creature", self.name, "type", self.type, "has", self.health, "health points!")
    
    def attack(self,target:object):
        """Creature's action which will decrease targets points of health

        Args:
            target (object): Creature on who attack action will affect
        """                
        if target.health >= 1:
            target.health = target.health -self.damage + target.defense
            print(self.name, "attacks", target.name, "and deals", self.damage - self.defense, "damage", "(" + str(self.defense), "blocked)")
            if target.health <= 0:
               target.dead()

    def block(self, damage_taken):
        pass

    def statistic(self):
        a = ["Type:", "Name:", "Health:", "Damage:", "Defense:", "Movement_speed:"]
        b = [self.type, self.name, self.health, self.damage, self.defense, self.movement_speed]
        for i, j in zip(a, b): 
            print(i,j)
 
    def position(self):
        pass

class Demon(Creature):
    """Basic model for creature - Demon"""

    def __init__(self, name:str, health:int, damage:int, defense:int, movement_speed:int):
        super().__init__(type = "Demon", name = name, health = health, damage= damage, defense = defense, movement_speed = movement_speed)

    def fireball(self, target:object):
        """Skills that deals fire damage to target which ingores target's armor

        Args:
            target (object): Creature who's health ponts will be decreased
        """        
        if target.health >= 1:
            fire_attack = self.damage + random.randint(20,35)
            print(self.name, "use special ability 'fireball' on", target.name, "and deals", fire_attack, "fire damage", "(ignores", target.name + "'s armor)")
            if target.health <= 0:
               target.dead()

    def roar(self, target:object):
        """Skill that allow Demon to decease target's armor by 5 points

        Args:
            target (object): Creature who's armor will be decreased
        """        
        target.defense -= 5
        print(self.name, "use special ability 'roar' on", target.name, "and reduce it's defense by 5 points")

class statistics(object):
    """Object gather statistics from all objects"""

Demon1 = Demon("Krzsztof", 350, 35,20,5)
Demon2 = Demon("Andrzej", 350, 35,20,5)
print(Demon2.health)
Demon1.attack(Demon2)
print(Demon2.health)
Demon1.attack(Demon2)
for i in range(18):
    i = Demon1.attack(Demon2)
Demon1.fireball(Demon2)
Demon1.roar(Demon2)
Demon2.statistic()
Creature.status()