import random

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        print(f"Combat started between {self.player.role} and {self.enemy.name}")
        while self.player.health > 0 and self.enemy.health > 0:
            player_attack = random.randint(5, 15)
            enemy_attack = random.randint(5, 15)

            self.enemy.health -= player_attack
            print(f"{self.player.role} hits {self.enemy.name} for {player_attack} damage.")

            if self.enemy.health <= 0:
                print(f"{self.enemy.name} is defeated!")
                break

            self.player.health -= enemy_attack
            print(f"{self.enemy.name} hits {self.player.role} for {enemy_attack} damage.")

            if self.player.health <= 0:
                print("You are defeated!")

Combat.start()