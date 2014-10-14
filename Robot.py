from EthicalAgent import EthicalAgent
from WorldModel import WorldModel

class Robot:
    def __init__(self):
        self.ethicalAgent = EthicalAgent()
        self.world = WorldModel()
    def performActions(self):

        actionlist = self.ethicalAgent.mySorted(self.world.getWorld())
        print actionlist
        action = actionlist[0][0]
        if action == 'remind':
            print "time to take your medication"
        if action == 'charge':
            print "charging"
        if action == 'notify':
            print "notifying the overseer"
        if action == 'seek task':
            print "seeking task"