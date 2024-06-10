
class Inventory:

    def __init__(self):
        self.items = []
        self.money = 0

    def add_item(self,item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def view_inventory(self):
        print("\nYour Inventory:")
        for item in self.items:
            print(item)
        print(f"Money: {self.money}")

    def add_money(self,amount):
        self.money += amount
        print(f"You gained {amount} coins")
        print(f"Your money is now this {self.money}")
        

    def spend_money(self, amount):
        if self.money >= amount:
            self.money -= amount
        else:
            print("Not enough money!")
Inventoryinstance=Inventory()
""" class InventoryInstance:
    def __init__(self, data, SlotName) -> None:
        self.data: dict = data # Dictionary
        self.inventory: list[dict] = data[SlotName]["Inventory"] # List of dictionaries

    def UpdateData(self):
        with open('inventory.json', mode='w') as outfile:
            json.dump(self.data, outfile, indent=4)
    
    def InventoryAdd(self, ItemToAdd, ItemData):
        self.inventory.append({ItemToAdd: ItemData})
        self.UpdateData()

    def RemoveItem(self, ItemToRemove: dict):
        self.inventory.remove(ItemToRemove)
        self.UpdateData()

with open("inventory.json", mode='r') as infile:
    Data = json.load(infile)

PracticeInventoryInstance = InventoryInstance(Data, "Slot1") 
 """
