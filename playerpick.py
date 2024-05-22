class Character:
    def __init__(player, damage, health, starterweapon):
        player.damage=damage
        player.health=health
        player.starterweapon=starterweapon

Archer=Character(20,40, "bow")
Beserker=Character(15, 50, "Sword")
Tank=Character(30, 100, "GreatSword")
Assasin=Character(25, 30, "dagger")



class Weapon:
    def __init__(self, weapon_hitchance, weapon_critchance):
        self.weapon_hitchance=weapon_hitchance
        self.weapon_hitchance=weapon_critchance
    
bow=Weapon(0.8, 0.5)
sword=Weapon(0.9, 0.7)
greatsword=Weapon(0.5, 0.5)


characterpick=input("who you wanna pick(Berserker, Archer, or Tank)")
if characterpick == "Berserker":
    Beserker
if characterpick == "Berserker":
    Beserker
if characterpick == "Berserker":
    Beserker

    

