# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed()
# generate some integers

#def unit class

class Unit:
    #a class to represent a basic unit
    def __init__(self, rating, hitcount, status, name):
        
        self.rating = rating #attack rating 1-5
        self.hitcount = hitcount # 0 to 2, >=2: destroy unit
        self.status = status #alive 1/ -1 dead
        self.name = name #unit name
        
def unit_rating(name):
    #function to return random unit rating
    a = randint(1, 5)
    print("%s Attack Rating: " %name, a) #rating
    return(a)
    
def dice_roll(sides):
    r = randint(1, sides)
    print("Dice roll: ", r) #dice roll
    return(r)

def Attack_Test(r, a, d, n):
#function to determine result of an attack: R=roll, a= attacker, d= defender
#n = name
    result=None #init result as empty/null
    
    if r == a:
        print("%s must take hit or retreat." % n)
        num=randint(1,10)
        if (num % 2) == 0:
            result=("Retreat".format(num))
        else:
            result=("Hit!".format(num))
            #hitcount = count += 1
    #if result == hit then funcRetreat(d) else funcHit(d)
    if r < a and a > 1:
    	result=("%s Hit and retreat!" % n) #must send a stats code instead of string
    	
    if r == 1 and a >= d: #destroy
        result=("%s Destroyed!" % n)
    
    return(result)    

p=Unit(-1, 0, 1, "Big Tank") #rating, hitcount, status, name
e=Unit(-1, 0, 1, "Tanky McTankface")

p.rating=unit_rating(p.name)
e.rating=unit_rating(e.name)

dice=dice_roll(10) #10 side die


result=Attack_Test(dice, p.rating, e.rating, e.name)

if result is None:
    print("Shot miss!")
else:
    print(result)
    
    if result == "Hit!" or "Hit and retreat!":
        e.hitcount += 1
        print(e.name, " hit count: %d " %e.hitcount)
        if e.hitcount >= 2:
            e.status = -1
            print("%s Destroyed!" %e.name)
    if result == "Destroyed!":
        e.status = -1

file_type=""
file_name=""

f= open("results.txt", "a+")
f.write("%s \r\n" %result)
f.close()

