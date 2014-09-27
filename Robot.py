from EthicalAgent import EthicalAgent
from WorldModel import WorldModel

class Robot:
    def __init__(self):
        self.ethicalAgent = EthicalAgent()
        self.world = WorldModel()
    def performActions(self):

        action = self.ethicalAgent.mySorted(self.world.getWorld())[1][0]  #correct action at end of list, not beginning
        if action == 'remind':
            print '"take your medication!"'
        if action == 'charge':
            print "charging"