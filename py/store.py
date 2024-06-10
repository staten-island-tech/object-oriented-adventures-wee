import json, os
""" from inventory import  PracticeInventoryInstance """

<<<<<<< Updated upstream
class Item:
=======
class Equipment:
>>>>>>> Stashed changes
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
    

with open("inventory.json", "r") as f:
    inventory = json.load(f)
<<<<<<< Updated upstream
with open("player_inventory.json", "r") as f:
    player = json.load(f)
def main():
=======
def enter_store():
>>>>>>> Stashed changes
    store = Store()
    while True:
        store_option = input("What do you want to do? (Buy | Exit): ")
        if store_option.lower() == "buy":
            item_type = input("What type of item do you want to buy? - Case sensitive - (Sword | Pickaxe | Armor): ")
            if item_type == "Sword":
                item_name = input("Enter the tier before the name of the item you want to buy (Tiers: Wooden, Stone, Iron, Diamond, Netherite, God): ")
                item = store.buy_item(item_name)
                item
            elif item_type == "Pickaxe":
                item_name = input("Enter the tier before the name of the item you want to buy (Tiers: Wooden, Stone, Iron, Diamond, Netherite, God): ")
                item = store.buy_item(item_name)
                item
                inventory.append(item.to_dict())
            elif item_type == "Armor":
                item_name = input("Enter the tier before the name of the item you want to buy (Tiers: Leather, Chainmail, Iron, Diamond, Netherite, God): ")
                item = store.buy_item(item_name)
                item
            else:
                print("Invalid item type.")

<<<<<<< Updated upstream
        elif store_option.lower() == "sell":
=======
        elif store_option.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose Buy or Exit.")

"""         elif store_option.lower() == "sell":
>>>>>>> Stashed changes
            S = "S"
            while S == "S":
                I = "I"
                for Data in inventory:
                    print("Item name:", Data["Name"]) 
                    print("Item quantity:", Data["Quantity"])
                    print("Sell value:", Data["Sell value"])
                    
                while I == "I":
                    ITEM = input("What do you want to sell? Choose 1 : ")
                    if ITEM == Data["Name"]:
                        print("You currently have", Data["Quantity"], Data["Name"])
                        I = "i"
                        Q = "Q"
                    else:
                        print("You don't have that item")
                while Q == "Q":
                    Quantity = input("How much of that item do you want to sell?: ")
<<<<<<< Updated upstream
                    if int(Quantity) <= 0:
                        print("Are you good?")
=======
                    if Quantity.isalpha() == True:
                        print("That's not a number")
                    elif Quantity == "":
                        print("Type something you moron")
>>>>>>> Stashed changes
                    elif int(Quantity) > (Data["Quantity"]):
                        print("You don't have that much items")
                    elif int(Quantity) <= 0:
                        print("Are you good?")
                    else: 
                        New_Quantity = (Data["Quantity"]) - int(Quantity)
                        Profit = int(Quantity) * (Data["Sell value"])
                        print("You are going sell", int(Quantity), Data["Name"])
                        s = "S"
                        Q = "q"
<<<<<<< Updated upstream
                    else:
                        print("That's not a number")
=======
>>>>>>> Stashed changes
                while s == "S":
                    sure = input("Are you sure you want to sell these items? Y/N ")
                    if sure.upper() == "Y":
                        print("You have sold", Quantity ,Data["Name"], "and earned", Profit, "ducats")
                        print("You now have", New_Quantity, Data["Name"])
<<<<<<< Updated upstream
                        inventory.append(.to_dict())
                        """PracticeInventoryInstance.RemoveItem({ITEM: {"Description": "SKIBIDI TOIL!!!"}}) """
=======
>>>>>>> Stashed changes
                        s = "s"
                        S = "s"
                    else:
                        print("Bro wtf")
                        s = "s"
<<<<<<< Updated upstream
                        S = "s"
                

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
=======
                        S = "s" """
>>>>>>> Stashed changes
