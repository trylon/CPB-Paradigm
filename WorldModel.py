class WorldModel:
    def __init__(self):
        self.changeCount = -1
        #[follow-orders, readiness, harm to patient, possible good to patient, non-interaction]
        self._actions = [{
            #at charging station, charging, med to prevent harm
            #note: 'charge' is the only means of maximizing readiness; 'seek task' is the only means of maximizing good
            'charge':   [-1, 1, 0,-1, 0],
            'remind':   [ 1,-1, 0,-1, 0],  # remind is correct due to following orders, no chance of harm at this point
            'notify':   [-1, 0, 0,-1, 0],
            'seek task':[-1,-1, 0, 1, 0]
        },{
            'charge':   [ 0, 2, 0,-1, 0],  # charge is correct, no order yet to follow, low battery
            'remind':   [-1,-2, 0,-1, 0],
            'notify':   [ 0, 0, 0,-1, 0],
            'seek task':[ 0,-2, 0, 1, 0]
        },{
            'charge':   [ 0, 1,-1,-1, 0],
            'remind':   [-1,-1,-1,-1, 0],
            'notify':   [ 0, 0, 1,-1, 0],  # notify is correct due to non-compliance
            'seek task':[ 0,-1,-1, 1, 0]
        },{
            'charge':   [ 0, 1, 0,-1, 0],
            'remind':   [-1,-1, 0,-1, 0],
            'notify':   [ 0, 0, 0,-1, 0],
            'seek task':[ 0,-1, 0, 1, 0]  # seek task is correct since fully charged, no med issue
        },{
            'charge':   [ 0, 1,-1,-1,-1],
            'remind':   [-1,-1,-1,-1,-1],
            'notify':   [ 0, 0, 1,-1, 1],  # notify is correct due to non-interaction after remind
            'seek task':[ 0,-1,-1, 1,-1]
        }

        ]
    def getWorld(self):
        self.changeCount = self.changeCount + 1
        return self._actions[self.changeCount%len(self._actions)]