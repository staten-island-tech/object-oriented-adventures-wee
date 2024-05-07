class Player:
    def __init__(player, health, damage):
        player.health=health
        player.damage=damage
    health=50
    damage=10

weapon=input("did you want to buy a wepon")

if weapon.capitalize() == "Yes":
    damage=100


print(Player)

