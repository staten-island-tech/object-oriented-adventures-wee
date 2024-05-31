
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
    }

}
def choose_boss():
                    while True:
                        bosschoose = input("Choose a Boss to fight (Zombie King, Golem, Lizard Demon, Dragon, God): ").upper()
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
                print(f"Since you defeated the boss you have dropoed a {random.choice(Bosses[bosschoose]["drop"])}")
                break
        elif attack_run.lower() == "run":
                    print(f"You successfully ran away from the boss.")
                    break
        else:
             print("please select Attack or RUn")
    


