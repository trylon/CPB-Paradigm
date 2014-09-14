class WorldModel:
    def __init__(self):
        self.changeCount = -1
        self._actions = [{
            'charge':[1,-1],
            'remind':[-1,1]
        },{
            'remind':[1,-1],
            'charge':[-1,1]
        }]
    def getWorld(self):
        self.changeCount = self.changeCount + 1
        return self._actions[self.changeCount%len(self._actions)]