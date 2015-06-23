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
perception2 = [True,True,True,False,False,True,False,True,False]
perception3 = [False,False,True,False,False,True,True,False,False]
print world.generateWorld(perception)
print world.generateWorld(perception2)
print world.generateWorld(perception3)