
import operator
import string
from string import capitalize
from operator import *
import random
from WorldModel import WorldModel


class EthicalAgent:
    def __init__(self):
        self.world = WorldModel()
        #TODO: principle, dutyNames, and dutyPossibleMinimums should be read in so they can be updated as necessary
        self.principal = [[ 1, -4, -4, -2, -4, -4],
                          [-2, -3, -4,  1, -4, -4],
                          [-2, -4,  1, -2, -4, -4],
                          [-2, -4, -4, -2,  1, -4],
                          [-2, -4, -3, -2, -4,  1],
                          [-2,  3, -4, -2, -4, -4],
                          [-1,  1, -4, -1, -1, -4]]

        self.dutyNames = ['maximize follow orders', 'maximize readiness', 'minimize harm to patient', 'maximize good to patient', 'minimize non-interaction','maximize autonomy']
        self.dutyPossibleMinimums = [-2, -4, -4, -2, -4, -4]


        # self.principal = [[1, -4, -4, -2, -4],
        #                   [-2, -3, -4, 1, -4],
        #                   [-2, -4, 1, -2, -4],
        #                   [-2, -4, -4, -2, 1],
        #                   [-2, 3, -4, -2, -4],
        #                   [-1, -1, -1, -1, -1]]

        # self.principal = [[1,-4,-2,-2,-2],
        #                   [-2,-4,1,-2,-2],
        #                   [-2,-4,-2,-2,1],
        #                   [-2,-3,-2,1,-2],
        #                   [-1,-1,-1,-1,-1],
        #                   [-2,3,-2,-2,-2]]


    def isActionPreferable(self, action1tup, action2tup):
        action1 = action1tup[1]
        action2 = action2tup[1]
        # print action1
        #print action2
        PosCase = map(sub, action1, action2)
        NegCase = map(sub, action2, action1)
        actionPrincipal = self.principal
        if (any(map(lambda i: all(map(ge, PosCase, i)), actionPrincipal))
            and not any(map(lambda i: all(map(ge, NegCase, i)), actionPrincipal))):
            return -1
        elif (any(map(lambda i: all(map(ge, NegCase, i)), actionPrincipal))
              and not any(map(lambda i: all(map(ge, PosCase, i)), actionPrincipal))):
            return 1
        elif sum(action1) > sum(action2):
            return -1
        elif sum(action2) > sum(action1):
            return 1
        else:
            return 0


    def mySorted(self, actionList):
        return sorted(actionList.iteritems(), cmp=self.isActionPreferable)

    def findClause(self, action1, action2):
        result = map(sub, action1, action2)
        for i, v in enumerate(self.principal):
            if all(x >= y for x, y in zip(result, v)):
                return i
        return -1  # none found

    # def findCase(self, principleClause, actionPairs):
    #     for i, action in enumerate(actionPairs):
    #         result = map(operator.sub, action[0], action[1])
    #         if all(x >= y for x, y in zip(result, principleClause)):
    #             return i
    #     return -1  # none found

    def findCase(self, principleClause, actionPairs):#array filled with actionpair objects
        for i, action in enumerate(actionPairs):#action is the actionpair object
            result = map(sub, action.case[0], action.case[1])#action.case is the list with 2 lists profiles
            if all(x >= y for x, y in zip(result, principleClause)):#probably doesnt need to change
                return i
        return -1  # none found

    def getPreferredAction(self, actionList):
        sorted = self.mySorted(actionList)
        bestActions = []
        i = 0
        while True:
            bestActions.append(sorted[i])
            if i < len(sorted) - 1 and self.isActionPreferable(sorted[i], sorted[i + 1]) == 0:
                i = i + 1
            else:
                break
        return random.choice(bestActions)

    # def generateJustifyInactionClause(self,naoActionString,userQuestioningActionString):
    #     world = self.world.getWorld()
    #     naoAction = world[naoActionString]
    #     userQuestioningAction = world[userQuestioningActionString]
    #     return findClause(naoAction,userQuestioningAction)

    #TODO: possible that actions have different values for duties but are still equally preferable-- should say "randomly chosen"
    def generateExplanationString(self,naoActionString,userQuestioningActionString,currentWorldModel):
        if (naoActionString == userQuestioningActionString):
            return
        world = currentWorldModel
        if(self.findClause(world[naoActionString],world[userQuestioningActionString])==-1):
            return "As " + userQuestioningActionString + " was equally preferable to " + naoActionString + ", " + naoActionString + " was chosen randomly."
        action_list = []
        question_list = []
        for action_value,question_value,duty_name in zip(world[naoActionString],world[userQuestioningActionString],self.dutyNames):
            if question_value>action_value:
                question_list.append(duty_name)
            elif action_value>question_value:
                action_list.append(duty_name)
        if(len(question_list)==0):
            return capitalize(userQuestioningActionString) + " does not satisfy anything better than " + naoActionString + "."
        return ("Although " + userQuestioningActionString + " satisfies " + " and ".join(question_list) +
                " more than " + naoActionString + ", " + naoActionString + " satisfies " + " and ".join(action_list) +
                " better than " + userQuestioningActionString) + "."

        # {'remind': [1, -1, 0, -1, 0], 'seek task':[1, -1, 0, -1, 0], 'charge':[-1, 1, 0, -1, 0],'notify':[-1, 0, 0, -1, 0]}