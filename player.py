import json
import os
with open("player.json", encoding="utf8") as file:
    player = json.load(file)
class Player():
    def __init__(self, name, health, weapons, tools, ):
        self.name = name
        self.health = health
        self.weapons = weapons
        self.tools = tools


while True:
    N = input("What's the player's name?: ")
    H = int(input("How much health does the player have?(up to 1000-only accessible with cheats on- otherwise, type 100): "))
    W = input("What starting weapon do you want?(up to iron-only if cheats are on- otherwise, type Fists): ")
    T = input("What starting tool do you want?(up to iron-only if cheats are on- otherwise, type Fists): ")
    players = Player(N,H,W,T)
    player.append(players.__dict__)
    break


new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(player)
    f.write(json_string)

os.remove("player.json")
os.rename(new_file, "player.json")