import json
import os
from inventory import Inventory
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print("Name:", self.name)
        print("Price:", self.price)

class Sword(Item):
    def __init__(self, name, price, damage, crit_percent):
        super().__init__(name, price)
        self.damage = damage
        self.crit_percent = crit_percent

    def display_info(self):
        super().display_info()
        print("Damage:", self.damage)
        print("Crit percent:", self.crit_percent)

class Pickaxe(Item):
    def __init__(self, name, price, mining_power):
        super().__init__(name, price)
        self.mining_power = mining_power

    def display_info(self):
        super().display_info()
        print("Mining Power:", self.mining_power)

class Armor(Item):
    def __init__(self, name, price, health_boost):
        super().__init__(name, price)
        self.health_boost = health_boost

    def display_info(self):
        super().display_info()
        print("Health Boost:", self.health_boost)

class Store:
    def __init__(self):
        with open("store.json", "r") as file:
            data = json.load(file)
            self.items = self.parse_items(data)

    def parse_items(self, data):
        items = []
        for item_data in data:
            if "Damage" in item_data:
                item = Sword(item_data["Name"], item_data["Price"], item_data["Damage"], item_data["Crit percent"])
            elif "Mining Power" in item_data:
                item = Pickaxe(item_data["Name"], item_data["Price"], item_data["Mining Power"])
            elif "Health_Boost" in item_data:
                item = Armor(item_data["Name"], item_data["Price"], item_data["Health_Boost"])
            items.append(item)
        return items

    def buy_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                item.display_info()
                sure = input("Are you sure you want to buy this? (Y/N): ")
                if sure.upper() == "Y":
                    print("You have purchased a", item.name)
                    return item
                else:
                    return None
        print("Item not found in the store.")
        return None

def main():
    store = Store()
    while True:
        store_option = input("What do you want to do? (Buy | Sell | Exit): ")
        if store_option == "Buy":
            item_type = input("What type of item do you want to buy? (Sword | Pickaxe | Armor): ")
            item_name = input("Enter the name of the item you want to buy (Sword & Pickaxe tiers: Wooden, Stone, Iron, Diamond, Netherite, God | Armor tiers: Leather, Chainmail, Iron, Diamond, Netherite, God): ")
            if item_type.lower() == "sword" or item_type.lower() == "pickaxe" or item_type.lower() == "armor":
                item = store.buy_item(item_name)
                if item:
                    new_file = "inventory.json"
                    with open(new_file, "w") as f:
                        json_string = json.dumps(item)
                        f.write(json_string)
                    os.rename(new_file, "inventory.json")
                    pass
            else:
                print("Invalid item type.")
        elif store_option == "Sell":
            for Data in :
                Inventory().view_inventory
                ITEM = input("What do you want to sell? Choose 1 : ")
                if ITEM == (Data["Name"]):
                    print("Item name:", Data["Name"])
                    print("Item quantity:", Data["Quantity"])
                    print("Sell value:", Data["Sell value"])

                Quantity = int(input("How much of that item do you want to sell?: "))
                if Quantity > (Data["Quantity"]):
                    print("You don't have that much items, type another number : ")
                    return 

            pass
        elif store_option == "Exit":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose Buy, Sell, or Exit.")

main()