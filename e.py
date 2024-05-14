import random

# Define variables and lists
start_game = ""
choice = "off"
mobYN = ["Y", "N"]
encounter_chance = [10, 90]
biomes = ['Badlands', 'Bamboo', 'Beach', 'Birch Forest', 'Cherry Grove', 'Cold Ocean', 'Dark Forest', 'Deep Ocean', 'Desert', 'Flower Forest', 'Forest', 'Frozen Peaks', 'Ice Spikes', 'Jungle', 'Mangrove Swamp', 'Meadow', 'Mooshroom Island', 'Ocean', 'Plains', 'River', 'Savanna', 'Snowy Plains', 'Snowy Taiga', 'Stony Peaks', 'Stony Shore', 'Sunflower Plains', 'Swamp', 'Taiga']
biome_weights = [3, 2, 5, 4, 2, 2, 4, 2, 6, 2, 8, 2, 2, 3, 2, 2, 1, 5, 10, 4, 4, 3, 3, 4, 3, 2, 3, 7]

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
                print("Bye bye")
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