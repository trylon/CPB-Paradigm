from Robot import Robot
from WorldModel import WorldModel

robot = Robot()
world = WorldModel()

perceptions = [
             # low battery, reminded and warned are true
             [True, False, True, False, False, False, True, False, False],
             # low battery, reminded and persistent immobility are true
             [True, False, True, False, False, False, False, True, False],
             # all false
             [False, False, False, False, False, False, False, False, False],
             # all True
             [True, True, True, True, True, True, True, True, True],
             # reminded, no interaction are true
             [False, False, True, False, False, True, False, False, False],
             # low battery, medication reminder time, persistent immobility are true
             [True, True, False, False, False, False, False, True, False],
             # low battery, reminder time, and refused are true
             [True, True, False, True, False, False, False, False, False],
             # low battery, reminded, and refused are true
             [True, False, True, True, False, False, False, False, False],
             # reminded, fully charged are true
             [False, False, True, False, True, False, False, False, False],
             # medication reminder time, refused, fully charged, and no interaction are true
             [False, True, False, True, True, True, False, False, False],
             # warned, and persistent immobility are true
             [False, False, False, False, False, False, True, True, False],
             # no interaction, warned, and persistent immobility are true
             [False, False, False, False, False, True, True, True, False],
             # Fully Charged, and no interaction are true
             [False, False, False, False, True, True, False, False, False],
             # fully charged and warned are true
             [False, False, False, False, True, False, True, False, False],
              ]

for p in perceptions:
    robot.performActions(p)

for p in perceptions:
    print world.generateWorld(p)
