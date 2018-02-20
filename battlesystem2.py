import random

class Dice():

    def d10(self):
        number = random.randint(0, 9)
        return number

    def d20(self):
        number = random.randint(1, 20)
        return number


class Player:

    def __init__(self, name, health, attack, heal, maxhealth, healed, enemy):
        self.name = name
        self.health = 100
        self.attack = 15
        self.heal = 50
        self.maxhealth = 100
        self.healed = False
        self.enemy = False

    def heal(self):
        if self.health < player.maxhealth:
            self.health = player.health + player.heal

        if player.health > player.maxhealth:
            self.health = player.maxhealth
        self.healed = True
        return player.health
    
name = input("What is your charaters name? ")

roll = Dice()

player = Player(
    name,
    100,
    15,
    50,
    100,
    False,
    False
)

goblinone = Player(
    'Trogd0r',
    25,
    20,
    10,
    25,
    False,
    True
)

goblinone.health = 25
goblinone.attack = 20
goblinone.maxhealth = 25

goblintwo = Player(
    'Termy Nator',
    50,
    5,
    10,
    50,
    False,
    True
)

goblintwo.health = 50
goblintwo.attack = 5
goblintwo.maxhealth = 50

goblinthree = Player(
    'St3v3 J0bzzz',
    75,
    10,
    10,
    75,
    False,
    True
)

goblinthree.health = 75
goblinthree.attack = 10
goblinthree.maxhealth = 75

goblinfour = Player(
    'Cassy Nova',
    100,
    8,
    50,
    100,
    False,
    True
)

goblinfour.health = 100
goblinfour.attack = 8
goblinfour.maxhealth = 100

#Greets player
print("Nice to meet you, " + player.name + ".")

print("4 wild goblins appear to take the sanctity of your holes away from you!!!")
print("IT'S TIME TO RUMBLE, MOTHERCLUCKER!")

combatactive = True
healcriteria = True

#Start of the combat loop
while combatactive == True:
    print("Current HP: " + str(player.health) + "/" + str(player.maxhealth)) 
    while player.healed == False and healcriteria == True:
        heal = input("Would yee like to heal? Caution: may only be used once during combat. y/n :")
        if heal == "y":
            health = player.health
            player.heal
            player.healed = True
            print(player.name + " healed for " + str(player.heal) + "HP for a total of " + str(player.health + player.heal) + "HP.")                          
        elif heal == "n":
            player.healed = False
            break
        else:
            print("Invalid syntax. y/n only.")
            healcriteria = True
    
#Prints monsters to attack   
    if goblinone.health > 0:
        print("(1) for " + goblinone.name + " " +str(goblinone.health) + "/" + str(goblinone.maxhealth) + "HP")
    else:
        print(goblinone.name + " is dead.")
        
    if goblintwo.health > 0:
        print("(2) for " + goblintwo.name + " " +str(goblintwo.health) + "/" + str(goblintwo.maxhealth) + "HP")
    else:
        print(goblintwo.name + " is dead.")

    if goblinthree.health > 0:
        print("(3) for " + goblinthree.name + " " +str(goblinthree.health) + "/" + str(goblinthree.maxhealth) + "HP")
    else:
        print(goblinthree.name + " is dead.")

    if goblinfour.health > 0:
        print("(4) for " + goblinfour.name + " " +str(goblinfour.health) + "/" + str(goblinfour.maxhealth) + "HP")
    else:
        print(goblinfour.name + " is dead.")
        
#Player attack sequence              
    attack = input("Which foul beast shall yee attack? ")
    attackable = ['1','2','3','4']
    attackcomplete = False
    while attackcomplete == False:
        if attack == '1' and goblinone.health > 0:
            smash = player.attack + roll.d20()
            goblinone.health = goblinone.health - smash
            print("Youve attacked " + goblinone.name + " for " + str(smash) + "HP.")
            attackcomplete = True
            break
        elif attack == '1' and goblinone.health <= 0:
            print("You've attacked a corpse!")
            attackcomplete = True
            break
        
        
        if attack == '2' and goblintwo.health > 0:
            smash = player.attack + roll.d20()
            goblintwo.health = goblintwo.health - smash
            print("Youve attacked " + goblintwo.name + " for " + str(smash) + "HP.")
            attackcomplete = True
            break
        elif attack == '2' and goblintwo.health <= 0:
            print("You've attacked a corpse!")
            attackcomplete = True
            break
        
            
        if attack == '3' and goblinthree.health > 0:
            smash = player.attack + roll.d20()
            goblinthree.health = goblinthree.health - smash
            print("Youve attacked " + goblinthree.name + " for " + str(smash) + "HP.")
            attackcomplete = True
            break
        elif attack == '3' and  goblinthree.health <= 0:
            print("You've attacked a corpse!")
            attackcomplete = True
            break
        
        
        if attack == '4' and goblinfour.health > 0:
            smash = player.attack + roll.d20()
            goblinfour.health = goblinfour.health - smash
            print("Youve attacked " + goblinfour.name + " for " + str(smash) + "HP.")
            attackcomplete = True
            break
        elif attack == '4' and  goblinfour.health <= 0:
            print("You've attacked a corpse!")
            attackcomplete = True
            break
        
        
        if attack not in attackable:
            print("invalid syntax. Please type 1, 2, 3 or 4.")
            attackcomplete = False

    attackcomplete = False         
        
        
# Goblin attack sequence         
    if goblinone.health > 0:        
        print(goblinone.name + " attacks!")
        x = roll.d20()
        if x > 10:
            print(goblinone.name + " hits for " + str(goblinone.attack) + " damage.")
            player.health = player.health - goblinone.attack
        else:
            print(goblinone.name + " misses.")
            
    if goblintwo.health > 0:
        print(goblintwo.name + " attacks!")
        x = roll.d20()
        if x > 10:
            print(goblintwo.name + " hits for " + str(goblintwo.attack) + " damage.")
            player.health = player.health - goblintwo.attack
        else:
            print(goblintwo.name + " misses.")
            
    if goblinthree.health > 0:
        print(goblinthree.name + " attacks!")
        x = roll.d20()
        if x > 10:
            print(goblinthree.name + " hits for " + str(goblinthree.attack) + " damage.")
            player.health = player.health - goblinthree.attack
        else:
            print(goblinthree.name + " misses.")
      
    if goblinfour.health > 0:
        print(goblinfour.name + " attacks!")
        x = roll.d20()
        if x > 10:
            print(goblinfour.name + " hits for " + str(goblinfour.attack) + " damage.")
            player.health = player.health - goblinfour.attack
        else:
            print(goblinfour.name + " misses.")
#Sets combat active to false if all monsters are dead            
    if goblinone.health <= 0 and goblintwo.health <= 0 and goblinthree.health <= 0 and goblinfour.health <= 0:
        combatactive = False
        print("YOU BEAT THE GOBLINS, FAM!")
    else:
        combatactive = True
#Sets combat active to false if player is dead
    if player.health <= 0:
        print("Oh heck, you freakin died")
        combatactive = False


      

