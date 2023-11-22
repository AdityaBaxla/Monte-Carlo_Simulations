import random

def foundCarWithSwitch():
    doors = [0, 0 , 0] # 1 = car here
    carDoor = random.randrange(0,3)
    doors[carDoor] = 1
    selectedDoor = random.randrange(0,3)

    choices = [0,1 ,2]
    choices.remove(selectedDoor)
    try :
        choices.remove(carDoor)
    except:
        pass

    hostOpenDoor = random.choice(choices)
    
    
 
    
    #door switch
    selectedDoor = (set([0,1,2]) - set([hostOpenDoor, selectedDoor]) ).pop()
    return doors[selectedDoor] == 1

def foundCarNoSwitch():
    doors = [0, 0 , 0] # 1 = car here
    carDoor = random.randrange(0,3)
    doors[carDoor] = 1
    selectedDoor = random.randrange(0,3)


    choices = [0, 1 ,2]
    choices.remove(selectedDoor)
    try :
        choices.remove(carDoor)
    except:
        pass

    hostOpenDoor = random.choice(choices)

    

    return doors[selectedDoor] == 1


simulations = 10
timesFoundWithSwitch = 0
timesFoundNoSwitch = 0

for _ in range(simulations):
    if foundCarWithSwitch():
        timesFoundWithSwitch += 1
    if foundCarNoSwitch():
        timesFoundNoSwitch += 1
print(f'\n\n % With Switch {timesFoundWithSwitch/simulations} \t % No switch {timesFoundNoSwitch/simulations}')


    

