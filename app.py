import random
from biome import biomes,biomeweights,badlandsloot,badlandschances,bamboojungleloot,bamboojunglechances,beachchances,beachloot,birchforestchances,birchforestloot,cherrygrovechances,cherrygroveloot,coldoceanchances,coldoceanloot,darkforestchances,darkforestloot,deepoceanchances,deepoceanloot,desertchances,desertloot,flowerforestchances,flowerforestloot,forestchances,forestloot,frozenpeakschances,frozenpeaksloot,icespikeschances,icespikesloot,junglechances,jungleloot,mangrovechances,mangroveloot,meadowchances,meadowloot,mooshroomchances,mooshroomloot,oceanchances,oceanloot,plainschances,plainsloot,riverchances,riverloot,savannachances,savannaloot,snowyplainschances,snowyplainsloot,snowytaigachances,snowytaigaloot,sunflowerplainschances,sunflowerplainsloot,swampchances,swamploot,taigachances,taigaloot


startgame = ("")
choice = ("off")
mobYN = ["Y","N"]
encounterchance = [10,90]
randommob = ["Zombie"]
mobweights = [1]
currentbiome = ['Plains']

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
                startgame = ("Start")
                print ("")

            if choice == ("forage"):
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

            if choice == ("Leave Game"):
                print ("")
                print ("bye bye")
                break
    elif start_game=="options":
        print("\nOptions to change: Difficulty | Cheats | Spawn Biome | Return")
        option = input("Choose what you want to change: ").lower()
        if option == "difficulty":
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
        elif choice == "Mine":
                easyMobsOres=[ "coal", "iron", "gold", "Weak Zombie", "Weak Skeleton", "Medium Zombie"]
                MediumMobsOres=[ "iron", "gold", "lapis", "Medium Zombie", "Medium Skeleton", "Hard Zombie"]
                HardMobsOres=[ "gold", "lapis", "daimond", "Hard Zombie", "Hard Skeleton", "Extreme Zombie"]
                ExtremeMobsOres=[ "lapis", "daimond", "dragon ingot", "Extreme Zombie", "Extreme Skeleton", "Hard Zombie"]
    
                easyMobsOresweight=[35,25,5,30,30,7]
                print("You have entered the mines")
                choiceM=input("which mines do you want to go in (better the loot the stronger the mobs)(Easy, Medium, Hard, Extremly Hard, Extreme)").lower()
                leaveMine=input("DO you wanna leave?(Y,N)")
                if leaveMine!="Y":
                        break
        
                if choiceM == "easy":  
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
                continueM=input("Do you wanna continue(Y,N)")
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
                continueM=input("Do you wanna continue(Y,N)")
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
                        elif randomMO=="diamond":
                                print("")            
                        elif randomMO=="Hard Skeleton":
                                print("")
                        elif randomMO=="Extreme Zombie":
                                print("")
                        continueM=input("DO you wanna continue(Y,N)")
                        if continueM.upper()!="Y":
                                break
    while start_game == ("exit"):
                print ("")
                print ("bye bye")









        