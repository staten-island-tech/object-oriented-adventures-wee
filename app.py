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

while mobencounter == ("Y"):
    mobencounter = ("off")
    mobfight = random.choices(randommob,mobweights,k=1)
    print("")
    print("You encountered a ", (mobfight))
while mobencounter == ("N"):
    mobencounter = ("off")
    currentbiome = random.choices(biomes,biomeweights,k=1)
    print("")
    print("You've successfully travelled to a ", (currentbiome), "biome!")
    startgame = ("Start")
    print ("")
    print ("Options: Craft | Mine | Explore | Inventory | Store | Fight | Forage | Leave Game ")
    choice = input("Choose what you want to do: ")

while choice == ("Fight"):
    choice = ("off")
    

while choice == ("Leave Game"):
    print ("")
    print ("bye bye")
    break

def loop():
    os.execv(sys.executable, ['python'] + sys.argv)
loop()