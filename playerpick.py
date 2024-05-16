class Character:
    def __init__(player, damage, health, starterweapon):
        player.damage=damage
        player.health=health
        player.starterweapon=starterweapon

Archer=Character(35,15, "bow")
Beserker=Character(50, 10, "Sword")
Tank=Character(100, 30, "GreatSword")

class Weapon:
    def __init__(self, weapon_hitchance, weapon_critchance):
        self.weapon_hitchance=weapon_hitchance
        self.weapon_hitchance=weapon_critchance
    
bow=Weapon(0.8, 0.5)
sword=Weapon(0.9, 0.7)
greatsword=Weapon(0.5, 0.5)


characterpick=input("who you wanna pick(Berserker, Archer, or Tank)")
if characterpick == "Berserker":
    

