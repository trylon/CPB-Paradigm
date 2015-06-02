from EthicalAgent import EthicalAgent
from WorldModel import WorldModel
from TextFileReader import TextFileReader

class Robot:
    def __init__(self):
        self.ethicalAgent = EthicalAgent()
        self.world = WorldModel()
        self.textFileReader = TextFileReader('Casebase')
        self.textFileReader.readData()

    def performActions(self):
        currentWorld = self.world.getWorld()
        actionlist = self.ethicalAgent.mySorted(currentWorld)
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
        if action == 'warn':
            print "warning"

    #Justify action
        print self.ethicalAgent.generateExplanationString(action, 'remind',currentWorld)
        print self.ethicalAgent.generateExplanationString(action, 'seek task',currentWorld)
        print self.ethicalAgent.generateExplanationString(action, 'charge',currentWorld)
        print self.ethicalAgent.generateExplanationString(action, 'warn',currentWorld)
        print self.ethicalAgent.generateExplanationString(action, 'notify',currentWorld)
        print