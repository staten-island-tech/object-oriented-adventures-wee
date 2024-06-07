class Player:
    def __init__(self, health, damage, level=1, experience=0):
        self.health = health
        self.damage = damage
        self.level = level
        self.experience = experience

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.health += 20
        self.damage += 5
        print(f"You leveled up! You are now level {self.level}.")

player = Player(100, 10)
