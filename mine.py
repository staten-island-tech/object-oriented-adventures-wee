import random,sys

class Mobs:
    def __init__(self, name, mobhealth, mobdamage):
        self.mobhealth=mobhealth
        self.mobdamage=mobdamage
        self.name=name
class Player:
    def __init__(self, health, damage):
        self.health=health
        self.damage=damage
player=Player(50, 10)
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
def choose_level():
                    while True:
                        level = input("Choose a mining difficulty (Easy, Medium, Hard, Extreme): ").lower()
                        if level in levels:
                            return level
                        else:
                            print("Invalid difficulty. Please choose again.")
                            print ("")
def mine(level):
                    print(f"You have entered the {level} mines")
                    while True:
                        choice = input("Do you want to mine or leave? (Mine/Leave): ").lower()
                        if choice == "leave":
                            print("Leaving the mines.")
                            print ("")
                            return
                        elif choice == "mine":
                            possible_outcomes = levels[level]['mobs'] + levels[level]['ores']
                            weights = [2] * len(levels[level]['mobs']) + [1] * len(levels[level]['ores'])
                            random_MO = random.choices(possible_outcomes, weights=weights, k=1)[0]
                            if random_MO in levels[level]["mobs"]:
                                mob = random_MO
                                print ("")
                                print(f"A {mob.name} appeared!")
                                player.health -= mob.mobdamage
                                if player.health > 0:
                                    print(f"The {mob.name} attacked you. Your health is now {player.health}.")
                                elif player.health <= 0:
                                    print(f"The {mob.name} attacked you. Your health is now 0.")
                                    print("You were defeated by the mob!")
                                    print("")
                                    print("GAME OVER! you fucking loser")
                                    sys.exit()
                                while random_MO in levels[level]['mobs']:
                                        attack_run = input("What would you like to do? (Attack/Run/Check): ")
                                        if attack_run.lower() == "attack":
                                            mob.mobhealth -= player.damage
                                            if mob.mobhealth > 0:
                                                print ("")
                                                print(f"You attacked the {mob.name}. Its health is now {mob.mobhealth}.")
                                                player.health -= mob.mobdamage
                                                if player.health > 0:
                                                    print(f"The {mob.name} attacked you. Your health is now {player.health}.")
                                                elif player.health <= 0:
                                                    print(f"The {mob.name} attacked you. Your health is now 0.")
                                                    print("You were defeated by the mob!")
                                                    print("")
                                                    print("GAME OVER! you fucking loser")
                                                    sys.exit()
                                            elif mob.mobhealth <= 0:
                                                print(f"Congratulations, you defeated the {mob.name}!")
                                                print ("")
                                                mob.mobhealth=25
                                                break
                                        elif attack_run.lower() == "run":
                                            print ("")
                                            print(f"You successfully ran away from the {mob.name}.")
                                            break
                                        elif attack_run.lower() == "check":
                                            print ("")
                                            print (f"Enemy HP: {mob.mobhealth}")
                                            print (f"Enemy Attack: {mob.mobdamage}")
                                        else:
                                                print("Invalid input. Please enter 'Attack' or 'Run'.")
                                        print ("")
                            elif random_MO in levels[level]["ores"]:
                                    ore = random_MO
                                    print ("")
                                    print(f"You found {ore} ore.")
                                    print ("")
                            else:
                                    print("Invalid choice. Please choose 'Mine' or 'Leave'.")
                                    print ("")


