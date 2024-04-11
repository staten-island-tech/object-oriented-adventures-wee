



class Mobs:
    def __init__(mob, name, damage, health, drops):
        mob.name=name
        mob.damage=damage
        mob.health=health
        mob.drops=drops

Spider=Mobs("spider", "5 dmg", "10 health", "String")
Zombie=Mobs("zombie", "5 dmg", "15 health", "Rotten Flesh")
print(Zombie(Mobs))
