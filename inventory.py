import json

with open("inventory.json", "r+") as f:
    inventory = json.load(f)

class Inventory:
    inventory = []
    def __init__(self, inventory):
        self.inventory = inventory
        with open("inventory.json", "r") as f:
            inventory = json.load(f)
            self.inventory = self.items(inventory)
    def view_inventory():
        for Data in inventory:
            print("Item name:", Data["Name"])
            print("Item quantity:", Data["Quantity"])
            print("Sell value:", Data["Sell value"])
    def items(self, data):
        items = []
        for item_data in data:
            if "Name" in item_data:
                item = (item_data["Name"], item_data["Price"], item_data["Damage"], item_data["Crit percent"])
            items.append(item)
        return items