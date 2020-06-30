
#BASED ON :http://www.miielz.com/WWIII/Media/Red%20Storm%20Rising%20Board%20Game%20Basic%20Rules.pdf

# class factory example http://code.activestate.com/recipes/86900/

# generate random integer values
import random

#from random import randint

#def Unit class

class Unit:

    #add Class Decorators

    def __init__(self, name):
        self.name = name
        self.hits_remaining = 2 #track number of hits, set it to the number of hits that each unit type can survive
        self.attack_rating = random.randint(1,5)
    
    def hit(self, hit_val=1): # just subtract 1 from self.hits_remaining each time it’s called
        self.hits_remaining -= hit_val
  
    def is_alive(self): #return true or false
        return self.hits_remaining > 0
    
    def unit_status(self):

        print(self.name, " rating: ", self.attack_rating, " Hits remaining: ", self.hits_remaining)
    
    def retreat(self): #make unit move back 
        pass

    def attack(self, roll, target_unit):
        attack_result = None #init result as empty/null
        # -1 Destroy, 0 = retreat, 1 = hit, 2 = hit and retreat
    
        if roll == self.attack_rating: #roll == attack
            print(f"{target_unit.name} must take hit or retreat.")
            num = random.randint(1,10) #rand to decide hit or retreat, even to retreat, odd to hit
            if (num % 2) == 0:
                attack_result = 0 #retreat
                target_unit.retreat()
            else:
                attack_result = 1 #hit
                target_unit.hit()
                
        if roll < self.attack_rating and self.attack_rating > 1:
            attack_result = 2 #hit and retreat
            target_unit.hit()
            target_unit.retreat()

        if roll == 1 and self.attack_rating >= target_unit.attack_rating: #destroy
            attack_result = -1 #target_unit.hits_remaining = 0

        if attack_result is None: #attack has no effect
            print("Shot miss!")
        else:
            print(f"Attack result: {attack_result}")
                       
        if attack_result == 1 or 2: #"Hit!" or "Hit and retreat!":
            target_unit.hit()
            print(target_unit.name, f"HIT! Hit count: {target_unit.hits_remaining} ")

        if target_unit.is_alive == False: #e.status = -1
            print(f"{target_unit.name} Destroyed!")
        

        return attack_result 
        

############################################################################

#Dice roll function
def dice_roll():
    roll = random.randint(1, 10)# generate some integers
    print("Dice roll: ", roll) #dice roll
    return roll

#get number of turns
def get_number_of_turns():
    while True:
        try:
            turns = int(input("Number of turns (max 10): "))
        except ValueError:
            print ("Please enter a valid number")
        else:
            if turns > 10:
                turns = 10
            elif turns <= 0:
                turns = 1
        return turns


def game_loop(t): #(turns)
    
#this loop puts one unit against another until destroyed or out of turns. 
#need to change it so unit take turns to attack each other

    num_turns = t

    while num_turns > 0:

        player = Unit("") # name
        enemy = Unit("") # enemy

        print("Number of turns:", num_turns)
        
        player.name=input("Unit 1 name: ")
        enemy.name=input("Unit 2 name: ")
    
        while enemy.is_alive(): # ==True
           
            player.unit_status()
            enemy.unit_status()

            dice = dice_roll() #10 side die
            result = player.attack(dice, enemy)
          
            num_turns -=1

            f= open("results.txt", "a+")
            f.write(f"attack result {result} \r\n")
            f.close()
        else:
            print(enemy.name, "Destroyed!")
        
    else:
        print("Game Over")
        
if __name__ == "__main__":
    num_turns=(get_number_of_turns())
    game_loop(num_turns) #call game loop function, number of turns

#Add an attribute to unit called hits_remaining.  And set it to the number of hits that each unit type can survive

#Then you can simplify the game loop to just impose a hit on a unit, then do:
#If not unit.is_alive(): print(“unit dead”) or whatever
#The other thing to think about maybe is writing tests to verify that the code does what you want
#So you’d write another method that would do something like, create a unit, call hit, and then test that it’s dead
#And then maybe have a different one for rank 3 units where you call hit once, check that it’s not dead, call it twice more, then check that it is
