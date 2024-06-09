import random

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0
        self.money = 100
        self.stats = {
            'strength': 10,
            'defense': 10,
            'agility': 10,
        }
        self.inventory = []
        self.health = 100

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.stats['strength'] += 5
        self.stats['defense'] += 5
        self.stats['agility'] += 5
        self.health = 100
        print(f"{self.name} leveled up to level {self.level}!")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"Added {item['name']} to inventory.")

    def show_stats(self):
        print(f"Level: {self.level}, Exp: {self.exp}, Money: {self.money}, Health: {self.health}")
        for stat, value in self.stats.items():
            print(f"{stat.capitalize()}: {value}")

    def show_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(f"{item['name']} - {item['type']}")

class Shop:
    def __init__(self):
        self.items = [
            {'name': 'Sword', 'type': 'weapon', 'price': 50},
            {'name': 'Shield', 'type': 'armor', 'price': 50},
            {'name': 'Potion', 'type': 'consumable', 'price': 20}
        ]

    def display_items(self):
        print("Shop Items:")
        for item in self.items:
            print(f"{item['name']} - {item['type']} - {item['price']} coins")

    def buy_item(self, player, item_name):
        for item in self.items:
            if item['name'].lower() == item_name.lower():
                if player.money >= item['price']:
                    player.money -= item['price']
                    player.add_item(item)
                    print(f"Bought {item['name']} for {item['price']} coins.")
                    return
                else:
                    print("Not enough money!")
                    return
        print("Item not found!")

class World:
    def __init__(self):
        self.locations = ["mine", "forest", "mountains"]
        self.boss = {'name': 'Dragon', 'strength': 50, 'defense': 50, 'health': 200}

    def explore(self, player):
        location = random.choice(self.locations)
        print(f"Exploring the {location}...")
        if location == "mine":
            self.mine(player)
        elif location == "forest":
            self.forage(player)
        elif location == "mountains":
            self.boss_fight(player)

    def mine(self, player):
        loot = {'name': 'Iron Ore', 'type': 'resource'}
        print(f"Found {loot['name']} in the mine!")
        player.add_item(loot)
        player.exp += 10
        if player.exp >= 100:
            player.level_up()

    def forage(self, player):
        loot = {'name': 'Herb', 'type': 'resource'}
        print(f"Found {loot['name']} in the forest!")
        player.add_item(loot)
        player.exp += 10
        if player.exp >= 100:
            player.level_up()

    def boss_fight(self, player):
        print(f"Encountered a {self.boss['name']}!")
        while self.boss['health'] > 0 and player.health > 0:
            attack = player.stats['strength'] - self.boss['defense'] // 2
            self.boss['health'] -= max(attack, 0)
            print(f"Attacked {self.boss['name']} for {max(attack, 0)} damage. Boss health: {self.boss['health']}")
            if self.boss['health'] <= 0:
                print(f"Defeated the {self.boss['name']}!")
                player.exp += 50
                player.money += 100
                if player.exp >= 100:
                    player.level_up()
                return
            boss_attack = self.boss['strength'] - player.stats['defense'] // 2
            player.health -= max(boss_attack, 0)
            print(f"{self.boss['name']} attacked for {max(boss_attack, 0)} damage. Player health: {player.health}")
            if player.health <= 0:
                print(f"{player.name} was defeated by the {self.boss['name']}...")
                return

def main():
    player_name = input("Enter your player's name: ")
    player = Player(player_name)
    shop = Shop()
    world = World()

    while True:
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. Visit Shop")
        print("3. Show Stats")
        print("4. Show Inventory")
        print("5. Quit")
        choice = input("> ")

        if choice == "1":
            world.explore(player)
        elif choice == "2":
            shop.display_items()
            item_choice = input("Enter the name of the item to buy: ")
            shop.buy_item(player, item_choice)
        elif choice == "3":
            player.show_stats()
        elif choice == "4":
            player.show_inventory()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
