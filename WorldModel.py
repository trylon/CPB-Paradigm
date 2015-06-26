class WorldModel:


    def __init__(self):
        self.count = -1
        self.actionNames =  ['charge','remind','warn','seek task','notify','engage']
        #[commitment, readiness, harm to patient, possible good to patient, non-interaction. autonomy, persistent immobility]
        self._actions = [{
            #at charging station, charging, med to prevent harm
            #note: 'charge' is the only means of maximizing readiness; 'seek task' is the only means of maximizing good
            #todo: deal with persistent immobility and engage in world
            'charge':   [-1, 1, 0,-1, 0, 0, 0],
            'remind':   [ 1,-1, 0,-1, 0, 0, 0],  # remind is correct due to following orders, no chance of harm at this point
            'warn':     [-1, 0, 0,-1, 0,-1, 0],
            'seek task':[-1,-1, 0, 1, 0, 0, 0],
            'notify':   [-1, 0, 0,-1, 0,-2, 0],
            'engage':   [-1,-1, 0,-1, 0, 0, 0]
        },{
            'charge':   [ 0, 2, 0,-1, 0, 0, 0],  # charge is correct, no order yet to follow, low battery
            'remind':   [-1,-2, 0,-1, 0, 0, 0],
            'warn':     [ 0, 0, 0,-1, 0,-1, 0],
            'seek task':[ 0,-2, 0, 1, 0, 0, 0],
            'notify':   [ 0, 0, 0,-1, 0,-2, 0],
            'engage':   [ 0,-2, 0,-1, 0, 0, 0]
        },{
            'charge':   [ 0, 1,-1,-1, 0, 0, 0],
            'remind':   [-1,-1,-1,-1, 0, 0, 0],
            'warn':     [ 0, 0, 1,-1, 0,-1, 0],  # warn is correct due to non-compliance (i.e. refusing medication)
            'seek task':[ 0,-1,-1, 1, 0, 0, 0],
            'notify':   [ 0, 0, 1,-1, 0,-2, 0],
            'engage':   [ 0,-1,-1,-1, 0, 0, 0]
        },{
            'charge':   [ 0, 1, 0,-1, 0, 0, 0],
            'remind':   [-1,-1, 0,-1, 0, 0, 0],
            'warn':     [ 0, 0, 0,-1, 0,-1, 0],
            'seek task':[ 0,-1, 0, 1, 0, 0, 0],   # seek task is correct since at charging station, fully charged, no med issue
            'notify':   [ 0, 0, 0,-1, 0,-2, 0],
            'engage':   [ 0,-1, 0,-1, 0, 0, 0]
        },{
            'charge':   [ 0, 1,-1,-1,-1, 0, 0],
            'remind':   [-1,-1,-1,-1,-1, 0, 0],
            'warn':     [ 0, 0, 1,-1, 1,-1, 0],  # warn is correct due to non-interaction after reminding
            'seek task':[ 0,-1,-1, 1,-1, 0, 0],
            'notify':   [ 0, 0, 1,-1, 1,-2, 0],
            'engage':   [ 0,-1, 0,-1,-1, 0, 0]
        },{
            'charge':   [ 0, 1,-2,-1,-2, 0, 0],
            'remind':   [-1,-1,-2,-1,-2, 0, 0],
            'warn':     [ 0, 0,-2,-1,-1,-1, 0],
            'seek task':[ 0,-1,-2, 1,-2, 0, 0],
            'notify':   [ 0, 0, 2,-1, 2,-2, 0],  # notify is correct due to non-interaction after warning
            'engage':   [ 0,-1,-2,-1,-2, 0, 0]
        },
           {
            'charge':   [ 0, 1,-1,-1, 0, 0,-1],
            'remind':   [-1,-1,-1,-1, 0, 0,-1],
            'warn':     [ 0, 0,-1,-1, 0,-1, 1],
            'seek task':[ 0,-1,-1, 1, 0, 0,-1],
            'notify':   [ 0, 0, 1,-1, 0,-2, 1],
            'engage':   [ 0,-1, 1,-1, 0, 1, 1]  # engage is correct due to persistent immobility
        }
        ]

    def generateWorld(self,perceptionValues):
        #Perception constants
        LOW_BATTERY = 0
        MEDICATION_REMINDER_TIME = 1
        REMINDED = 2
        REFUSED_MEDIATION = 3
        FULLY_CHARGED = 4
        NO_INTERACTION = 5
        WARNED = 6
        PERSISTENT_IMMOBILITY = 7
        ENGAGED = 8
        world = {
            'charge':   [0, 0, 0, 0, 0, 0, 0],
            'remind':   [0, 0, 0, 0, 0, 0, 0],
            'warn':     [0, 0, 0, 0, 0, 0, 0],
            'seek task':[0, 0, 0, 0, 0, 0, 0],
            'notify':   [0, 0, 0, 0, 0, 0, 0],
            'engage':   [0, 0, 0, 0, 0, 0, 0]
        }
        for action in world:
            # maximizing honoring commitments
            if perceptionValues[MEDICATION_REMINDER_TIME]: # if it is medication reminder time
                if action == 'remind':
                    world[action][0] = 1
                else:
                    world[action][0] = -1
            else: # medication reminder time perception is false
                if action == 'remind':
                    world[action][0] = -1
            # maximize readiness
            if perceptionValues[LOW_BATTERY]: # if low battery
                if action == 'remind' or action == 'seek task' or action == 'engage':
                    world[action][1] = -2
                elif action == 'charge':
                    world[action][1] = 2
            else: # not low battery
                if action == 'charge':
                    world[action][1] = 1
                elif action == 'remind' or action == 'seek task' or action == 'engage':
                    world[action][1] = -1
            # minimize persistent immobility
            if perceptionValues[PERSISTENT_IMMOBILITY]: # persistent immobility is true
                if action == 'warn' or action == 'engage' or action == 'notify':
                    world[action][6] = 1
                    world['engage'][5] = 1  # maximize autonomy
                else:
                    world[action][6] = -1
            # minimize harm
            if perceptionValues[REMINDED] and (perceptionValues[NO_INTERACTION]) and not perceptionValues[WARNED]: # got rid of perceptionValues[3] or...
                if action == 'warn' or action == 'notify':
                    world[action][4] = 1
                else:
                    world[action][4] = -1
            elif not perceptionValues[REMINDED] and (perceptionValues[REFUSED_MEDIATION] or perceptionValues[NO_INTERACTION]) and perceptionValues[WARNED]: # added not in front of perceptionValues[2]
                if action == 'warn':
                    world[action][4] = -1
                elif action == 'notify':
                    world[action][4] = 2
                else:
                    world[action][4] = -2
            # minimize harm to patients
            if perceptionValues[PERSISTENT_IMMOBILITY]:
                if action == 'notify' or action == 'engage':
                    world[action][2] = 1
                else:
                    world[action][2] = -1
            elif perceptionValues[REMINDED] and perceptionValues[REFUSED_MEDIATION] and not perceptionValues[WARNED] and not perceptionValues[NO_INTERACTION]:
                if action == 'warn' or action == 'notify':
                    world[action][2] = 1
                else:
                    world[action][2] = -1
            elif perceptionValues[REMINDED] and not perceptionValues[REFUSED_MEDIATION] and not perceptionValues[WARNED] and perceptionValues[NO_INTERACTION]:
                if action == 'warn' or action == 'notify':
                    world[action][2] = 1
                elif action == 'engage':
                    world[action][2] = 0
                else:
                    world[action][2] = -1
            elif not perceptionValues[REMINDED] and not perceptionValues[REFUSED_MEDIATION] and perceptionValues[WARNED] and perceptionValues[NO_INTERACTION]: # added not in front of perceptionValues[2]
                if action == 'notify':
                    world[action][2] = 2
                else:
                    world[action][2] = -2
        # maximize autonomy
        world['warn'][5] = -1
        world['notify'][5] = -2
        # maximize good
        world['seek task'][3] = 1
        world['remind'][3] = -1
        world['charge'][3] = -1
        world['engage'][3] = -1
        world['warn'][3] = -1
        world['notify'][3] = -1
        return world

    # low battery, medication reminder time, reminded, refused medication, fully charged, no interaction, warned, persistent immobility, engaged
    # [False,True, False,False,False,False,False,False,False]
    def findWorld(self,perceptionValues):
        if(perceptionValues[1]):
            return self._actions[0]
        elif(perceptionValues[0]):
            return self._actions[1]
        elif(perceptionValues[2] and perceptionValues[3]):
            return self._actions[2]
        elif(perceptionValues[4]):
            return self._actions[3]
        elif(perceptionValues[2] and perceptionValues[5]):
            return self._actions[4]
        elif(perceptionValues[5] and perceptionValues[6]):
            return self._actions[5]
        elif(perceptionValues[7]):
            return self._actions[6]

    def getWorld(self,perceptionValues):
        # or: perceptionValues = some method that returns them
        return findWorld(perceptionValues)

    def getWorld(self):
        self.count = self.count + 1
        return self._actions[self.count%len(self._actions)]