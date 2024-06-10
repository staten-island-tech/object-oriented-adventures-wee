import random,json
biomedata = open("./biome.json", encoding="utf8")
biomedata1 = json.load(biomedata)
from biome import biomes,biomeweights
from fight import Bosses
from fight import Bossfight, choose_boss
from mine import levels
from mine import choose_level, mine
from inventory import Inventory
Inventoryinstance=Inventory()
                
# Define variables and lists
start_game = ""
choice = "off"
mobYN = ["Y", "N"]
encounter_chance = [20, 80]
currentbiome = ["Plains"]
difficulty = ["normal"]
difficulty1 = ["normal"]
cheats = ["off"]

class Mobs:
    def __init__(self, name, mobhealth, mobdamage):
        self.mobhealth=mobhealth
        self.mobdamage=mobdamage
        self.name=name
class Player:
    def __init__(self, health, damage):
        self.health=health
        self.damage=damage
player=Player(10000, 5)
# Game loop
while True:
    print("\nOptions: Start | Options | Exit")
    start_game = input("What do you want to do?: ").lower()
    if start_game == "start":
        print("\nWelcome to Minecraft (ripoff version)!")
        while True:
            print("Options: Mine | Explore | Inventory | Store | Fight | Forage | Leave Game")
            choice = input("Choose what you want to do: ").lower()
            if choice == "explore":
                currentbiome = random.choices(biomes,biomeweights,k=1)
                print("")
                print("You've successfully travelled to a ", (currentbiome), "biome!")
                print ("")
            elif choice == ("forage"):
                mobencounter = random.choices(mobYN,encounter_chance,k=1)
                if mobencounter == ["Y"]:
                    if difficulty == ("peaceful"):
                        for i in biomedata1:
                            if currentbiome == (i["name"]):
                                itemobtained = random.choices(i["loot"],i["chances"],k=1)
                        print ("")
                        print ("You have obtained a", (itemobtained),"!")
                        Inventoryinstance.add_item(itemobtained)
                        print ("")
                    else:
                        print ("insert combat system here")
                elif mobencounter == ["N"]:
                    for i in biomedata1:
                        if currentbiome == (i["name"]):
                            itemobtained = random.choices(i["loot"],i["chances"],k=1)
                    print ("")
                    print ("You have obtained a", (itemobtained),"!")
                    Inventoryinstance.add_item(itemobtained)
                    print ("")
            elif choice == ("fight"):
                chooseboss=choose_boss()
                Bossfight(chooseboss, player)
            elif choice == ("inventory"):
                
                Inventoryinstance.view_inventory()
            elif choice == "mine":
                # Mining logic
                level = choose_level()
                mine(level, player)
            elif choice == "leave game":
                print("")
                break
            else:
                print("Invalid choice. Please try again.")
    elif start_game == "options":
        while True:
            print("\nOptions to change: Difficulty | Cheats | Spawn Biome | Return")
            option = input("Choose what you want to change: ").lower()
            if option == "difficulty":
                print("\nDifficulty Options: Peaceful | Easy | Medium | Hard")
                difficulty1 = input("Choose the difficulty level: ").lower()
                if difficulty1 not in ["peaceful", "easy", "medium", "hard"]:
                    print("Invalid difficulty level.")
                else:
                    print("Difficulty set to:", difficulty1)
                    difficulty = difficulty1
            elif option == "cheats":
                cheats1 = input("\nDo you want cheats on or off? (On | Off): ").lower()
                if cheats1 not in ["on", "off"]:
                    print("Invalid choice for cheats.")
                else:
                    print("Cheats set to:", cheats1)
                    cheats = cheats1
            elif option == "spawn biome":
                print("\nAvailable Biomes:", ", ".join(biomes))
                currentbiome1 = input("Enter the biome you want to spawn in (CASE SENSITIVE): ")
                if currentbiome1 not in biomes:
                    print("Invalid biome.")
                else:
                    print("Spawn biome set to:", currentbiome1)      
                    currentbiome = [currentbiome1]          
            elif option == "return":
                break  # Exit the inner loop
            else:
                print("Invalid option. Please try again.")
    elif start_game == "exit":
        print("Bye bye!")
        break
    else:
        print("Invalid choice. Please try again.")
        