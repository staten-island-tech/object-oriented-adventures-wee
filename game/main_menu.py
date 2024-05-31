from Player import Player
from app1 import print_slow, print_slower
from time import sleep
from Storyline import Storyline
class MainMenu:
    def __init__(self):
        self.options = {
            "1": self.start_game,
            "2": self.quit_game
        }

    def display(self):
        while True:
            print_slow("Main Menu")
            print_slow("1. Start Game")
            print_slow("2. Quit Game")
            choice = input("Choose an option: ")
            action = self.options.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def start_game():
        print("")
        print_slow("Starting game")
        print_slower("...")
        print_slower("     ")
        print("")
        print_slow("Game done loading")
        print("")
        # Initialize the player selection menu and start the game
        player_selection_menu = PlayerSelectionMenu()
        player_selection_menu.display()

    def quit_game(self):
        print_slow("Thank you for playing!")
        exit()

class PlayerSelectionMenu:
    def __init__(self):
        self.options = {
            "1": self.select_tank,
            "2": self.select_berserker,
            "3": self.select_archer,
            "4": self.select_assassin,
            "5": self.back_to_main
        }

    def display(self):
        print_slow("Player Selection Menu")
        print("")
        while True:
            print_slow("1. Tank")
            print("")
            print_slow("2. Berserker")
            print("")
            print_slow("3. Archer")
            print("")
            print_slow("4. Assassin")
            print("")
            print_slow("5. Back to Main Menu")
            print("")
            choice = input("Choose a character: ")
            action = self.options.get(choice)
            if action:
                action()
                break
            else:
                print_slow(f"{choice} is not a valid choice")
                print("")

    def select_tank(self):
        print("")
        print_slow("Tank selected")
        print("")
        print_slow("Your Stats:")
        print("")
        print_slow("Health: 100")
        print("")
        print_slow("Damage: 30")
        # Create a Warrior player and proceed with the game
        player = Player("Tank")
        storyline = Storyline(player)
        storyline.start()

    def select_berserker(self):
        print("")
        print_slow("Berserker selected")
        print("")
        print_slow("Your Stats:")
        print("")
        print_slow("Health: 75")
        print("")
        print_slow("Damage: 45")
        # Create a Warrior player and proceed with the game
        player = Player("Berserker")
        storyline = Storyline(player)
        storyline.start()

    def select_archer(self):
        print("")
        print_slow("Archer selected")
        print("")
        print_slow("Your Stats:")
        print("")
        print_slow("Health: 40")
        print("")
        print_slow("Damage: 60")
        # Create an Archer player and proceed with the game
        player = Player("Archer")
        storyline = Storyline(player)
        storyline.start()

    def select_assassin(self):
        print("")
        print_slow("Assassin selected")
        print("")
        print_slow("Your Stats:")
        print("")
        print_slow("Health: 50")
        print("")
        print_slow("Damage: 50")
        # Create a Mage player and proceed with the game
        player = Player("Assassin")
        storyline = Storyline(player)
        storyline.start()

    def back_to_main(self):
        main_menu = MainMenu()
        main_menu.display()
        



MainMenu.start_game()