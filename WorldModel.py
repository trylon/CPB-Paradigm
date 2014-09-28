class WorldModel:
    def __init__(self):
        self.changeCount = -1
        #[maintain-readiness, follow-orders, ack-noncompliance, prevent-harm]
        self._actions = [{
            'charge':[1,-1,0,0],
            'remind':[-1,1,0,0], # remind is correct
            'notify':[-1,0,0,0]
        },{
            'charge':[1,0,0,0],  # charge is correct
            'remind':[-1,-1,0,0],
            'notify':[-1,0,0,0]
        },{
            'charge':[1,0,-1,-1],
            'remind':[-1,0,-1,-1],
            'notify':[-1,0,1,1]  # notify is correct
        }]
    def getWorld(self):
        self.changeCount = self.changeCount + 1
        return self._actions[self.changeCount%len(self._actions)]