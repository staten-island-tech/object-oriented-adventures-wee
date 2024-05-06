import json
from inventory import Inventory
Inventory.view_inventory()

def load_inventory():
    try:
        with open("inventory.json", "r") as f:
            inventory = json.load(f)
    except FileNotFoundError:
        inventory = []
    return inventory
load_inventory()

def save_inventory(inventory):
    with open("inventory.json", "w") as f:
        json.dump(inventory, f, indent=4)
