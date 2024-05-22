import json, os
""" from inventory import  PracticeInventoryInstance """

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
        self.name = name
        self.price = price
        self.damage = damage
        self.crit_percent = crit_percent
    def display_info(self):
        super().display_info()
        print("Damage:", self.damage)
        print("Crit percent:", self.crit_percent)
    def to_dict(self):
        return {
            "Name": self.name,
            "Price": self.price,
            "Damage": self.damage,
            "Crit percent": self.crit_percent
        }

class Pickaxe(Item):
    def __init__(self, name, price, mining_power):
        super().__init__(name, price)
        self.mining_power = mining_power
    def display_info(self):
        super().display_info()
        print("Mining Power:", self.mining_power)
    def to_dict(self):
        return {
            "Name": self.name,
            "Price": self.price,
            "Mining power": self.mining_power
        }

class Armor(Item):
    def __init__(self, name, price, health_boost):
        super().__init__(name, price)
        self.health_boost = health_boost
    def display_info(self):
        super().display_info()
        print("Health Boost:", self.health_boost)
    def to_dict(self):
        return {
            "Name": self.name,
            "Price": self.price,
            "Health boost": self.health_boost
        }



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
    def sell_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                item.display_info()
                sure = input("Are you sure you want to sell this? (Y/N): ")
                if sure.upper() == "Y":
                    print("You have sold ", item.name)
                    return item
                else:
                    return None
        print("Item not found in inventory.")
        return None
    

with open("inventory.json", "r") as f:
    inventory = json.load(f)
with open("player_inventory.json", "r") as f:
    player = json.load(f)
def main():
    store = Store()
    while True:
        store_option = input("What do you want to do? (Buy | Sell | Exit): ")
        if store_option == "Buy":
            item_type = input("What type of item do you want to buy? - Case sensitive - (Sword | Pickaxe | Armor): ")
            if item_type == "Sword":
                item_name = input("Enter the tier before the name of the item you want to buy (Tiers: Wooden, Stone, Iron, Diamond, Netherite, God): ")
                item = store.buy_item(item_name)
                item
                info = item
                player.append(info.to_dict())
            elif item_type == "Pickaxe":
                item_name = input("Enter the tier before the name of the item you want to buy (Tiers: Wooden, Stone, Iron, Diamond, Netherite, God): ")
                item = store.buy_item(item_name)
                item
            elif item_type == "Armor":
                item_name = input("Enter the tier before the name of the item you want to buy (Tiers: Leather, Chainmail, Iron, Diamond, Netherite, God): ")
                item = store.buy_item(item_name)
                item
            else:
                print("Invalid item type.")

        elif store_option == "Sell":
            S = "S"
            while S == "S":
                I = "I"
                for Data in inventory:
                    print("Item name:", Data["Name"]) 
                    print("Item quantity:", Data["Quantity"])
                    print("Sell value:", Data["Sell value"])
                while I == "I":
                    ITEM = input("What do you want to sell? Choose 1 : ")
                    if ITEM == (Data["Name"]):
                        print("You currently have", Data["Quantity"], Data["Name"])
                        I = "A"
                        Q = "Q"
                    else:
                        ("You don't have that item, type again: ")
                while Q == "Q":
                    Quantity = int(input("How much of that item do you want to sell?: "))
                    if Quantity <= (Data["Quantity"]): 
                        New_Quantity = (Data["Quantity"]) - Quantity
                        Profit = Quantity * (Data["Sell value"])
                        print("You are going sell", Data["Quantity"], Data["Name"])
                        s = "S"
                    else:
                        print("You don't have that much items")
                while s == "S":
                    sure = input("Are you sure you want to sell", Data["Quantity"], Data["Name"])
                    if sure.upper() == "Y":
                        print("You have sold ", Quantity ,Data["Name"], "and earned", Profit, "ducats")
                        print("You now have", New_Quantity, Data["Name"])
                        """PracticeInventoryInstance.RemoveItem({ITEM: {"Description": "SKIBIDI TOIL!!!"}}) """
                    else:
                        S = "S"
                

        elif store_option == "Exit":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose Buy, Sell, or Exit.")

main()



new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(player)
    f.write(json_string)


os.remove("player_inventory.json")
os.rename(new_file, "player_inventory.json")