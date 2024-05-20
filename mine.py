import random
from main import player

class CaveMobs:
    def __init__(self, name, mobhealth, mobdamage):
        self.mobhealth=mobhealth
        self.mobdamage=mobdamage
        self.name=name

levels = {
                    "easy": {
                        "mobs": [CaveMobs("Weak Zombie", 25, 10), CaveMobs("Weak Skeleton", 25, 10)],
                        "ores": ["coal", "iron", "gold"]
                    },
                    "medium": {
                        "mobs": [CaveMobs("Medium Zombie", 40, 20), CaveMobs("Medium Skeleton", 40, 20)],
                        "ores": ["iron", "gold", "lapis"]
                    },
                    "hard": {
                        "mobs": [CaveMobs("Hard Zombie", 80, 40), CaveMobs("Hard Skeleton", 80, 40)],
                        "ores": ["gold", "lapis", "diamond"]
                    },
                    "extreme": {
                        "mobs": [CaveMobs("Extreme Zombie", 150, 80), CaveMobs("Extreme Skeleton", 150, 80)],
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
        choice = input("Do you want to mine or leave? (Mine/Leave): ")
        if choice.lower() == "leave":
            print("Leaving the mines.")
            return
        elif choice.lower() == "mine":
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