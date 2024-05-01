import json

with open("inventory.json", "r") as f:
    inventory = json.load(f)

class Inventory:
    def __init__(self, inventory):
        self.inventory = inventory
        with open("inventory.json", "r") as f:
            inventory = json.load(f)
            self.inventory = inventory
    def view_inventory(self, inventory):
        for Data in inventory:
            print("Item name:", Data["Name"])
            print("Item quantity:", Data["Quantity"])
            print("Sell value:", Data["Sell value"])

def Filter():
    Y = "Y"
    while Y == "Y":
        Inventory.view_inventory
Filter()







