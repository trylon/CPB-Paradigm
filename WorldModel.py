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
    def getWorld(self):
        self.count = self.count + 1
        return self._actions[self.count%len(self._actions)]