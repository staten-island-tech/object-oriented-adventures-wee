import random

# Define variables and lists
start_game = ""
choice = "off"
mobYN = ["Y", "N"]
encounter_chance = [10, 90]
biomes = ['Badlands', 'Bamboo', 'Beach', 'Birch Forest', 'Cherry Grove', 'Cold Ocean', 'Dark Forest', 'Deep Ocean', 'Desert', 'Flower Forest', 'Forest', 'Frozen Peaks', 'Ice Spikes', 'Jungle', 'Mangrove Swamp', 'Meadow', 'Mooshroom Island', 'Ocean', 'Plains', 'River', 'Savanna', 'Snowy Plains', 'Snowy Taiga', 'Stony Peaks', 'Stony Shore', 'Sunflower Plains', 'Swamp', 'Taiga']
biome_weights = [3, 2, 5, 4, 2, 2, 4, 2, 6, 2, 8, 2, 2, 3, 2, 2, 1, 5, 10, 4, 4, 3, 3, 4, 3, 2, 3, 7]

# Game loop
while True:
    print("\nOptions: Start | Options | Exit")
    start_game = input("What do you want to do?: ").lower()
    
    if start_game == "start":
        print("\nWelcome to Minecraft (ripoff version)!")
        while True:
            print("Options: Craft | Mine | Explore | Inventory | Store | Fight | Forage | Leave Game")
            choice = input("Choose what you want to do: ").lower()

            if choice == "explore":
                # Placeholder for exploration logic
                pass

            elif choice == "options":
                while True:
                    print("\nOptions to change: Difficulty | Cheats | Spawn Biome | Return")
                    option = input("Choose what you want to change: ").lower()

                    if option == "difficulty":
                        print("\nDifficulty Options: Peaceful | Easy | Medium | Hard")
                        difficulty = input("Choose the difficulty level: ").lower()
                        if difficulty not in ["peaceful", "easy", "medium", "hard"]:
                            print("Invalid difficulty level.")
                        else:
                            print("Difficulty set to:", difficulty)

                    elif option == "cheats":
                        cheats = input("\nDo you want cheats on or off? (On | Off): ").lower()
                        if cheats not in ["on", "off"]:
                            print("Invalid choice for cheats.")
                        else:
                            print("Cheats set to:", cheats)

                    elif option == "spawn biome":
                        print("\nAvailable Biomes:", ", ".join(biomes))
                        current_biome = input("Enter the biome you want to spawn in: ").capitalize()
                        if current_biome not in biomes:
                            print("Invalid biome.")
                        else:
                            print("Spawn biome set to:", current_biome)                
                    elif option == "return":
                        break  # Exit the inner loop

                    else:
                        print("Invalid option. Please try again.")

            elif choice == "mine":
                # Mining logic
                easy_mobs_ores = ["coal", "iron", "gold", "Weak Zombie", "Weak Skeleton", "Medium Zombie"]
                medium_mobs_ores = ["iron", "gold", "lapis", "Medium Zombie", "Medium Skeleton", "Hard Zombie"]
                hard_mobs_ores = ["gold", "lapis", "diamond", "Hard Zombie", "Hard Skeleton", "Extreme Zombie"]
                extreme_mobs_ores = ["lapis", "diamond", "dragon ingot", "Extreme Zombie", "Extreme Skeleton", "Hard Zombie"]

                easy_mobs_ores_weight = [35, 25, 5, 30, 30, 7]
                print("You have entered the mines")
                choice_mine = input("Which mines do you want to go in (better the loot the stronger the mobs)(Easy, Medium, Hard, Extremely Hard, Extreme): ").capitalize()
                if choice_mine not in ["Easy", "Medium", "Hard", "Extremely Hard", "Extreme"]:
                    print("Invalid choice.")
                    continue

                print(f"This mine contains {' and '.join(easy_mobs_ores)}")
                print("Every time you move, you have chances of encountering an ore or a mob")

                for i in range(100):
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
                print("Bye bye")
                break

            else:
                print("Invalid choice. Please try again.")

    elif start_game == "exit":
        print("Bye bye!")
        break

    else:
        print("Invalid choice. Please try again.")