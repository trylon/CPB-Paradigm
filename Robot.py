from EthicalAgent import EthicalAgent
from WorldModel import WorldModel
from TextFileReader import TextFileReader
from operator import sub

class Robot:
    def __init__(self):
        self.ethicalAgent = EthicalAgent()
        self.world = WorldModel()
        self.textFileReader = TextFileReader('Casebase')
        self.textFileReader.readData()

    def performActions(self):
        currentWorld = self.world.getWorld()
        actionlist = self.ethicalAgent.mySorted(currentWorld)
        print "Duties:",
        print self.ethicalAgent.dutyNames
        print "Duty Minimums:",
        print self.ethicalAgent.dutyPossibleMinimums
        print 'Principle:',
        print self.ethicalAgent.principal
        print 'Actions:',
        print actionlist
        action = actionlist[0][0]
        print "Chosen Action:",
        print action
        # if action == 'remind':
        #     print "time to take your medication"
        # if action == 'charge':
        #     print "charging"
        # if action == 'notify':
        #     print "notifying the overseer"
        # if action == 'seek task':
        #     print "seeking task"
        # if action == 'warn':
        #     print "warning"

    #Find justifying principle clause
        print 'Justifying Clauses with Differences:'
        for i in self.world.actionNames:
            print i,
            print '\t: ',
            clause_index = self.ethicalAgent.findClause(currentWorld[action],currentWorld[i])
            if clause_index == -1:
                print '\tNone'
            else:
                print self.ethicalAgent.principal[clause_index],
                print " ",
                print map(sub, currentWorld[action], currentWorld[i])
        print

  

    #Justify action
        # print self.ethicalAgent.generateExplanationString(action, 'remind',currentWorld)
        # print self.ethicalAgent.generateExplanationString(action, 'seek task',currentWorld)
        # print self.ethicalAgent.generateExplanationString(action, 'charge',currentWorld)
        # print self.ethicalAgent.generateExplanationString(action, 'warn',currentWorld)
        # print self.ethicalAgent.generateExplanationString(action, 'notify',currentWorld)
        # print