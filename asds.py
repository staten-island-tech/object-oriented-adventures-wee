import random

class Entity:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
    
    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)
        return self.health <= 0
    
    def is_alive(self):
        return self.health > 0

class Player(Entity):
    def __init__(self, name):
        super().__init__(name, 100, 10, 5)
        self.level = 1
        self.exp = 0
        self.inventory = []
        self.gold = 0
    
    def level_up(self):
        self.level += 1
        self.health += 20
        self.attack += 5
        self.defense += 3
        self.exp = 0
    
    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= 100:
            self.level_up()

class Monster(Entity):
    def __init__(self, name, health, attack, defense, exp_reward):
        super().__init__(name, health, attack, defense)
        self.exp_reward = exp_reward

class Shop:
    def __init__(self):
        self.items = {
            'sword': {'price': 10, 'attack': 5},
            'shield': {'price': 15, 'defense': 3},
            'potion': {'price': 5, 'heal': 20}
        }
    
    def display_items(self):
        for item, details in self.items.items():
            print(f"{item.capitalize()}: {details}")

class Game:
    def __init__(self):
        self.player = Player('Hero')
        self.shop = Shop()
    
    def explore(self):
        print("Exploring...")
        if random.random() < 0.5:
            self.fight_monster()
        else:
            print("You found nothing.")

    def forage(self):
        print("Foraging...")
        found = random.choice(['berries', 'mushrooms', 'nothing'])
        if found == 'nothing':
            print("You found nothing.")
        else:
            self.player.inventory.append(found)
            print(f"You found {found}.")

    def mine(self):
        print("Mining...")
        found = random.choice(['coal', 'iron', 'gold', 'nothing'])
        if found == 'nothing':
            print("You found nothing.")
        else:
            self.player.inventory.append(found)
            print(f"You found {found}.")

    def visit_shop(self):
        print("Welcome to the shop!")
        self.shop.display_items()
        choice = input("What would you like to buy? ").lower()
        if choice in self.shop.items:
            item = self.shop.items[choice]
            if self.player.gold >= item['price']:
                self.player.gold -= item['price']
                self.player.inventory.append(choice)
                print(f"You bought a {choice}.")
            else:
                print("Not enough gold.")
        else:
            print("Invalid choice.")
    
    def fight_monster(self):
        monster = Monster('Zombie', 50, 8, 2, 30)
        print(f"A wild {monster.name} appeared!")
        while monster.is_alive() and self.player.is_alive():
            action = input("Do you want to [attack] or [run]? ")
            if action == 'attack':
                if monster.take_damage(self.player.attack):
                    print(f"You defeated the {monster.name}!")
                    self.player.gain_exp(monster.exp_reward)
                    break
                if self.player.take_damage(monster.attack):
                    print("You died!")
                    break
            elif action == 'run':
                if random.random() < 0.5:
                    print("You escaped!")
                    break
                else:
                    print("You failed to escape!")
                    if self.player.take_damage(monster.attack):
                        print("You died!")
                        break
            else:
                print("Invalid action.")
    
    def show_stats(self):
        print(f"Name: {self.player.name}, Health: {self.player.health}, Attack: {self.player.attack}, Defense: {self.player.defense}, Level: {self.player.level}, Exp: {self.player.exp}, Gold: {self.player.gold}")
        print(f"Inventory: {self.player.inventory}")

def main():
    game = Game()
    while True:
        print("\nWhat do you want to do?")
        print("[1] Explore")
        print("[2] Forage")
        print("[3] Mine")
        print("[4] Visit Shop")
        print("[5] Show Stats")
        print("[6] Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            game.explore()
        elif choice == '2':
            game.forage()
        elif choice == '3':
            game.mine()
        elif choice == '4':
            game.visit_shop()
        elif choice == '5':
            game.show_stats()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
