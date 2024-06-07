""" class ItemInventory:
    def __init__(self, name='', count=0, cost=0.0, category='')
        self.name = name
        self.count = count
        self.cost = cost
        self.category = category

    def get_input(self):
        self.name = input('Enter item name: ')
        self.count = int(input('Enter item count: '))
        self.cost = float(input('Enter unit cost: '))
        self.category = input('Enter category: ')
"""  """
    def __str__(self):
        return f"{self.name}\n"
               f"\tCount: {self.count}, Cost: {self.cost}\n"
               f"\tCategory: {self.category}"
        

category_list = ['Food', 'Drink', 'Merch']

def main():
    inventory = []
    
    # Create a loop in which the user can add multiple items in inventory list.
    answer = ''
    while answer.lower() != 'n':
            # Create an object, ask the user for item input using object's method,
            # then append object to inventory lsit.
            new_item = ItemInventory()
            new_item.get_input()
            inventory.append(ItemInventory(new_item))

            answer = input('Enter more items? ')

    # I need to print the items in each category. I'm required to have a 
    # specific function for this.
    for category in category_list:
        display_category(category, inventory)

    # One more function that displays ALL items in inventory.
    display_inventory(inventory)


def display_category(category_name, inventory):
    header = f'Items in {category_name}'
    divider = len(header) * '-'
    print(header)
    print(divider)
    
    for item in inventory:
        if category_name in item:
            print(item)
        else:
            return 'Category empty.'

def display_inventory(inventory):
    print()
    print('Current Inventory')
    print('-----------------')
    if len(inventory) == 0:
        print('Inventory empty.')
    else:
        print(Inventory)


main()


"https://www.reddit.com/r/learnpython/comments/17lhaj7/first_time_working_with_classes_how_do_i_append/?rdt=50242" """