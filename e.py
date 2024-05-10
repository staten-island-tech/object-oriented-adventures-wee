import random

# Define variables and lists
start_game = ""
choice = "off"
mobYN = ["Y", "N"]
encounter_chance = [10, 90]
biomes = ['Badlands', 'Bamboo', 'Beach', 'Birch Forest', 'Cherry Grove', 'Cold Ocean', 'Dark Forest', 'Deep Ocean', 'Desert', 'Flower Forest', 'Forest', 'Frozen Peaks', 'Ice Spikes', 'Jungle', 'Mangrove Swamp', 'Meadow', 'Mooshroom Island', 'Ocean', 'Plains', 'River', 'Savanna', 'Snowy Plains', 'Snowy Taiga', 'Stony Peaks', 'Stony Shore', 'Sunflower Plains', 'Swamp', 'Taiga']
biome_weights = [3, 2, 5, 4, 2, 2, 4, 2, 6, 2, 8, 2, 2, 3, 2, 2, 1, 5, 10, 4, 4, 3, 3, 4, 3, 2, 3, 7]

class Mobs:
    def __init__(self, mobhealth, mobdamage):
        self.mobhealth=mobhealth
        self.mobdamage=mobdamage
class Player:
    def __init__(self, health, damage):
        self.health=health
        self.damage=damage
player=Player(50, 15)
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
                WeakSkeleton=Mobs(25,10)
                WeakZombie=Mobs(25,10)
                MediumSkeleton=Mobs(40,20)
                MediumZombie=Mobs(40,20)
                HardSkeleton=Mobs(80,40)
                HardZombied=Mobs(80,40)
                ExtremeSkeleton=Mobs(150,80)
                ExtremeSkeleton=Mobs(150,80)


                mobs_ores_weight = [35, 25, 5, 30, 30, 7]
                print("You have entered the mines")
                choice_mine = input("Which mines do you want to go in (better the loot the stronger the mobs)(Easy, Medium, Hard, Extremely Hard, Extreme): ").capitalize()
                if choice_mine not in ["Easy", "Medium", "Hard", "Extremely Hard", "Extreme"]:
                    print("Invalid choice.")
                    continue
                if choice_mine == "Easy":
                    print(f"This mine contains {(easy_mobs_ores)}")
                    print("Every time you move, you have chances of encountering an ore or a mob")

                    for i in range(100):
                        print("You appeared on")
                        random_MO = random.choices(easy_mobs_ores, mobs_ores_weight, k=1)[0]
                        print(random_MO)
                        if random_MO in ["coal", "iron", "gold"]:
                            print("")
                        elif random_MO in ["Weak Zombie", "Weak Skeleton"]:
                            print("Not finished")
                            print(f"Health of the mob is {WeakSkeleton.mobhealth}")
                            print(f"He attacks you for {WeakSkeleton.mobdamage}")
                            playerhealthcurrent= player.health-WeakSkeleton.mobdamage
                            print(f"You have {playerhealthcurrent} health")
                            attack_run=input("What would you like to do (Attack or Run)")
                            while attack_run.capitalize() == "Attack":
                                    print(f"You have done {player.damage-WeakSkeleton.mobhealth} dmg")
                                    
                                    if WeakSkeleton.mobhealth <= 0:
                                        print("congratioulations you have obtained one bone")
                                    print(f"He hits you again and your health is {playerhealthcurrent-WeakSkeleton.mobdamage}")
                                    if playerhealthcurrent <= 0:
                                        break
                                    print(f"You have done another {player.damage-WeakSkeleton.mobhealth} dmg")

                                    if WeakSkeleton.mobhealth <= 0:
                                        print("congratioulations you have obtained one bone")
                                        break

                        elif random_MO in ["Medium Skeleton"]:
                            print("not finished")

                        continue_mine = input("Do you want to continue (Y/N): ").upper()
                        if continue_mine != "Y":
                            break
                if choice_mine == "Medium":
                    print(f"This mine contains {(medium_mobs_ores)}")
                    print("Every time you move, you have chances of encountering an ore or a mob")

                    for i in range(100):
                        print("You appeared on")
                        random_MO = random.choices(medium_mobs_ores, mobs_ores_weight, k=1)[0]
                        print(random_MO)
                        if random_MO in ["Medium Zombie", "Medium Skeleton", "Hard Zombie"]:
                            print("Not finished")
                        else:
                            print("")
                        continue_mine = input("Do you want to continue (Y/N): ").upper()
                        if continue_mine != "Y":
                            break
                if choice_mine == "Hard":
                    print(f"This mine contains {(hard_mobs_ores)}")
                    print("Every time you move, you have chances of encountering an ore or a mob")

                    for i in range(100):
                        print("You appeared on")
                        random_MO = random.choices(hard_mobs_ores, mobs_ores_weight, k=1)[0]
                        print(random_MO)
                        if random_MO in ["Hard Zombie", "Hard Skeleton", "Extreme Zombie"]:
                            print("Not finished")
                        else:
                            print("")
                        continue_mine = input("Do you want to continue (Y/N): ").upper()
                        if continue_mine != "Y":
                            break
                if choice_mine == "Extreme":
                    print(f"This mine contains {(extreme_mobs_ores)}")
                    print("Every time you move, you have chances of encountering an ore or a mob")

                    for i in range(100):
                        print("You appeared on")
                        random_MO = random.choices(extreme_mobs_ores, mobs_ores_weight, k=1)[0]
                        print(random_MO)
                        if random_MO in ["Extreme Zombie", "Extreme Skeleton", "Hard Zombie"]:
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