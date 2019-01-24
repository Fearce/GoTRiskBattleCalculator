import random

def work():
    while True:
        attackers = input('number attackers? ')
        defenders = input('number defenders? ')
        do_battle(int(attackers), int(defenders))
            
            
def do_battle(atk, defense):
    attackRolls = []
    defenseRolls = []
    defLost = 0
    atkLost = 0
    print("You attacked " + str(defense) + " troops with " + str(atk))
    for i in range(int(atk)):
        attackRolls.append(Roll())
    print("Attack rolls : " + str(attackRolls))
    for i in range(int(defense)):
        defenseRolls.append(Roll())
    print("Defense rolls : " + str(defenseRolls))
    while len(attackRolls) > 0 and len(defenseRolls) > 0:
        if GetLargest(len(attackRolls), attackRolls) > GetLargest(len(defenseRolls), defenseRolls):
            defLost += 1
            print("Attack win. " + str(GetLargest(len(attackRolls), attackRolls)) + " beats " + str(GetLargest(len(defenseRolls), defenseRolls)))
            attackRolls.remove(GetLargest(len(attackRolls), attackRolls))
            defenseRolls.remove(GetLargest(len(defenseRolls), defenseRolls))
        else:
            atkLost += 1
            print("Defense win. " + str(GetLargest(len(defenseRolls), defenseRolls)) + " beats " + str(GetLargest(len(attackRolls), attackRolls)))
            attackRolls.remove(GetLargest(len(attackRolls), attackRolls))
            defenseRolls.remove(GetLargest(len(defenseRolls), defenseRolls))
    print("Defense loses " + str(defLost) + " attack loses " + str(atkLost) + "\n")
        
        
        
def GetLargest(n, a): # n = elements, a = array of ints
    a.sort()
    return a[n-1]
    

def Roll():
    return random.randint(1,6)
    
    
work()    
