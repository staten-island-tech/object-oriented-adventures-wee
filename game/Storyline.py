from game.utils import print_slow, print_slower
class Storyline:
    def __init__(self, player):
        self.player = player

    def start(self):
        print("")
        print_slow(f"Starting storyline for {self.player.role}...")
        print_slower("     ")
        if self.player.role == "Tank":
            print("")
            print_slower("u are a tank")
        elif self.player.role == "Berserker":
            print("")
            print_slower("u are a berserker")
            print("")
        elif self.player.role == "Archer":
            print("")
            print_slow("You are a child of a prestigious and skilled marksman from a noble family")
            print("")
            print_slow("You've always dreamt of exploring the world, and now that you're an adult")

        elif self.player.role == "Assassin":
            print("")
            print_slower("u are a assassin")
            print("")
        pass