from Robot import Robot
from WorldModel import WorldModel

robot = Robot()
world = WorldModel()

perceptions = [
             # remind is correct due to following orders, no chance of harm at this point
             [False, True, False, False, False, False, False, False, False],
             # charge is correct, no order yet to follow, low battery
             [True, False, False, False, False, False, False, False, False],
             # warn is correct due to non-compliance (i.e. refusing medication)
             [False, False, True, True, False, False, False, False, False],
             # seek task is correct since at charging station, fully charged, no med issue
             [False, False, False, False, True, False, False, False, False],
             # warn is correct due to non-interaction after reminding
             [False, False, True, False, False, True, False, False, False],
             # notify is correct due to non-interaction after warning
             [False, False, False, False, False, True, True, False, False],
             # engage is correct due to persistent immobility
             [False, False, False, False, False, False, False, True, False],
              ]

for p in perceptions:
    robot.performActions(p)

for p in perceptions:
    print world.generateWorld(p)