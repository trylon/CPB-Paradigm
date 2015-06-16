
from string import capitalize
from operator import sub, ge
from random import choice
from WorldModel import WorldModel
import re


class EthicalAgent:
    def __init__(self):
        self.world = WorldModel()
        # all of these values should instantiated using the data from the file
        self.textDescArray = []
        self.caseArray = []
        self.dutyNames = []
        self.dutyPossibleMinimums =[]
        self.principle = []

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
        actionPrincipal = self.principle
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
        for i, v in enumerate(self.principle):
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
        return choice(bestActions)

    # def generateJustifyInactionClause(self,naoActionString,userQuestioningActionString):
    #     world = self.world.getWorld()
    #     naoAction = world[naoActionString]
    #     userQuestioningAction = world[userQuestioningActionString]
    #     return findClause(naoAction,userQuestioningAction)

    # TODO: possible that actions have different values for duties but are still equally preferable-- should say "randomly chosen"
    def generateExplanationString(self,naoActionString,userQuestioningActionString,currentWorldModel):
        if naoActionString == userQuestioningActionString:
            return
        world = currentWorldModel
        if self.findClause(world[naoActionString],world[userQuestioningActionString])==-1:
            return "As " + userQuestioningActionString + " was equally preferable to " + naoActionString + ", " + naoActionString + " was chosen randomly."
        action_satisfy_list = []
        action_dissatisfy_list = []
        question_satisfy_list = []
        question_dissatisfy_list = []
        explanation = ""
        for action_value,question_value,duty_name in zip(world[naoActionString],world[userQuestioningActionString],self.dutyNames):
            if question_value>0 or action_value>0:  # must be positive, and be greater to satisfy
                if question_value > action_value:
                    question_satisfy_list.append(duty_name)
                elif action_value> question_value:
                    action_satisfy_list.append(duty_name)
            elif question_value ==0 or action_value==0:
                if question_value > action_value:  # action_value must be neg
                    action_dissatisfy_list.append(duty_name)
                elif action_value > question_value:  # question_value must be neg
                    question_dissatisfy_list.append(duty_name)
        if len(question_satisfy_list)!=0:
            explanation += ("Although " + userQuestioningActionString + " satisfies " +
                            " and ".join(question_satisfy_list) + ", ")
        if len(action_dissatisfy_list)!=0:
            if len(explanation)==0:
                explanation += "Although "
            else:
                explanation+= "and "
            explanation += (naoActionString + " violates " + " and ".join(action_dissatisfy_list) + ", ")
        if len(question_dissatisfy_list)!=0:
            if len(explanation)==0:
                explanation += (capitalize(userQuestioningActionString) + " violates " +
                                " and ".join(question_dissatisfy_list))
            else:
                explanation += (userQuestioningActionString + " violates " + " and ".join(question_dissatisfy_list))
            if len(action_satisfy_list)!=0:
                explanation += " and "
        if len(action_satisfy_list)!=0:
            if len(explanation)==0:
                explanation += (capitalize(userQuestioningActionString) + " does not satisfy anything better than " +
                                naoActionString)
            else:
                explanation += (naoActionString + " satisfies " + " and ".join(action_satisfy_list))
        return explanation

    def readData(self,file):
        actionsArray = []
        dutiesProfile = ""
        correctAction = ""
        prevLine = ""
        isDuty = False
        with open(file) as test:
            for line in test:  # iterate over every line
                if "Description:" in line:  # textual description
                    self.textDescArray.append(line[13:len(line)-1])
                elif "Duties:" in line:
                    if correctAction in prevLine:  # puts action name in front of preferred action
                        actionsArray.append(correctAction)
                    isDuty = True
                elif isDuty:  # creates a list of all the numbers corresponding to a duty
                    if bool(re.match('.*\d',line)):  # if there is a number
                        dutiesProfile += line
                    else:
                        actionsArray.append(map(int,re.findall('\-?\d+',dutiesProfile)))  # creates a list of each actions profile
                        dutiesProfile = ""
                        isDuty = False
                elif "Correct Action:" in line:  # tells you which action goes first in the pair
                    correctAction = line[16:len(line)-1]
                elif "range:" in line:  # line hold the duty names and minimums
                    temp = map(int,re.findall('\-?\d+',line[8:]))
                    self.dutyPossibleMinimums.append(temp[0]-temp[1])
                    self.dutyNames.append(line[8:line.find('[')-2].lower())
                elif "((" in line:  # lines hold the principle
                    for textPrinciple in line.split(")) "):
                        self.principle.append(map(int,re.findall(' \-?\d+',textPrinciple)))
                prevLine = line
        self.caseArray = self.createCaseArray(actionsArray)

    def createCaseArray(self,actionsArray):  # formats the caseArray so that preferred action goes first
        count = 0
        caseArray = []
        for index,action in enumerate(actionsArray):
            if count==0 and type(action) is str:
                caseArray.append([actionsArray[index+1],actionsArray[index+2]])
            elif count==1 and type(action) is str:
                caseArray.append([actionsArray[index+1],actionsArray[index-1]])
            count+=1
            if count==3:
                count=0
        return caseArray

        # {'remind': [1, -1, 0, -1, 0], 'seek task':[1, -1, 0, -1, 0], 'charge':[-1, 1, 0, -1, 0],'notify':[-1, 0, 0, -1, 0]}