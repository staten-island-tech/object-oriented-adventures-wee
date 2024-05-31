class Inventory:
    def __init__(self, player):
        self.player = player

    def display(self):
        for item in self.player.inventory:
            print(item.name)

    def use_item(self, item_name):
        # Logic to use an item
        pass