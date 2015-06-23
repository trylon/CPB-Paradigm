from Robot import Robot
from WorldModel import WorldModel

robot = Robot()
robot.performActions()
robot.performActions()
robot.performActions()
robot.performActions()
robot.performActions()
robot.performActions()
robot.performActions()

world = WorldModel()
perception = [False,False,False,False,False,False,False,False,False]
perception2 = [True,True,True,False,False,True,False,True,False] # persistent immobility case D
perception3 = [False,False,True,True,False,False,False,False,False] # case A
perception4 = [False,False,True,False,False,True,False,False,False] # case B
perception5 = [False,False,True,False,False,True,True,False,False] # case C
print world.generateWorld(perception)
print world.generateWorld(perception2)
print world.generateWorld(perception3)
print world.generateWorld(perception4)
print world.generateWorld(perception5)