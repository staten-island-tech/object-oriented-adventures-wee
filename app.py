import random

startgame = ("off")
choice = ("off")
difficulty = ("Medium")
cheats = ("Off")
biome = ("Plains")

while startgame == ("off"):
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
        biome = input("What Biome do you want to spawn in? (see biome list): ")
        print ("")
        print ("Options: Start | Options | Exit")
        startgame = input("What do you want to do?: ")
    elif choice == ("Return"):
        choice = ("off")
        print ("")
        print ("Options: Start | Options | Exit")
        startgame = input("What do you want to do?: ")

while startgame == ("Start"):
    print ("")
    print ("Welcome to Minecraft (ripoff version)!")
    print ("")
    print ("Options: Craft | Mine | Explore | Inventory | Store | Fight | Forage | Leave Game ")
    choice = input("Choose what you want to do: ")
    startgame = ("off")

while startgame == ("Exit"):
    print ("")
    print ("bye bye")
    break

while choice == ("Leave Game"):
    print ("")
    print ("bye bye")
    break