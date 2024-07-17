import random
from entities import Player, Enemy
from items import items

def generate_random_enemy():
    names = ["Goblin", "Troll", "Orc", "Skeleton", "Zombie", "Vampire", "Werewolf", "Dragon", "Demon", "Giant"]
    name = random.choice(names)
    hp = random.randint(20, 50)
    damage = random.randint(5, 15)
    inventory = random.sample(items, random.randint(0, 3))  
    immunity = random.choice([None, "burn", "freeze", "shock", "poison", "curse", "holy", "magic"])
    return Enemy(name, hp, damage, inventory, immunity)

def main():
    player = Player("Hero", 100, 10, [items[0], items[9]], None)  
    turn = 0

    while player.alive:
        turn += 1
        print(f"--- Turn {turn} ---")
        enemy = generate_random_enemy()
        print(f"A wild {enemy.name} appeared with {enemy.hp} HP and {enemy.damage} Damage!")

        while enemy.alive and player.alive:
            action = input("Choose your action (attack/use item/run): ").strip().lower()
            if action == "attack":
                player.attack(enemy, player.inventory[0])
                if not enemy.alive:
                    player.gain_exp(50)
                    enemy.drop_item(player)
            elif action == "use item":
                if player.inventory:
                    for idx, item in enumerate(player.inventory):
                        print(f"{idx + 1}: {item.name}")
                    choice = int(input("Choose an item to use: ")) - 1
                    if 0 <= choice < len(player.inventory):
                        player.attack(enemy, player.inventory[choice])
                        if not enemy.alive:
                            player.gain_exp(50)
                            enemy.drop_item(player)
                else:
                    print("No items to use!")
            elif action == "run":
                print("You fled the battle!")
                break
            else:
                print("Invalid action! Try again.")

            if enemy.alive:
                if enemy.inventory:
                    enemy.attack(player, enemy.inventory[0])
                else:
                    enemy.attack(player)
                if not player.alive:
                    print("You have been defeated!")
                    break

if __name__ == "__main__":
    main()
