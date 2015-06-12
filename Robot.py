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
        print
        print "World State ",
        print self.world.count
        print "Duties:",
        print self.ethicalAgent.dutyNames
        print "Duty Minimums:",
        print self.ethicalAgent.dutyPossibleMinimums
        print 'Principle:',
        print self.ethicalAgent.principal
        print 'Sorted Actions:',
        print actionlist
        action = actionlist[0][0]
        print "Chosen Action:",
        print action + " ",
        print currentWorld[action]

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
        print "-----------------------------------------------------------------------------------"
        print '\t\t\tAction\t\t\t\t\tDifferences\t\t\t\tJustifying Clause'
        for i in self.world.actionNames:
            print i,
            print '\t: ',
            print currentWorld[i],
            clause_index = self.ethicalAgent.findClause(currentWorld[action],currentWorld[i])
            if clause_index == -1:
                print '\tNone\t\t\t\t\tNone'
            else:
                print " ",
                print map(sub, currentWorld[action], currentWorld[i]),
                print " ",
                print self.ethicalAgent.principal[clause_index]
        print

    #todo: justification strategy [work in progress]
        #if all justifying clauses are the same,
        #  state all duties values in the clause that are not minimums and have positive values in the chosen action
        #  ex. remind in state 0; 'maximize follow orders' is the only non-minimum valued duty in clause that meets the criterion
        #      "I chose remind because I was told to at this time."

        #if only one justifying clause differs from the others,
        #
        #  ex. seek task in the state 3
  

    #Justify action
        # print self.ethicalAgent.generateExplanationString(action, 'remind',currentWorld)
        # print self.ethicalAgent.generateExplanationString(action, 'seek task',currentWorld)
        # print self.ethicalAgent.generateExplanationString(action, 'charge',currentWorld)
        # print self.ethicalAgent.generateExplanationString(action, 'warn',currentWorld)
        # print self.ethicalAgent.generateExplanationString(action, 'notify',currentWorld)
        # print