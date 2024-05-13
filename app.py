import random
import os
import sys

startgame = ("")
choice = ("off")
mobYN = ["Y","N"]
encounterchance = [10,90]
randommob = ["Zombie"]
mobweights = [1]
biomes = ['Badlands','Bamboo','Beach','Birch Forest','Cherry Grove','Cold Ocean','Dark Forest','Deep Ocean','Desert','Flower Forest','Forest','Frozen Peaks','Ice Spikes','Jungle','Mangrove Swamp','Meadow','Mooshroom Island','Ocean','Plains','River','Savanna','Snowy Plains','Snowy Taiga','Stony Peaks','Stony Shore','Sunflower Plains','Swamp','Taiga']
biomeweights = [3,2,5,4,2,2,4,2,6,2,8,2,2,3,2,2,1,5,10,4,4,3,3,4,3,2,3,7]

while True:
    print("\nOptions: Start | Options | Exit")
    start_game = input("What do you want to do?: ").lower()
    
    if start_game == "start":
        print("\nWelcome to Minecraft (ripoff version)!")
        while True:
            print("Options: Craft | Mine | Explore | Inventory | Store | Fight | Forage | Leave Game")
            choice = input("Choose what you want to do: ").lower()

            if choice == "explore":
                # Exploration logic
                pass  # Placeholder for exploration logic
            elif start_game=="options":
                print("\nOptions to change: Difficulty | Cheats | Spawn Biome | Return")
                option = input("Choose what you want to change: ").lower()

            elif option == "difficulty":
                print("Difficulty Options: Peaceful | Easy | Medium | Hard")
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
            elif choice == "mine":
                easyMobsOres=[ "coal", "iron", "gold", "Weak Zombie", "Weak Skeleton", "Medium Zombie"]
                MediumMobsOres=[ "iron", "gold", "lapis", "Medium Zombie", "Medium Skeleton", "Hard Zombie"]
                HardMobsOres=[ "gold", "lapis", "daimond", "Hard Zombie", "Hard Skeleton", "Extreme Zombie"]
                ExtremeMobsOres=[ "lapis", "daimond", "dragon ingot", "Extreme Zombie", "Extreme Skeleton", "Hard Zombie"]
    
                easyMobsOresweight=[35,25,5,30,30,7]
                print("You have entered the mines")
                choiceM=input("which mines do you want to go in (better the loot the stronger the mobs)(Easy, Medium, Hard, Extremly Hard, Extreme)")
                leaveMine=input("DO you wanna leave?(Y,N)")
                if leaveMine!="Y":
                        break
        
                if choiceM == "Easy":  
                        print("This mine contains coal, iron, and very rare chances for gold")
                        print("Everytime you move you have chances of wondering upon a ore or a mob")
            
                for i in range(100):
                        print("you appeard on")
                        randomMO = random.choices(easyMobsOres,easyMobsOresweight, k=1)
                        print(randomMO)
                        if randomMO=="Weak Zombie":
                                print("not finished")
                        elif randomMO=="coal":
                                print("")
                        elif randomMO=="iron":
                                print("")
                        elif randomMO=="gold":
                                print("")            
                        elif randomMO=="Weak Skeleton":
                                print("")
                        elif randomMO=="Medium Zombie":
                                print("")
                continueM=input("DO you wanna continue(Y,N)")
                if continueM.upper()!="Y":
                        break
    elif choiceM == "Medium":  
            print("This mine contains iron, gold, and very rare chances for lapis")
            print("Everytime you move you have chances of wondering upon a ore or a mob")
            
            for i in range(100):
                print("you appeard on")
                randomMO = random.choices(MediumMobsOres,easyMobsOresweight, k=1)
                print(randomMO)
                if randomMO=="Medium Zombie":
                        print("not finished")
                elif randomMO=="iron":
                        print("")
                elif randomMO=="gold":
                        print("")
                elif randomMO=="lapis":
                        print("")            
                elif randomMO=="Medium Skeleton":
                        print("")
                elif randomMO=="Hard Zombie":
                        print("")
                continueM=input("DO you wanna continue(Y,N)")
                if continueM.upper()!="Y":
                        break
    elif choiceM == "Hard":  
            print("This mine contains gold, lapis, and very rare chances for daimond")
            print("Everytime you move you have chances of wondering upon a ore or a mob")
            
            for i in range(100):
                print("you appeard on")
                randomMO = random.choices(HardMobsOres,easyMobsOresweight, k=1)
                print(randomMO)
                if randomMO=="Hard Zombie":
                        print("not finished")
                elif randomMO=="gold":
                        print("")
                elif randomMO=="lapis":
                        print("")
                elif randomMO=="daimond":
                        print("")            
                elif randomMO=="Hard Skeleton":
                        print("")
                elif randomMO=="Extreme Zombie":
                        print("")
                continueM=input("DO you wanna continue(Y,N)")
                if continueM.upper()!="Y":
                        break 
    elif choiceM == "Extreme":  
            print("This mine contains lapis, daimond, and very rare chances for dragon ore")
            print("Everytime you move you have chances of wondering upon a ore or a mob")
            
            for i in range(100):
                print("you appeard on")
                randomMO = random.choices(easyMobsOres,easyMobsOresweight, k=1)
                print(randomMO)
                if randomMO=="Extreme Zombie":
                        print("not finished")
                elif randomMO=="lapis":
                        print("")
                elif randomMO=="daimond":
                        print("")
                elif randomMO=="dragon ingot":
                        print("")            
                elif randomMO=="Extreme Skeleton":
                        print("")
                elif randomMO=="Hard Zombie":
                        print("")
                continueM=input("DO you wanna continue(Y,N)")
                if continueM.upper()!="Y":
                        break           

    while choice == ("Leave Game"):
                print ("")
                print ("bye bye")
                break








        