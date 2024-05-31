class Player:
    def __init__(self, role):
        self.role = role
        self.inventory = []
        self.health = 100
        self.gold = 0

    def show_status(self):
        print(f"Role: {self.role}")
        print(f"Health: {self.health}")
        print(f"Gold: {self.gold}")
        print(f"Inventory: {self.inventory}")