from EthicalAgent import EthicalAgent
from WorldModel import WorldModel

class Robot:
    def __init__(self):
        self.ethicalAgent = EthicalAgent(
            [[-1, -1, -1, -2], [-2, 1, -2, -2], [-2, -2, 1, -2]]
        )
        self.world = WorldModel()
    def performActions(self):

        action = self.ethicalAgent.mySorted(self.world.getWorld())[0][0]
        if action == 'remind':
            print "time to take your medication"
        if action == 'charge':
            print "charging..."
        if action == 'notify':
            print "notifying the overseer"