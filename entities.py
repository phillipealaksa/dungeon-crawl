class Entity:
    def __init__(self, name, hp, damage, inventory, imunity):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.inventory = inventory
        self.imunity = imunity
        self.curse = None
        self.alive = True
    
    def attack(self, target, item):
        if not item.curse == None and target.imunity == item.curse:
            print(f'{target.name} is imune to {item.name}! No damage was dealt!')
            target.take_damage(0)
            target.curse = item.curse
            self.inventory.remove(item)
            return True
        print(f'{self.name} used {item.name} on {target.name}!')
        target.take_damage(self.damage)
        self.inventory.remove(item)
        return True
        
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f'{self.name} has died!')
            self.alive = False
        print(f'{self.name} has {self.hp} hp left!')
 

class Player(Entity):
    def __init__(self, name, hp, damage, inventory, imunity):
        super().__init__(name, hp, damage, inventory, imunity)
        self.level = 1
        self.exp = 0
    
    def level_up(self):
        self.hp += 10
        self.damage += 1
        self.level += 1
        print(f'{self.name} has leveled up to level {self.level}!')

    def aquire_item(self, item):
        self.inventory.append(item)
        print(f'{self.name} has aquired {item.name}!')

    def gain_exp(self, exp):
        self.exp += exp

class Enemy(Entity):
    def __init__(self, name, hp, damage, inventory, imunity):
        super().__init__(name, hp, damage, inventory, imunity)
    
    def drop_item(self, target):
        for item in self.inventory:
            target.inventory.append(item)
        print(f'{self.name} has dropped {', '.join(str(i) for i in self.inventory)}!')
