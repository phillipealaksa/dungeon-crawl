class Item:
    def __init__(self, name, damage=0, curse=None, heal=0, consumable=False):
        self.name = name
        self.damage = damage
        self.curse = curse
        self.heal = heal
        self.consumable = consumable

items = [
    Item("Sword", 10),
    Item("Axe", 15),
    Item("Dagger", 5),
    Item("Mace", 12),
    Item("Spear", 8),
    Item("Bow", 9),
    Item("Fire Staff", 14, curse="burn"),
    Item("Ice Wand", 7, curse="freeze"),
    Item("Lightning Rod", 13, curse="shock"),
    Item("Healing Potion", heal=20, consumable=True),
    Item("Poison", 6, curse="poison", consumable=True),
    Item("Cursed Blade", 11, curse="curse"),
    Item("Holy Water", heal=15, consumable=True),
    Item("Shield", 0),  
    Item("Magic Ring", 0, curse="magic"),
    Item("War Hammer", 16),
    Item("Crossbow", 11),
    Item("Flame Thrower", 17, curse="burn"),
    Item("Freeze Ray", 10, curse="freeze"),
    Item("Thunderbolt", 18, curse="shock"),
    Item("Large Healing Potion", heal=50, consumable=True),
    Item("Elixir of Life", heal=100, consumable=True)
]
