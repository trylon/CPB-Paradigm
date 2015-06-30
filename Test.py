from Robot import Robot
from WorldModel import WorldModel

robot = Robot()
world = WorldModel()
# remind is correct due to following orders, no chance of harm at this point
perception1 = [False,True,False,False,False,False,False,False,False]
# charge is correct, no order yet to follow, low battery
perception2 = [True,False,False,False,False,False,False,False,False]
# warn is correct due to non-compliance (i.e. refusing medication)
perception3 = [False,False,True,True,False,False,False,False,False]
# seek task is correct since at charging station, fully charged, no med issue
perception4 = [False,False,False,False,True,False,False,False,False]
# warn is correct due to non-interaction after reminding
perception5 = [False,False,True,False,False,True,False,False,False]
# notify is correct due to non-interaction after warning
perception6 = [False,False,False,False,False,True,True,False,False]
# engage is correct due to persistent immobility
perception7 = [False,False,False,False,False,False,False,True,False]
robot.performActions(perception1)
robot.performActions(perception2)
robot.performActions(perception3)
robot.performActions(perception4)
robot.performActions(perception5)
robot.performActions(perception6)
robot.performActions(perception7)
print world.generateWorld(perception1)
print world.generateWorld(perception2)
print world.generateWorld(perception3)
print world.generateWorld(perception4)
print world.generateWorld(perception5)
print world.generateWorld(perception6)
print world.generateWorld(perception7)