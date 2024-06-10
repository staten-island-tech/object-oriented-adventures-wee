import json, os
""" from inventory import  PracticeInventoryInstance """

with open("store.json", "r") as file:
    data = json.load(file)
with open("inventory.json", "r") as f:
    inventory = json.load(f)
with open("player_inventory.json", "r") as f:
    player = json.load(f)

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.description} (Value: {self.value})"

class Equipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print("Name:", self.name)
        print("Price:", self.price)

class Sword(Equipment):
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

class Pickaxe(Equipment):
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

class Armor(Equipment):
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
        z = 0

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

    def buy_item(self, item_type, item_tier):
        item_data = data[item_type][item_tier]
        if item_type == "sword":
            item = Sword(item_data["Name"], item_data["Price"], item_data["Damage"], item_data["Crit percent"])
        elif item_type == "pickaxe":
            item = Pickaxe(item_data["Name"], item_data["Price"], item_data["Mining Power"])
        elif item_type == "armor":
            item = Armor(item_data["Name"], item_data["Price"], item_data["Health_Boost"])
        item.display_info()
        sure = input("Are you sure you want to buy this? (Y/N): ")
        if sure:
            if sure.upper() == "Y":
                #if player.
                print("You have purchased a", item.name)
                info = Equipment(item.name, item.price)
                player.append(info.to_dict())
                return item
            else:
                return None

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
    

# CREATE openstore(PLAYER OBJ) 
def enter_store():
    store = Store()
    while True:
        store_option = input("What do you want to do? (Buy | Sell | Exit): ")
        if store_option.lower() == "buy":
            item_type = input("What type of item do you want to buy? - (Sword | Pickaxe | Armor): ").lower()
            if item_type == "sword":
                item_tier = input("Enter the tier before the name of the item you want to buy (Tiers: Wood, Stone, Iron, Diamond, Netherite, God): ").lower()
                if item_tier not in ["wood", "stone", "iron", "diamond", "netherite", "god"]:
                    print("Item not found in the store.")
                    return None
            elif item_type == "pickaxe":
                item_tier = input("Enter the tier before the name of the item you want to buy (Tiers: Wood, Stone, Iron, Diamond, Netherite, God): ").lower()
                if item_tier not in ["wood", "stone", "iron", "diamond", "netherite", "god"]:
                    print("Item not found in the store.")
                    return None
            elif item_type == "armor":
                item_tier = input("Enter the tier before the name of the item you want to buy (Tiers: Leather, Chainmail, Iron, Diamond, Netherite, God): ").lower()
                if item_tier not in ["leather", "chainmail", "iron", "diamond", "netherite", "god"]:
                    print("Item not found in the store.")
                    return None
            else:
                print("Invalid item type.")
                return None
            
            store.buy_item(item_type, item_tier)

        elif store_option == "Sell":
            E = "E"
            while E == "E":
                I = "I"
                for Data in inventory:
                    print("Item name:", Data["Name"]) 
                    print("Item quantity:", Data["Quantity"])
                    print("Sell value:", Data["Sell value"])
                while I == "I":
                    ITEM = input("What do you want to sell? Choose 1 : ")
                    if ITEM == Data["Name"]:
                        print("You currently have", Data["Quantity"], Data["Name"])
                        I = "A"
                        Q = "Q"
                    else:
                        print("You don't have that item")
                while Q == "Q":
                    Quantity = int(input("How much of that item do you want to sell?: "))
                    if Quantity <= 0:
                        print("Are you stupid?")
                    elif Quantity > (Data["Quantity"]):
                        Quantity = input("How much of that item do you want to sell?: ")
                    if int(Quantity) <= 0:
                        print("Are you good?")
                    elif int(Quantity) > (Data["Quantity"]):
                        print("You don't have that much items")
                    elif 0 < int(Quantity) <= (Data["Quantity"]): 
                        New_Quantity = (Data["Quantity"]) - int(Quantity)
                        Profit = int(Quantity) * (Data["Sell value"])
                        print("You are going sell", int(Quantity), Data["Name"])
                        s = "S"
                        Q = "q"
                    else:
                        print("That's not a number")
                while S == "S":
                    sure = input("Are you sure you want to sell", Data["Quantity"], Data["Name"])
                    if sure.upper() == "Y":
                        print("You have sold ", Quantity ,Data["Name"], "and earned", Profit, "ducats")
                        print("You now have", New_Quantity, Data["Name"])
                        
                        S = "s"
                        E = "e"
                    else:
                        E = "E"
                

        elif store_option == "Exit":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose Buy, Sell, or Exit.")

    new_file = "updated.json"
    with open(new_file, "w") as f:
        json_string = json.dumps(player)
        f.write(json_string)


    os.remove("player_inventory.json")
    os.rename(new_file, "player_inventory.json")