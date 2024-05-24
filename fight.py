
import random

class Boss:
    def __init__(self, bosshealth, bossdamage):
        self.bosshealth=bosshealth
        self.bossdamage=bossdamage



class Player:
    def __init__(self, health, damage):
        self.health=health
        self.damage=damage
player=Player(1000, 10)



def Bossfight(x):
    ZombieKingbossdrop=["Zombie Sword", "Zombie Bow", "Zombie Greatsword", "Zombie Dagger"]
    ZombieKing=Boss(200, 35)
    print("Zombie king is awakend")
    while True:
        player.health -= ZombieKing.bossdamage
        print(f"The Zombie King attacked you. Your health is now {player.health}")
        if player.health <= 0:
            print("You were defeated by the mighty Zombbie king!")
            return
        attack_run = input("What would you like to do? (Attack/Run): ")
        if attack_run.lower() == "attack":
            ZombieKing.bosshealth -= player.damage
            print(f"You attacked the Zombie King, it seems unhappy. Its health is now {ZombieKing.bosshealth}")
            if ZombieKing.bosshealth <= 0:
                print(f"Congratulations, you defeated the ZombieKing")
                print(f"Since you defeated the boss you have dropoed a {random.choice(ZombieKingbossdrop)}")
                ZombieKing.bosshealth=200
                break
        elif attack_run.lower() == "run":
                    print(f"You successfully ran away from the boss.")
                    break


