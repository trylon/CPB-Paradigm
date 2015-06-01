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
        if action == 'warn':
            print "warning"


        print self.ethicalAgent.generateExplanationString(action, 'remind')
        print self.ethicalAgent.generateExplanationString(action, 'seek task')
        print self.ethicalAgent.generateExplanationString(action, 'charge')
        print self.ethicalAgent.generateExplanationString(action, 'warn')
        print self.ethicalAgent.generateExplanationString(action, 'notify')
        print