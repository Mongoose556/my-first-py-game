# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed()
# generate some integers

#for _ in range(10):
#	value = randint(0, 10)
#	print(value)
	
#for _ in range(10):
def blue_unit():
    a = randint(1, 5)
    print("Your Attack Rating: ", a) #attacker rating
    return(a)
    
def red_unit():
    d = randint(1, 5)
    print("Enemy Attack Rating: ", d) #defender rating
    return(d)

def dice_roll(sides):
    
    r = randint(1, sides)
    print("Dice roll: ", r) #dice roll
    return(r)

def unit_hit(unit):
    
    return(totalhits)

def attacktest(r, a, d):
#attack test
    if r == a:
        print("Enemy must take hit or retreat.")
        result=randint(1,10)
        num = result    #int(input("Enter a number: "))
        if (num % 2) == 0:
            print("Retreat".format(num))
        else:
            print("Hit".format(num))
            #hitcount = count += 1
            unit_hit(d)
            
    #else:
        #print("miss")
        
    #if result == hit then funcRetreat(d) else funcHit(d)
    if r < a and a > 1:
    	print("Boom! Hit and retreat!")
    if r == 1 and a >= d: #destroy
        print("Boom! Destroyed!")
    
    return()    
    
#def hit_check():

player=blue_unit()
enemy=red_unit()
dice=dice_roll(10)

attacktest(dice, player, enemy)



    #elif a < d:
    #print("Boom! Hit and retreat!")#hit and retreat

#hit tests                
#if d == 1 or 2:
    #destroy
    
    #if d == 3:
        #1 hit
        #if def.hit == 1:
            #destroy
            #if d == 4 or 5 :
                #def hit == 1/2
                #if d hit > 2:
                    #destroy

#retreat
# check rear coord. if empty then move. if not destroy

