import random
# import random is a simple library that implements the random number generator behavior

# Please read into the variables below the correct numbers. Use try and except to catch error.
# a simple example would be:
# hero_hp = int(input("how many hp does the hero have?"))

while True:
    try:
        hero_hp= input("what is the life of the hero")
        hero_hp=int( hero_hp)
        break

    except:

     print("get a proper hero number")

while True:
    try:
         dragon_hp=input (" what is the life of the dragon")
         dragon_hp=int(dragon_hp)
         break

    except:
      print ("get a proper dragon number")

while True:
    try:
         hero_max_dmg=input (" what is the damage of the gero")
         hero_max_dmg=int(hero_max_dmg)
         break

    except:
      print ("give me a proper hero number of damage")


while True:
    try:
         dragon_max_dmg=input (" what is the damage of the dragon")
         dragon_max_dmg=int(dragon_max_dmg)
         break

    except:
      print ("give a proper dragon number of damage")

print("The dragon with", dragon_hp, "hp attacks out hero with", hero_hp, "hp")


while True:


# add a While for an infinite block
# here goes the while:
    dragon_attack = random.randint(1, dragon_max_dmg)
    # here you need to update the hero hp, you need to subtract the damage that the dragon did
    # add code on this line
    hero_hp =(hero_hp-dragon_attack)

    print("The dragon does", dragon_attack, "damage and the hero has", hero_hp, "hp left")
    # add an if condition to check if the hero was killed by the dragon
    # here goes the if
    if hero_hp <= 0:
        print("Unfortunately the dragon killed our hero. RIP sir Bravealot")
        break

    hero_attack = random.randint(1, hero_max_dmg)
    dragon_hp = dragon_hp-hero_attack
    print("The hero does", hero_attack, "damage and the dragon has", dragon_hp, "hp left")

    if dragon_hp <1:

        print("Our valiant hero has slain the dragon!")
        break

    input("Round over. Press any key")