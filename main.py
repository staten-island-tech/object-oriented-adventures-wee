import random
from biome import biomes,biomeweights,badlandsloot,badlandschances,bamboojungleloot,bamboojunglechances,beachchances,beachloot,birchforestchances,birchforestloot,cherrygrovechances,cherrygroveloot,coldoceanchances,coldoceanloot,darkforestchances,darkforestloot,deepoceanchances,deepoceanloot,desertchances,desertloot,flowerforestchances,flowerforestloot,forestchances,forestloot,frozenpeakschances,frozenpeaksloot,icespikeschances,icespikesloot,junglechances,jungleloot,mangrovechances,mangroveloot,meadowchances,meadowloot,mooshroomchances,mooshroomloot,oceanchances,oceanloot,plainschances,plainsloot,riverchances,riverloot,savannachances,savannaloot,snowyplainschances,snowyplainsloot,snowytaigachances,snowytaigaloot,sunflowerplainschances,sunflowerplainsloot,swampchances,swamploot,taigachances,taigaloot

# Define variables and lists
start_game = ""
choice = "off"
mobYN = ["Y", "N"]
encounter_chance = [10, 90]

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
                if currentbiome == (['Badlands']):
                    itemobtained = random.choices(badlandsloot,badlandschances,k=1)
                if currentbiome == (['Bamboo']):
                    itemobtained = random.choices(bamboojungleloot,bamboojunglechances,k=1)
                if currentbiome == (['Beach']):
                    itemobtained = random.choices(beachloot,beachchances,k=1)
                if currentbiome == (['Birch Forest']):
                    itemobtained = random.choices(birchforestloot,birchforestchances,k=1)
                if currentbiome == (['Cherry Grove']):
                    itemobtained = random.choices(cherrygroveloot,cherrygrovechances,k=1)
                if currentbiome == (['Cold Ocean']):
                    itemobtained = random.choices(coldoceanloot,coldoceanchances,k=1)
                if currentbiome == (['Dark Forest']):
                   itemobtained = random.choices(darkforestloot,darkforestchances,k=1)
                if currentbiome == (['Deep Ocean']):
                    itemobtained = random.choices(deepoceanloot,deepoceanchances,k=1)
                if currentbiome == (['Desert']):
                    itemobtained = random.choices(desertloot,desertchances,k=1)
                if currentbiome == (['Flower Forest']):
                    itemobtained = random.choices(flowerforestloot,flowerforestchances,k=1)
                if currentbiome == (['Forest']):
                    itemobtained = random.choices(forestloot,forestchances,k=1)
                if currentbiome == (['Frozen Peaks']):
                    itemobtained = random.choices(frozenpeaksloot,frozenpeakschances,k=1)
                if currentbiome == (['Ice Spikes']):
                    itemobtained = random.choices(icespikesloot,icespikeschances,k=1)
                if currentbiome == (['Jungle']):
                    itemobtained = random.choices(jungleloot,junglechances,k=1)
                if currentbiome == (['Mangrove Swamp']):
                    itemobtained = random.choices(mangroveloot,mangrovechances,k=1)
                if currentbiome == (['Meadow']):
                    itemobtained = random.choices(meadowloot,meadowchances,k=1)
                if currentbiome == (['Mooshroom Island']):
                    itemobtained = random.choices(mooshroomloot,mooshroomchances,k=1)
                if currentbiome == (['Ocean']):
                    itemobtained = random.choices(oceanloot,oceanchances,k=1)
                if currentbiome == (['Plains']):
                    itemobtained = random.choices(plainsloot,plainschances,k=1)
                if currentbiome == (['River']):
                    itemobtained = random.choices(riverloot,riverchances,k=1)
                if currentbiome == (['Savanna']):
                    itemobtained = random.choices(savannaloot,savannachances,k=1)
                if currentbiome == (['Snowy Plains']):
                    itemobtained = random.choices(snowyplainsloot,snowyplainschances,k=1)
                if currentbiome == (['Snowy Taiga']):
                    itemobtained = random.choices(snowytaigaloot,snowytaigachances,k=1)
                if currentbiome == (['Sunflower Plains']):
                    itemobtained = random.choices(sunflowerplainsloot,sunflowerplainschances,k=1)
                if currentbiome == (['Swamp']):
                    itemobtained = random.choices(swamploot,swampchances,k=1)
                if currentbiome == (['Taiga']):
                    itemobtained = random.choices(taigaloot,taigachances,k=1)
                print ("")
                print ("You have obtained a", (itemobtained),"!")
                print ("")

            elif choice == "mine":
                # Mining logic
                easy_mobs_ores = ["coal", "iron", "gold", "Weak Zombie", "Weak Skeleton", "Medium Zombie"]
                medium_mobs_ores = ["iron", "gold", "lapis", "Medium Zombie", "Medium Skeleton", "Hard Zombie"]
                hard_mobs_ores = ["gold", "lapis", "diamond", "Hard Zombie", "Hard Skeleton", "Extreme Zombie"]
                extreme_mobs_ores = ["lapis", "diamond", "dragon ingot", "Extreme Zombie", "Extreme Skeleton", "Hard Zombie"]

                easy_mobs_ores_weight = [35, 25, 5, 30, 30, 7]
                print("")
                print("You have entered the mines.")
                choice_mine = input("Which mines do you want to go in? (better the loot the stronger the mobs) (Easy, Medium, Hard, Extremely Hard, Extreme): ").capitalize()
                if choice_mine not in ["Easy", "Medium", "Hard", "Extremely Hard", "Extreme"]:
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
    elif start_game == "exit":
        print("Bye bye!")
        break

    else:
        print("Invalid choice. Please try again.")