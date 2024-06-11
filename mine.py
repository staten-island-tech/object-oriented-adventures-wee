import random
from inventory import Inventory
class Mobs:
    def __init__(self, name, mobhealth, mobdamage):
        self.mobhealth=mobhealth
        self.mobdamage=mobdamage
        self.name=name
class Mober:
    def __init__(self, moberhealth, moberdamage):
        self.moberhealth=moberhealth
        self.moberdamage=moberdamage


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
mober = {
                    "easy": {
                        "healther":[25]
                    },
                    "medium": {
                        "healther":[40]    
                    },
                    "hard": {
                        "healther":[80]
                    },
                    "extreme": {
                        "healther":[150]
                    }
                }

def choose_level():
                    while True:
                        level = input("Choose a mining difficulty (Easy, Medium, Hard, Extreme): ").lower()
                        if level in levels:
                            return level
                        else:
                            print("Invalid difficulty. Please choose again.")
def mine(level, player):
                    print(f"You have entered the {level} mines")
                    while True:
                        choice = input("Do you want to mine or leave? (Mine/Leave): ").lower()
                        if choice == "leave":
                            print("Leaving the mines.")
                            return
                        elif choice == "mine":
                            possible_outcomes = levels[level]['mobs'] + levels[level]['ores']
                            weights = [2] * len(levels[level]['mobs']) + [1] * len(levels[level]['ores'])
                            random_MO = random.choices(possible_outcomes, weights=weights, k=1)[0]
                            if random_MO in levels[level]["mobs"]:
                                mob = random_MO
                                
                                print(f"A {mob.name} appeared!")
                                while random_MO in levels[level]['mobs']:
                                        player.health -= mob.mobdamage
                                        print(f"The {mob.name} attacked you. Your health is now {player.health}")
                                        if player.health <= 0:
                                            print("You were defeated by the mob!")
                                            player.health==150
                                            return
                                        attack_run = input("What would you like to do? (Attack/Run): ")
                                        if attack_run.lower() == "attack":
                                            mob.mobhealth -= player.damage
                                            print(f"You attacked the {mob.name}. Its health is now {mob.mobhealth}")
                                            if mob.mobhealth <= 0:
                                                print(f"Congratulations, you defeated the {mob.name}!")
                                                if level=="easy":
                                                    mob.mobhealth=25
                                                elif level=="medium":
                                                    mob.mobhealth=40
                                                if level=="hard":
                                                    mob.mobhealth=80
                                                elif level=="extreme":
                                                    mob.mobhealth=150
                                                break
                                        elif attack_run.lower() == "run":
                                                    print(f"You successfully ran away from the {mob.name}.")
                                                    break
                                        else:
                                                print("Invalid input. Please enter 'Attack' or 'Run'.")
                                                return
                            elif random_MO in levels[level]["ores"]:
                                    ore = random_MO
                                    print(f"You found {ore} ore.")
                            else:
                                    print("Invalid choice. Please choose 'Mine' or 'Leave'.")


