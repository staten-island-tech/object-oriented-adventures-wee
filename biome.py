class Character:
    def __init__(player, damage, health, starterweapon):
        player.damage=damage
        player.health=health
        player.starterweapon=starterweapon

Archer=Character(35,15, "bow")
Beserker=Character(50, 10, "Sword")
Tank=Character(100, 30, "GreatSword"  )