class Character:
    def __init__(player, damage, health, starterweapon):
        player.damage=damage
        player.health=health
        player.starterweapon=starterweapon

Archer=Character(60,40, "bow")
Beserker=Character(45, 75, "Sword")
Tank=Character(30, 100, "GreatSword")
Assasin=Character(50, 50, "dagger")

class Weapon:
    def __init__(self, weapon_hitchance, weapon_critchance):
        self.weapon_hitchance=weapon_hitchance
        self.weapon_hitchance=weapon_critchance
    
bow=Weapon(0.8, 0.5)
sword=Weapon(0.9, 0.7)
greatsword=Weapon(0.5, 0.5)


characterpick=input("who you wanna pick(Berserker, Archer, Tank,or Assasin")
if characterpick == "Berserker":
    Beserker
elif characterpick == "Berserker":
    Beserker
elif characterpick == "Berserker":
    Beserker

    

