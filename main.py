import random,json
biomedata = open("./biome.json", encoding="utf8")
biomedata1 = json.load(biomedata)
from biome import biomes,biomeweights
from mobs import easymobencounter, mediummobencounter, hardmobencounter, extrememobencounter

# Define variables and lists
start_game = ""
choice = "off"
mobYN = ["Y", "N"]
encounter_chance = [10, 90]
currentbiome = ["Plains"]
difficulty = ["normal"]
cheats = ["off"]

# Game loop
while True:
    if start_game == "exit":
        print("Bye bye!")
        break
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
                    if difficulty == ["peaceful"]:
                        for i in biomedata1:
                            if currentbiome == (i["name"]):
                                itemobtained = random.choices(i["loot"],i["chances"],k=1)
                        print ("")
                        print ("You have obtained a", (itemobtained),"!")
                        print ("")
                    elif difficulty == ["easy"]:
                        easymobencounter()
                    elif difficulty == ["medium"]:
                        mediummobencounter()
                    elif difficulty == ["hard"]:
                        hardmobencounter()
                elif mobencounter == ["N"]:
                    for i in biomedata1:
                        if currentbiome == (i["name"]):
                            itemobtained = random.choices(i["loot"],i["chances"],k=1)
                    print ("")
                    print ("You have obtained a", (itemobtained),"!")
                    print ("")
            elif choice == ("fight"):
                while difficulty == ("peaceful"):
                    print ("")
                    print ("Fighting has been disabled as you're on peaceful difficulty.")
                    print ("")
                while difficulty == ("easy"):
                    mediummobencounter(1)
                while difficulty == ("medium"):
                    hardmobencounter(1)
                while difficulty == ("hard"):
                    extrememobencounter(1)
            elif choice == "mine":
                # Mining logic
                easy_mobs_ores = ["coal", "iron", "gold", "Weak Zombie", "Weak Skeleton", "Medium Zombie"]
                medium_mobs_ores = ["iron", "gold", "lapis", "Medium Zombie", "Medium Skeleton", "Hard Zombie"]
                hard_mobs_ores = ["gold", "lapis", "diamond", "Hard Zombie", "Hard Skeleton", "Extreme Zombie"]
                extreme_mobs_ores = ["lapis", "diamond", "dragon ingot", "Extreme Zombie", "Extreme Skeleton", "Hard Zombie"]

                easy_mobs_ores_weight = [35, 25, 5, 30, 30, 7]
                print("")
                print("You have entered the mines.")
                choice_mine = input("Which mines do you want to go in? (the better the loot the stronger the mobs) (Easy, Medium, Hard, Extremely Hard, Extreme): ").capitalize()
                if choice_mine not in ["Easy", "Medium", "Hard", "Extreme"]:
                    print("Invalid choice.")
                    continue

                print ("")
                print(f"This mine contains {' and '.join(easy_mobs_ores)}")
                print("Every time you move, you have chances of encountering an ore or a mob")

                for i in range(100):
                    print ("")
                    print("You appeared on")
                    random_MO = random.choices(easy_mobs_ores, easy_mobs_ores_weight, k=1)[0]
                    print(random_MO)
                    if random_MO in ["Weak Zombie", "Weak Skeleton", "Medium Zombie"]:
                        print("Not finished")
                    else:
                        print("")
                    continue_mine = input("Do you want to continue (Y/N): ").upper()
                    if continue_mine != "Y":
                        break

            elif choice == "leave game":
                start_game = ("exit")
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
        print("bye bye!")
        break

    else:
        print("Invalid choice. Please try again.")