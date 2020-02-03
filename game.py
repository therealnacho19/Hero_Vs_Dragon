import random

hero_hp = 50
dragon_hp = 100
hero_max_dmg = 20
dragon_max_dmg = 10

print("The dragon with {} hp attacks our hero with {} hp".format(dragon_hp, hero_hp))

while True:
    dragon_attack = random.randint(1, dragon_max_dmg)
    hero_hp = hero_hp - dragon_attack
    print("The dragon does {} damage and the hero has {} hp left".format(dragon_attack, hero_hp))
    if hero_hp <= 0:
        print("The hero is dead")
        break

    hero_attack = random.randint(1, hero_max_dmg)
    dragon_hp = dragon_hp - hero_attack
    print("The hero does {} damage and the dragon has {} hp left".format(hero_attack, dragon_hp))
    if dragon_hp <= 0:
        print("The dragon is dead")
        break

    input("Round over, press any key")