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
perception = [False,False,False,False,False,False,False,True,False]
perception2 = [False,True,False,False,False,False,False,False,False]
print world.findWorld(perception)
print world.generateWorld(perception)
print world.generateWorld(perception2)