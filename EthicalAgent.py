from operator import *
from WorldModel import WorldModel

class EthicalAgent:
    def __init__(self):
        self.world = WorldModel()
        self.principal = [[1,-4,-2,-2,-2],
                          [-2,-4,1,-2,-2],
                          [-2,-4,-2,-2,1],
                          [-2,-3,-2,1,-2],
                          [-1,-1,-1,-1,-1],
                          [-2,3,-2,-2,-2]]


    def isActionPreferable(self,action1tup, action2tup):
        action1 = action1tup[1]
        action2 = action2tup[1]
        #print action1
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


    def mySorted(self,actionList):
        return sorted(actionList.iteritems(), cmp=self.isActionPreferable)
    
    def findClause(self,action1,action2):
        result = map(operator.sub,action1,action2)
        for i,v in enumerate(self.principal):
            if all(x >= y for x, y in zip(result, v)):
                return i
        return -1 #none found
        
    def findCase(self,principleClause,actionPairs):
        for i,action in enumerate(actionPairs):
            result = map(operator.sub,action[0],action[1])
            if all(x >= y for x, y in zip(principleClause, result)):
                return i
        return -1 #none found
