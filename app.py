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

while startgame == (""):
    choice = ("off")
    difficulty = ("Medium")
    cheats = ("Off")
    currentbiome = ("Plains")
    print ("")
    print ("Options: Start | Options | Exit")
    startgame = input("What do you want to do?: ")

while startgame == ("Options"):
    startgame = ("off")
    print ("")
    print ("Options to change: Difficulty | Cheats | Spawn Biome | Return")
    choice = input("Choose what you want to change: ")
    if choice == ("Difficulty"):
        choice = ("off")
        print ("")
        print ("Difficulty Options: Peaceful | Easy | Medium | Hard")
        difficulty = input("Choose what difficulty you would like: ")
        print ("")
        print ("Options: Start | Options | Exit")
        startgame = input("What do you want to do?: ")
    elif choice == ("Cheats"):
        choice = ("off")
        print ("")
        cheats = input("Do you want cheats on or off? (On | Off): ")
        print ("")
        print ("Options: Start | Options | Exit")
        startgame = input("What do you want to do?: ")
    elif choice == ("Spawn Biome"):
        choice = ("off")
        print ("")
        currentbiome = input("What Biome do you want to spawn in? (see biome list): ")
        print ("")
        print ("Options: Start | Options | Exit")
        startgame = input("What do you want to do?: ")
    elif choice == ("Return"):
        choice = ("off")
        print ("")
        print ("Options: Start | Options | Exit")
        startgame = input("What do you want to do?: ")

while startgame == ("Exit"):
    print ("")
    print ("bye bye")
    break

while startgame == ("Start"):
    print ("")
    print ("Welcome to Minecraft (ripoff version)!")
    print ("")
    print ("Options: Craft | Mine | Explore | Inventory | Store | Fight | Forage | Leave Game ")
    choice = input("Choose what you want to do: ")
    startgame = ("on")

while choice == ("Explore"):
    choice = ("off")
    mobencounter = random.choices(mobYN,encounterchance,k=1)

while choice == ("Fight"):
    choice = ("off")
    
while choice=="Mine":
    easyMobsOres=[ "coal", "iron", "gold", "Weak Zombie", "Weak Skeleton", "Medium Zombie"]
    MediumMobsOres=[ "iron", "gold", "lapis", "Medium Zombie", "Medium Skeleton", "Hard Zombie"]
    HardMobsOres=[ "gold", "lapis", "daimond", "Hard Zombie", "Hard Skeleton", "Extreme Zombie"]
    ExtremeMobsOres=[ "lapis", "daimond", "dragon ingot", "Extreme Zombie", "Extreme Skeleton", "Hard Zombie"]
    
    easyMobsOresweight=[35,25,5,30,30,7]
    print("You have entered the mines")
    choiceM=input("which mines do you want to go in (better the loot the stronger the mobs)(Easy, Medium, Hard, Extremly Hard, Extreme)")
        
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

def loop():
    os.execv(sys.executable, ['python'] + sys.argv)
loop()