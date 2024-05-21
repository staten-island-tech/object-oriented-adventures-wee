import random,json
biomedata = open("./biome.json", encoding="utf8")
biomedata1 = json.load(biomedata)
from biome import biomes,biomeweights

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
player=Player(50, 10)
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
                        print ("")
                    else:
                        print ("insert combat system here")
                elif mobencounter == ["N"]:
                    for i in biomedata1:
                        if currentbiome == (i["name"]):
                            itemobtained = random.choices(i["loot"],i["chances"],k=1)
                    print ("")
                    print ("You have obtained a", (itemobtained),"!")
                    print ("")
            elif choice == ("fight"):
                if difficulty == ("peaceful"):
                    print ("")
                    print ("Fighting has been disabled as you're on peaceful difficulty.")
                    print ("")
                else:
                    print ("insert combat system here")
            elif choice == "mine":
                # Mining logic
                levels = {
                    "easy": {
                        "mobs": [Mobs("Weak Zombie", 25, 10), Mobs("Weak Skeleton", 25, 10)],
                        "ores": ["coal", "iron", "gold"]
                    },
                    "medium": {
                        "mobs": [Mobs("Medium Zombie", 40, 20), Mobs("Medium Skeleton", 40, 20)],
                        "ores": ["iron", "gold", "lapis"]
                    },
                    "hard": {
                        "mobs": [Mobs("Hard Zombie", 80, 40), Mobs("Hard Skeleton", 80, 40)],
                        "ores": ["gold", "lapis", "diamond"]
                    },
                    "extreme": {
                        "mobs": [Mobs("Extreme Zombie", 150, 80), Mobs("Extreme Skeleton", 150, 80)],
                        "ores": ["lapis", "diamond", "dragon ingot"]
                    }
                }
                def choose_level():
                    while True:
                        level = input("Choose a mining difficulty (Easy, Medium, Hard, Extreme): ").lower()
                        if level in levels:
                            return level
                        else:
                            print("Invalid difficulty. Please choose again.")
                def mine(level):
                    print(f"You have entered the {level} mines")
                    while True:
                        choice = input("Do you want to mine or leave? (Mine/Leave): ").lower()
                        if choice == "leave":
                            print("Leaving the mines.")
                            return
                        elif choice == "mine":
                            possible_outcomes = levels[level]['mobs'] + levels[level]['ores']
                            weights = [3] * len(levels[level]['mobs']) + [1] * len(levels[level]['ores'])
                            random_MO = random.choices(possible_outcomes, weights=weights, k=1)[0]
                            if random_MO in levels[level]["mobs"]:
                                mob = random_MO
                                print(f"A {mob.name} appeared!")
                                while random_MO in levels[level]['mobs']:
                                        player.health -= mob.mobdamage
                                        print(f"The {mob.name} attacked you. Your health is now {player.health}")
                                        if player.health <= 0:
                                            print("You were defeated by the mob!")
                                            return
                                        attack_run = input("What would you like to do? (Attack/Run): ")
                                        if attack_run.lower() == "attack":
                                            mob.mobhealth -= player.damage
                                            print(f"You attacked the {mob.name}. Its health is now {mob.mobhealth}")
                                            if mob.mobhealth <= 0:
                                                print(f"Congratulations, you defeated the {mob.name}!")
                                                mob.mobhealth=25
                                                break
                                        elif attack_run.lower() == "run":
                                                    print(f"You successfully ran away from the {mob.name}.")
                                                    break
                                        else:
                                            print("Invalid input. Please enter 'Attack' or 'Run'.")
                                else:
                                    ore = random_MO
                                    print(f"You found {ore} ore.")
                            else:
                                print("Invalid choice. Please choose 'Mine' or 'Leave'.")
                level = choose_level()
                mine(level)
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