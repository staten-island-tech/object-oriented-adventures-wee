import json

with open("inventory.json", "r+") as f:
    inventory = json.load(f)

class Inventory:
    inventory = []
    def __init__(self, inventory, playerinfo):
        self.inventory = inventory
        with open("inventory.json", "r") as f:
            inventory = json.load(f)
            self.inventory = self.items(inventory)
        self.player_data = playerinfo
    def view_inventory():
        for Data in inventory:
            print("Item name:", Data["Name"])
            print("Item quantity:", Data["Quantity"])
            print("Sell value:", Data["Sell value"])

class InventoryInstance:
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

""" PracticeInventoryInstance.RemoveItem({"SkibidiToilet": {"Description": "SKIBIDI TOIL!!!"}}) """
