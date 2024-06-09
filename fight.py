
import random


class Boss:
    def __init__(self, bosshealth, bossdamage):
        self.bosshealth=bosshealth
        self.bossdamage=bossdamage








Bosses = {
    "ZOMBIE KING": {
        "drop":["Zombie Sword", "Zombie Bow", "Zombie Greatsword", "Zombie Dagger"],
        "boss":Boss(200, 35)
    },
    "GOLEM": {
        "drop":["Golem Sword", "Golem Bow", "Golem Greatsword", "Golem Dagger"],
        "boss":Boss(500, 70)
    },
    "GIANT SERPANT": {
        "drop":["Serpant Sword", "Serpant Bow", "Serpant Greatsword", "Serpant Dagger"],
        "boss":Boss(790, 170)
    },
    "DRAGON": {
        "drop":["Dragon Sword", "Dragon Bow", "Dragon Greatsword", "Dragon Dagger"],
        "boss":Boss(1600, 380)
    },
    "GOD": {
        "drop":["God Sword", "God Bow", "God Greatsword", "God Dagger"],
        "boss":Boss(4000, 700)
    }
}
def choose_boss():
                    while True:
                        bosschoose = input("Choose a Boss to fight (Zombie King, Golem, Giant Serpant, Dragon, God): ").upper()
                        if bosschoose in Bosses:
                            return bosschoose
                        elif bosschoose in Bosses:
                              print("You already defeated this boss")
                        elif bosschoose.bosshealth <= 0:
                              print("You have already defeated this boss")
                        else:
                            print("Invalid boss. Please choose again.")


def Bossfight(bosschoose, player):
    print(f"You have awakend {bosschoose}")
    print(f"{bosschoose} is awakend")
    boss=Bosses[bosschoose]["boss"]
    bossdrops=random.choice(Bosses[bosschoose]["drop"])
    while True:
        player.health -= boss.bossdamage
        print(f"The {bosschoose} attacked you. Your health is now {player.health}")
        if player.health <= 0:
            print("You were defeated!")
            return
        attack_run = input("What would you like to do? (Attack/Run): ")
        if attack_run.lower() == "attack":
            boss.bosshealth -= player.damage
            print(f"You attacked, {bosschoose} seems unhappy. Its health is now {boss.bosshealth}")
            if boss.bosshealth <= 0:
                print(f"Congratulations, you defeated the boss")
                if bosschoose=="ZOMBIE KING":
                      boss.bosshealth=200
                if bosschoose=="GOLEM":
                      boss.bosshealth=500
                if bosschoose=="GIANT SERPANT":
                      boss.bosshealth=790
                if bosschoose=="DRAGON":
                      boss.bosshealth=1600
                if bosschoose=="GOD":
                      boss.bosshealth=4000
                print(f"Since you defeated the boss you have dropoed a {bossdrops}")
                break
        elif attack_run.lower() == "run":
                    print(f"You successfully ran away from the boss.")
                    break
        else:
             print("please select Attack or RUn")
    


