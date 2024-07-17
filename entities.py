class Entity:
    def __init__(self, name, hp, damage, inventory, immunity):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.inventory = inventory
        self.immunity = immunity
        self.curse = None
        self.alive = True
    
    def attack(self, target, item=None):
        if item and item.heal > 0:
            self.hp += item.heal
            if self.hp > 100: 
                self.hp = 100
            print(f'{self.name} used {item.name} and healed for {item.heal} HP! Now at {self.hp} HP.')
            if item.consumable:
                self.inventory.remove(item)
            return True
        if item and item.curse and target.immunity == item.curse:
            print(f'{target.name} is immune to {item.name}! No damage was dealt!')
            target.take_damage(0)
            target.curse = item.curse
            if item.consumable:
                self.inventory.remove(item)
            return True
        if item:
            print(f'{self.name} used {item.name} on {target.name}!')
            target.take_damage(self.damage + item.damage)
            if item.consumable:
                self.inventory.remove(item)
        else:
            print(f'{self.name} attacks {target.name} with a basic attack!')
            target.take_damage(self.damage)
        return True

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f'{self.name} has died!')
            self.alive = False
        print(f'{self.name} has {self.hp} hp left!')

class Player(Entity):
    def __init__(self, name, hp, damage, inventory, immunity):
        super().__init__(name, hp, damage, inventory, immunity)
        self.level = 1
        self.exp = 0
        self.equipped = None
    
    def level_up(self):
        self.hp += 10
        self.damage += 1
        self.level += 1
        print(f'{self.name} has leveled up to level {self.level}!')

    def acquire_item(self, item):
        self.inventory.append(item)
        print(f'{self.name} has acquired {item.name}!')

    def gain_exp(self, exp):
        self.exp += exp
        if self.exp >= 100: 
            self.level_up()
            self.exp = 0

class Enemy(Entity):
    def __init__(self, name, hp, damage, inventory, immunity):
        super().__init__(name, hp, damage, inventory, immunity)
    
    def drop_item(self, target):
        for item in self.inventory:
            target.inventory.append(item)
        print(f'{self.name} has dropped {", ".join(item.name for item in self.inventory)}!')
