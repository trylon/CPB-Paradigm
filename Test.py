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
print world.findWorld(perception)