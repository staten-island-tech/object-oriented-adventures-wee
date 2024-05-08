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