# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed()
# generate some integers

#def unit class

class Unit:
    def __init__(self, rating, hitcount, status):
        
        self.rating = rating #attack rating 1-5
        self.hitcount = hitcount # 0 to 2, 3 destroy unit
        self.status = status #alive/dead
    
    #def Create_Unit(self):
        a=randint(1, 5)
        self.rating=a
        return(a)

    def GetAttackRating(self):
        print("Attack Rating: " + rating)
    def NumberOfHits(self):
        print("Hits taken " + self.hitcount)
        
    def Create_Unit(self):
        a=randint(1, 5)
        self.rating=a
        return(a)
        


def blue_unit():
    a = randint(1, 5)
    print("Your Attack Rating: ", a) #attacker rating
    #h = 0 # hit points
    return(a)
    
def red_unit():
    d = randint(1, 5)
    print("Enemy Attack Rating: ", d) #defender rating
    return(d) #return(d, h)

def dice_roll(sides):
    r = randint(1, sides)
    print("Dice roll: ", r) #dice roll
    return(r)

def attacktest(r, a, d):
#attack test
    result=None
    
    if r == a:
        print("Enemy must take hit or retreat.")
        num=randint(1,10)
        if (num % 2) == 0:
            result=("Retreat...".format(num))
        else:
            result=("Hit!".format(num))
            #hitcount = count += 1
    #if result == hit then funcRetreat(d) else funcHit(d)
    if r < a and a > 1:
    	result=("Hit and retreat!")
    	
    if r == 1 and a >= d: #destroy
        result=("Boom! Destroyed!")
    
    return(result)    

player=blue_unit()
enemy=red_unit()
dice=dice_roll(10) #10 side die

p=Unit(player, 0)
e=Unit(enemy, 0)
print(p.rating)
print(e.rating)



result=attacktest(dice, player, enemy)
if result is None:
    print("Shot miss!")
else:
    print(result)






