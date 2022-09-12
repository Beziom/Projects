import random
from all_items import all_items_game
class Creature(object):
    """Basic model for creatures"""

    number_of_creatures = 0
    number_of_attacks = 0
    number_of_abilities = 0
    damage_dealt_by_attacks = 0
    damage_dealt_by_abilities = 0

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
        Creature.number_of_creatures += 1

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
            self.number_of_attacks += 1 # Is it the best idea to add statistic solution here (or it should be done in classs)
            self.damage_dealt_by_attacks += self.damage - target.defense
            print(self.name, "attacks", target.name, "and deals", self.damage - self.defense, "damage", "(" + str(self.defense), "blocked)")

            if target.health <= 0:
               target.dead()

    def block(self, damage_taken):
        pass

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
            self.number_of_abilities += 1
            self.damage_dealt_by_abilities += fire_attack
            print(self.name, "use special ability 'fireball' on", target.name, "and deals", fire_attack, "fire damage", "(ignores", target.name + "'s armor)")
            if target.health <= 0:
               target.dead()

    def roar(self, target:object):
        """Skill that allow Demon to decease target's armor by 5 points

        Args:
            target (object): Creature who's armor will be decreased
        """           
        target.defense -= 5
        self.number_of_abilities += 1 # Is it the best idea to add statistic solution here (or it should be done in classs)
        print(self.name, "use special ability 'roar' on", target.name, "and reduce it's defense by 5 points")

class Vampire(Creature):
    """_Basic model fo creature Vampire"""   
    
    def __init__(self, name: str, health: int, damage: int, defense: int, movement_speed: int):
        super().__init__(type = "Vampire", name = name, health = health, damage = damage, defense = defense, movement_speed = movement_speed)
    
    def attack(self, target: object):
        super().attack(target)
        self.health += self.damage - target.defense

    def consumption(self, target:object):
        life_steal_damage = random.randint(10,15)
        if target.health <= life_steal_damage:
               target.dead()
        else:
            target.health -= life_steal_damage
            self.health += life_steal_damage
            print(self.name, "use special ability 'consumption' on", target.name, "and steals", life_steal_damage, "health points from", target.name)

class Statistics(object):
    """Class which gathers all object's data"""
    number_of_creatures = 0
    number_of_attacks = 0
    number_of_abilities = 0

    @staticmethod
    def status():
        print("Overall number of Creatues is", Creature.number_of_creatures)

    def current_stats(creature:object):
        """Current creature's basic stats

        Args:
            creature (_type_): Creature which stat's will be shown
        """        
        a = ["Type:", "Name:", "Health:", "Damage:", "Defense:", "Movement_speed:", "Number_of_attacks:", "Damage_dealt_by_attacks:", "Number_of_used_abilities:", "Damage_dealt_by_abilities"]
        b = [creature.type, creature.name, creature.health, creature.damage, creature.defense, creature.movement_speed, creature.number_of_attacks, creature.damage_dealt_by_attacks, creature.number_of_abilities, creature.damage_dealt_by_abilities]
        for i, j in zip(a, b): 
            print(i,j)

class Inventory(object):
    Creature.inventory = {"health_potion":5, "mana_potion":3}
    
    def equipment(Creature:object):
        for key,value in Creature.inventory.items():
            print(key,value)
        pass    

    def add_item(Creature:object):

        added_item = input("What item do You want to add?:")
        Creature.inventory[added_item] += 1

#Main program
Demon1 = Demon("Krzsztof", 350, 35,20,5)
Demon2 = Demon("Andrzej", 350, 35,20,5)
Vampire1 = Vampire("Kamil", 400, 25, 20, 10)

Demon1.attack(Demon2)
Demon1.fireball(Demon2)
Demon1.roar(Demon2)
Vampire1.attack(Demon1)
Vampire1.consumption(Demon1)

Statistics.current_stats(Vampire1)
Statistics.current_stats(Demon1)
Statistics.current_stats(Demon2)
Inventory.equipment(Demon1)
Inventory.add_item(Demon1)
Inventory.equipment(Demon1)
#To do:
#1* Try to what method should i use to count attacks (uses ability) - done
#2* Adding Mana inficator 
#3* Check PyGame - maybe there are solution idea for extension --inventory
#4* Best practice: Where should be database for all items (if - when something is not in the game)
